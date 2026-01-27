import duckdb


def process_heavy_data(input_path: str, output_path: str = None):
    import duckdb

    # Crea una connessione esplicita per settare i limiti
    con = duckdb.connect()

    # LIMITA LA RAM: ad esempio a 4GB o 6GB per lasciare respiro al sistema
    con.execute("SET memory_limit = '6GB';")
    # Usa una cartella temporanea su disco per le operazioni pesanti (come il distinct)
    con.execute("SET temp_directory = './tmp_duckdb';")

    # 1. Caricamento Lazy
    rel = con.from_csv_auto(input_path, header=True)

    # 2. Ottimizzazione: Il .distinct() è davvero necessario?
    # Spesso i dataset MyAnimeList sono già unici per coppia username-anime_id.
    # Se devi proprio farlo, DuckDB ora userà il disco (temp_directory) invece di freezare la RAM.

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

    # 3. Output
    if output_path:
        rel_pulita.write_parquet(output_path, compression='snappy')
        print(f"Pulizia completata: {output_path}")
        con.close()
        return None
    else:
        # Ritorna la relazione DuckDB per mostrarla nel notebook
        return rel_pulita


def process_file(input_path: str):
    """Esempio per il file profiles basato sul tuo notebook"""
    rel = duckdb.read_csv(input_path)

    # Replica di: dropna(subset=['username']) e drop_duplicates()
    return rel.filter("username IS NOT NULL").distinct()