import pandas as pd

keywords_corona = ['coronavirus', 'COVID-19', 'SARS-CoV-2', 'pandemic', 'quarantine']
class RelevantCoronaDataBase:
    @staticmethod
    def relevant_to_corona(database):
        # Initialize an empty list to store relevant publications
        relevant_database = []

        # Iterate through publications and identify relevant ones
        for index, row in database.iterrows():
            abstract = row['Abstract']
            # Check if the abstract is a valid string and contains any of the keywords
            if isinstance(abstract, str) and any(keyword.lower() in abstract.lower() for keyword in keywords_corona):
                # Add the publication to the list of relevant publications
                relevant_database.append(row)

        # Create a new DataFrame containing relevant publications
        relevant_df = pd.DataFrame(relevant_database)
        print('\nHere is the relevant_df:\n', relevant_df)
        num_rows = len(relevant_df)
        print("Number of rows:", num_rows)
        # Return the relevant DataFrame
        return relevant_df
