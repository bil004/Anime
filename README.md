# Anime Data - README

## Scopo
Fornire a fan e giornalisti accesso ai dati sugli anime tramite notebook Jupyter che eseguono pulizia, analisi e visualizzazioni dei dataset disponibili.

## Struttura del progetto
- `data/` — file CSV originali e risultati del preprocessing (es. `characters.csv`, `ratings.csv`, `profiles.csv`, ...)
- `solution/cleaning/` — notebook di pulizia:
  - `1_Dataset_Cleaning.ipynb`
  - `2_Dataset_Cleaning.ipynb`
  - `3_Dataset_Cleaning.ipynb`
- `models/` — eventuali modelli salvati
- `report/` — output di analisi e figure per il report
- `requirements.txt` — dipendenze Python

## Requisiti
- Python 3.8+ (Windows)
- Installare dipendenze:


## Esecuzione dei notebook
1. Aprire il progetto in PyCharm o avviare `jupyter notebook` / `jupyter lab`.
2. Eseguire i notebook nell'ordine numerico:
   - `solution/cleaning/1_Dataset_Cleaning.ipynb` (caricamento e pulizia iniziale)
   - `solution/cleaning/2_Dataset_Cleaning.ipynb` (integrazione e normalizzazione)
   - `solution/cleaning/3_Dataset_Cleaning.ipynb` (controlli finali e salvataggio)
3. I notebook generano dataset puliti e visualizzazioni salvabili nelle cartelle `data/`, `report/` e `models/`.

## Output atteso
- Dataset puliti e coerenti per analisi successive
- Visualizzazioni e statistiche riassuntive utilizzabili in articoli o report
- (Opzionale) modelli predittivi salvati in `models/`

## Note
- Modificare i percorsi dei file nei notebook se si esegue da cartelle diverse.
- Usare PyCharm 2025.2.5 o un ambiente Jupyter compatibile su Windows per eseguire i file `.ipynb`.
