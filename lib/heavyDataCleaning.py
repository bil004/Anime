import duckdb

"""
Module: heavyDataCleaning
Summary: High-volume data cleaning routines leveraging DuckDB.
Description: Provides performant transformations for large CSV inputs, producing de-duplicated
             and normalized outputs suitable for analytics.

Swagger/OpenAPI:
  tags:
    - name: ETL
      description: High-performance cleaning and transformation steps.
"""


def clean_ratings_table(input_path: str, output_path: str = None):
    """
    Summary:
        Clean a ratings CSV by removing null usernames, deduplicating, and selecting key columns.
    Description:
        Loads a CSV via DuckDB, filters out rows with null usernames, applies distinct,
        and casts fields to compact types. Optionally writes the cleaned result to Parquet.

    Parameters:
        input_path (str): Path to the source CSV file.
        output_path (str | None): Optional path to write a Parquet file (Snappy compressed). If None, returns a DuckDB relation.

    Returns:
        duckdb.DuckDBPyRelation | None: Cleaned relation if output_path is None; otherwise None after writing to disk.

    Swagger/OpenAPI:
      operationId: cleanRatingsTable
      tags:
        - ETL
      parameters:
        - name: input_path
          in: body
          required: true
          schema:
            type: string
          description: Filesystem path to the input ratings CSV.
        - name: output_path
          in: body
          required: false
          schema:
            type: string
            nullable: true
          description: Filesystem path to output Parquet; if omitted, returns an in-memory relation.
      responses:
        '200':
          description: Cleaning completed successfully.
          schema:
            oneOf:
              - type: object
                description: DuckDB relation handle (opaque).
              - type: 'null'
        '400':
          description: Invalid input path or I/O error.
      examples:
        request:
          input_path: "./data/ratings.csv"
          output_path: "./data/ratings_clean.parquet"
        response:
          value: null
    """
    con = duckdb.connect()

    con.execute("SET memory_limit = '6GB';")
    con.execute("SET temp_directory = './tmp_duckdb';")

    rel = con.from_csv_auto(input_path, header=True)
    rel_pulita = rel.filter("username IS NOT NULL") \
        .distinct() \
        .project("""
            username,
            anime_id,
            status,
            score,
            CAST(is_rewatching AS TINYINT) as is_rewatching,
            num_watched_episodes
        """)

    if output_path:
        rel_pulita.write_parquet(output_path, compression='snappy')
        print(f"Pulizia completata: {output_path}")
        con.close()
        return None
    else:
        return rel_pulita
