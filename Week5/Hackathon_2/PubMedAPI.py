from Bio import Entrez
from io import BytesIO
import pandas as pd


class PubMedAPI:
    def __init__(self, email):
        self.email = email
        Entrez.email = email

    def retrieve_recent_publications(self, subject, years, max_results_per_year):
        """
        Retrieves recent publications from PubMed based on the specified subject and timeframe.
        Limits the search to a certain number of years and maximum number of results per year.

        Parameters:
        - subject: The subject/topic to search for.
        - years: Number of years to search within.
        - max_results_per_year: Maximum number of publications to retrieve per year.

        Returns:
        - List of article IDs for the retrieved publications.
        """
        try:
            current_year = pd.Timestamp.now().year
            start_year = current_year - years

            # Initialize list to store article IDs
            articles = []

            # Iterate over each year
            for year in range(start_year+1, current_year + 1):
                # Construct the search query for the current year
                search_term = f'"{subject}"[Title/Abstract] AND ("{year}/01/01"[DateRevised] : "{year}/12/31"[DateRevised])'

                # Perform the search and retrieve article IDs
                handle = Entrez.esearch(db="pubmed", term=search_term, retmax=max_results_per_year)
                record = Entrez.read(handle)
                handle.close()
                article_ids = record['IdList']

                # Add a random sample of article IDs to the list
                #   articles.extend(random.sample(article_ids, min(len(article_ids), max_results_per_year)))
                articles.extend(article_ids)

            return articles
        except Exception as e:
            print(f"Error occurred while retrieving publications: {e}")
            return []

    def retrieve_article_details(self, article_ids):
        articles_info = []
        try:
            for article_id in article_ids:
                handle = Entrez.efetch(db="pubmed", id=article_id, rettype="medline", retmode="xml")
                xml_data = handle.read()
                handle.close()

                # Parse XML data
                handle = BytesIO(xml_data)
                record = Entrez.read(handle)

                if 'PubmedArticle' in record and record['PubmedArticle']:
                    authors = record['PubmedArticle'][0]['MedlineCitation']['Article'].get('AuthorList', [])
                    authors_info = []
                    for author in authors:
                        if 'LastName' in author and 'Initials' in author:
                            author_info = author['LastName'] + ' ' + author['Initials']
                            authors_info.append(author_info)

                    article_info = {
                        'PMID': article_id,
                        'Title': record['PubmedArticle'][0]['MedlineCitation']['Article'].get('ArticleTitle', ''),
                        'Authors': ', '.join(authors_info),
                        'Journal': record['PubmedArticle'][0]['MedlineCitation']['Article']['Journal'].get('Title', ''),
                        'CountryOfPublication': record['PubmedArticle'][0]['MedlineCitation']['MedlineJournalInfo'].get(
                            'Country', ''),
                        'PublicationDate': record['PubmedArticle'][0]['MedlineCitation'].get("DateRevised", {}).get(
                            'Year', ''),
                        'Abstract': record['PubmedArticle'][0]['MedlineCitation']['Article'].get('Abstract', {}).get(
                            'AbstractText', [''])[0],
                    }
                    articles_info.append(article_info)
        except Exception as e:
            print(f"Error occurred while retrieving article details: {e}")
        return articles_info

    def retrieve_dataframe(self, articles_info):
        database = pd.DataFrame(articles_info)
        return database
