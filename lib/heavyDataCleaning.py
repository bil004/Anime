import duckdb

"""
Module: heavyDataCleaning
High-performance data loading and cleaning routines for large datasets.

Leverages the in-memory DuckDB analytical engine to transform and deduplicate
large CSV files, saving cleaned outputs to Parquet format optimized for Data Analysis.
"""


def clean_ratings_table(input_path: str, output_path: str = None):
    """
    Cleans and casts data types for the user ratings table.

    Loads a CSV file via DuckDB, drops records missing a username, removes duplicates,
    selects relevant columns, and downcasts data types to optimize memory usage.

    Parameters:
        input_path (str): Filepath to the source CSV file.
        output_path (str, optional): Target destination filepath for writing a compressed Parquet file (Snappy).
                                     If omitted, returns an in-memory DuckDB relation.

    Returns:
        duckdb.DuckDBPyRelation | None: DuckDB relation handle if `output_path` is None, otherwise None.
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