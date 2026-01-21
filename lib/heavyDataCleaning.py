import duckdb


def process_heavy_data(input_path: str, output_path: str = None):
    """
    Carica un file ratings CSV di grandi dimensioni (>4GB), pulisce i dati
    usando la Relational API di DuckDB e (opzionalmente) salva in Parquet.
    """

    # 1. Lazy Loading: DuckDB "guarda" il file ma non lo carica in RAM
    # scan_csv è simile a read_csv ma ottimizzato per dataset grandi
    rel = duckdb.read_csv(input_path, header=True, auto_detect=True)

    # 2. Applicazione delle trasformazioni (Metodo B - Relational API)
    # Replica di: ratings.dropna(subset=['username']) e drop_duplicates()

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

    # Nota: .project serve a selezionare le colonne e fare cast al volo.
    # CAST(is_rewatching AS TINYINT) è l'equivalente SQL di .astype('int8')

    # 3. Output
    if output_path:
        # Scrive su disco in formato Parquet (molto più compresso e veloce del CSV)
        rel_pulita.write_parquet(output_path, compression='snappy')
        print(f"Pulizia completata. File salvato in: {output_path}")
        return None
    else:
        # Ritorna la relazione DuckDB per mostrarla nel notebook
        return rel_pulita


def process_file(input_path: str):
    """Esempio per il file profiles basato sul tuo notebook"""
    rel = duckdb.read_csv(input_path)

    # Replica di: dropna(subset=['username']) e drop_duplicates()
    return rel.filter("username IS NOT NULL").distinct()