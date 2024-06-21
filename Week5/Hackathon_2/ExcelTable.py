import os
from PubMedAPI import PubMedAPI
from KeywordGenerator import generate_keywords
from KeywordExtractor import extract_keywords
import pandas as pd

class DataBaseFromAPIs:
    @staticmethod
    def database_from_apis(excel_file_name, excel_sheet_name):
        if not ExcelTable.excel_database_exists(excel_file_name):
            email = "your@gmail.com"

            # Assuming this part of the code allows the user to input subject, years, and max_results
            subject = input("Enter subject: ")
            years = int(input("Enter number of years: "))
            max_results_per_year = int(input("Enter max number of results per year: "))

            # Create PubMedAPI instance
            api = PubMedAPI(email)

            # Retrieve article IDs
            article_ids = api.retrieve_recent_publications(subject, years, max_results_per_year)

            # Retrieve article details
            articles_info = api.retrieve_article_details(article_ids)

            # Create DataFrame
            database = api.retrieve_dataframe(articles_info)

            # Generate keywords
            keyphrase_dict = generate_keywords(database)

            # Add keyphrase_dict as a new column to the database DataFrame
            keyphrase_series = pd.Series(keyphrase_dict)
            database['KeyPhrases'] = keyphrase_series

            # Extract keywords using NLTK
            database['KeywordsNLTK'] = extract_keywords(database)

            print(database.head())  # Print the first few rows of the DataFrame

            # Create ExcelDatabase
            ExcelTable.database_to_excel(database, excel_file_name, excel_sheet_name)
            print(f"DataFrame has been saved to '{excel_file_name}' in sheet '{excel_sheet_name}'.")
        else:
            database = ExcelTable.database_from_excel(excel_file_name, excel_sheet_name)
            print(database.head())



class ExcelTable:
    @staticmethod
    def database_to_excel(database, excel_file_name, excel_sheet_name):
        database.to_excel(excel_file_name, sheet_name=excel_sheet_name, index=False)
    @staticmethod
    def excel_database_exists(excel_file_name):
        return os.path.isfile(excel_file_name)

    @staticmethod
    def database_from_excel(excel_file_name, excel_sheet_name):
        database = pd.read_excel(excel_file_name, sheet_name=excel_sheet_name)
        return database
