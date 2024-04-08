from main import excel_file_name, excel_sheet_name
from VisualizerClass import VisualizerClass
from ExcelTable import ExcelTable
from RelevantToCorona import RelevantCoronaDataBase
from KeywordExtractor import extract_keywords
import pandas as pd

if not ExcelTable.excel_database_exists(excel_file_name):
    print ("Excel database does not exist, please run main program to create an Excel file")
else:
    database = ExcelTable.database_from_excel(excel_file_name, excel_sheet_name)
    # Clean the data from empty rows
    database.dropna(inplace=True)
    # Change data type
    database['PublicationDate'] = pd.to_datetime(database['PublicationDate'], format='%Y').dt.year
    # Assuming 'KeyPhrases' is the column containing the key phrases
    database['KeyPhrases'] = database['KeyPhrases'].apply(lambda x: ' '.join(word.lower() for word in x.split()))
    key_phrases = dict(zip(database.index, database['KeyPhrases']))
    # Extract the phrases from the dictionary values and split them into individual words
    key_words_OpenAI = [word[:-1].lower() if word.endswith('s') and len(word) > 1 else word.lower() for phrase
                      in key_phrases.values() for word in phrase.split()]
    # Call the relevant_to_corona method to get the relevant DataFrame
    relevant_df = RelevantCoronaDataBase.relevant_to_corona(database)
    keywords_list = dict(zip(database.index, database['KeywordsNLTK']))
    # Extract the phrases from the dictionary values and split them into individual words
    key_words_NLTK = [word[:-1].lower() if word.endswith('s') and len(word) > 1 else word.lower() for phrase
                      in keywords_list.values() for word in phrase.split()]

    # Load your dataset
    data_vaccines = pd.read_csv('covid-vaccine-doses-by-manufacturer.csv')
    # Convert the 'Day' column to datetime
    data_vaccines['Day'] = pd.to_datetime(data_vaccines['Day'])
    # Filter the data for doses administered for all vaccines
    vaccines_data = data_vaccines[['Pfizer/BioNTech', 'Moderna', 'Oxford/AstraZeneca', 'Johnson&Johnson',
                                   'Sputnik V', 'Sinovac', 'Novavax', 'Covaxin', 'Sanofi/GSK', 'Valneva']]

    # Group the filtered data by year and sum the doses administered for each vaccine
    yearly_doses = vaccines_data.groupby(data_vaccines['Day'].dt.year).sum()

    VisualizerClass.word_cloud(key_phrases)
    VisualizerClass.keyword_frequency(key_words_OpenAI)
    VisualizerClass.keyword_nltk_frequency(key_words_NLTK)
    VisualizerClass.venn_diagram(key_words_OpenAI, key_words_NLTK)
    VisualizerClass.relevant_to_corona(database, relevant_df)
    VisualizerClass.pie_for_max_year(database, relevant_df)
    VisualizerClass.country_publication_bins(database, relevant_df)
    VisualizerClass.total_articles(database, relevant_df)
    VisualizerClass.count_articles(database, relevant_df)
    VisualizerClass.visualize_relative_counts(database, relevant_df)
    VisualizerClass.vaccines_heatmap(yearly_doses)
    VisualizerClass.vaccines_plot(yearly_doses)









