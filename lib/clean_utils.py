import ast
import pandas as pd


def clean_studio_format(entry):
    """
    Pulisce il formato dei dati 'studios' convertendo stringhe
    come "['Studio Name']" nel nome dello studio pulito.
    """
    try:
        # Se è null o non è una stringa, lo ignoriamo
        if pd.isna(entry) or not isinstance(entry, str):
            return None

        # Converte la stringa "['Nome']" in una lista vera ['Nome']
        # ast.literal_eval è sicuro per valutare strutture dati da stringhe
        lista_studi = ast.literal_eval(entry)

        # Se la conversione ha successo ed è una lista non vuota
        if isinstance(lista_studi, list) and len(lista_studi) > 0:
            return lista_studi[0]  # Restituisce il primo elemento

        return None
    except (ValueError, SyntaxError):
        # Se c'è un errore di parsing, ritorna None
        return None