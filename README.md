# HCI - Progetto di Analisi Dati sugli Anime

## Obiettivo del Progetto

L'obiettivo principale di questo progetto è fornire un dataset completo per appassionati di anime e giornalisti. Attraverso una serie di Jupyter Notebook, puliremo, analizzeremo e visualizzeremo i dati relativi ad anime, personaggi e doppiatori per scoprire approfondimenti e tendenze.

## Struttura del Progetto

Il progetto è organizzato nelle seguenti directory:

- `data/`: Contiene i file CSV originali e grezzi.
- `cleaned_data/`: Contiene i dataset puliti e pre-elaborati, pronti per l'analisi.
- `solution/`: Contiene i Jupyter Notebook per le diverse fasi del progetto.
  - `cleaning/`: Notebook dedicati alla pulizia e preparazione dei dati.
  - `analysis/`: Notebook per l'analisi esplorativa dei dati.
  - `visualisation/`: Notebook per la visualizzazione dei dati.
- `models/`: Directory per eventuali modelli di machine learning.
- `report/`: Directory per report o riassunti del progetto.
- `README.md`: Questo file, che fornisce una panoramica del progetto.

## Pulizia dei Dati

Il processo di pulizia dei dati è dettagliato nei notebook all'interno di `solution/cleaning/`. Il processo per ogni dataset include:
1.  Caricamento dei dati da un database PostGres.
2.  Ispezione della struttura dei dati e dei valori iniziali.
3.  Gestione dei valori mancanti (`null`).
4.  Identificazione e rimozione delle voci duplicate.
5.  Correzione dei tipi di dati e ottimizzazione dell'uso della memoria.
6.  Salvataggio dei dati puliti nella directory `cleaned_data/` (`ratings_cleaned.parquet`).

La pulizia è suddivisa in più notebook:
- `1_Dataset_Cleaning.ipynb`: Pulisce `favs`, `character_anime_works`, `character_nicknames` e `characters`.
- `2_Dataset_Cleaning.ipynb`: Pulisce `details`, `person_alternate_names`, `person_anime_works` e `person_details`.
- `3_Dataset_Cleaning.ipynb`: Pulisce `person_voice_works`, `profiles`, `recommendations` e `stats`.
- `4_Dataset_Cleaning.ipynb`: Pulisce `ratings`.

## Come Eseguire

1.  Assicurati di avere installato Python e Jupyter Notebook.
2.  Assicurati di avere la connessione del database tramite postgres (obbligatorio) tramite il file `.env`.
2.  Installa le librerie richieste eseguendo:
    ```bash
    pip install -r requirements.txt
    ```
3.  Apri i Jupyter Notebook nella directory `solution/` per esplorare il progetto. Inizia con i notebook di `cleaning`, poi passa ad `analysis` e `visualisation`.
