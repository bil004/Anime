# Anime Data Analysis Project

## Project Goal

The main goal of this project is to provide a comprehensive dataset for anime fans and journalists. Through a series of Jupyter Notebooks, we will clean, analyze, and visualize data related to anime, characters, and voice actors to uncover insights and trends.

## Project Structure

The project is organized into the following directories:

- `data/`: Contains the original, raw CSV files.
- `cleaned_data/`: Contains the cleaned and preprocessed datasets, ready for analysis.
- `solution/`: Contains the Jupyter Notebooks for the different project phases.
  - `cleaning/`: Notebooks dedicated to data cleaning and preparation.
  - `analysis/`: Notebooks for exploratory data analysis.
  - `visualisation/`: Notebooks for data visualization.
- `models/`: Directory for any machine learning models.
- `report/`: Directory for project reports or summaries.
- `README.md`: This file, providing an overview of the project.

## Data Cleaning

The data cleaning process is detailed in the notebooks inside `solution/cleaning/`. The process for each dataset includes:
1.  Loading the data from CSV files.
2.  Inspecting the data structure and initial values.
3.  Handling missing (`null`) values.
4.  Identifying and removing duplicate entries.
5.  Correcting data types and optimizing memory usage.
6.  Saving the cleaned data into the `cleaned_data/` directory.

The cleaning is split across multiple notebooks:
- `1_Dataset_Cleaning.ipynb`: Cleans `favs`, `character_anime_works`, `character_nicknames`, and `characters`.
- `2_Dataset_Cleaning.ipynb`: Cleans `details`, `person_alternate_names`, `person_anime_works`, and `person_details`.
- `3_Dataset_Cleaning.ipynb`: Cleans `person_voice_works`, `profiles`, `ratings`, `recommendations`, and `stats`.

## How to Run

1.  Make sure you have Python and Jupyter Notebook installed.
2.  Install the required libraries by running:
    ```bash
    pip install -r requirements.txt
    ```
3.  Open the Jupyter Notebooks in the `solution/` directory to explore the project. Start with the `cleaning` notebooks, then move to `analysis` and `visualisation`.

