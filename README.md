# HCI - Anime Data Analysis Project

## Project Goal

The main goal of this project is to provide a comprehensive dataset for anime enthusiasts and journalists. Through a series of Jupyter Notebooks, we will clean, analyze, and visualize data related to anime, characters, and voice actors to uncover insights and trends.

## Project Structure

The project is organized into the following directories:

- `data/`: Contains the original and raw CSV files.
- `cleaned_data/`: Contains the cleaned and pre-processed datasets, ready for analysis.
- `solution/`: Contains the Jupyter Notebooks for the different phases of the project.
  - `cleaning/`: Notebooks dedicated to data cleaning and preparation.
  - `analysis/`: Notebooks for exploratory data analysis.
  - `visualisation/`: Notebooks for data visualization.
- `models/`: Directory for any machine learning models.
- `report/`: Directory for project reports or summaries.
- `README.md`: This file, which provides an overview of the project.

## Data Cleaning

The data cleaning process is detailed in the notebooks inside `solution/cleaning/`. The process for each dataset includes:
1.  Loading data from a PostgreSQL database.
2.  Inspecting the data structure and initial values.
3.  Handling missing (`null`) values.
4.  Identifying and removing duplicate entries.
5.  Correcting data types and optimizing memory usage.
6.  Saving the cleaned data in the `cleaned_data/` directory (`ratings_cleaned.parquet`).

The cleaning is divided into multiple notebooks:
- `1_Dataset_Cleaning.ipynb`: Cleans `favs`, `character_anime_works`, `character_nicknames`, and `characters`.
- `2_Dataset_Cleaning.ipynb`: Cleans `details`, `person_alternate_names`, `person_anime_works`, and `person_details`.
- `3_Dataset_Cleaning.ipynb`: Cleans `person_voice_works`, `profiles`, `recommendations`, and `stats`.
- `4_Dataset_Cleaning.ipynb`: Cleans `ratings`.

## How to Run

1.  Make sure you have Python and Jupyter Notebook installed.
2.  Ensure you have a database connection via PostgreSQL (mandatory) through the `.env` file.
3.  Install the required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```
4.  Open the Jupyter Notebooks in the `solution/` directory to explore the project. Start with the `cleaning` notebooks, then move on to `analysis` and `visualisation`.
