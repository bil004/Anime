import duckdb


def clean_ratings_table(input_path: str, output_path: str = None):
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
