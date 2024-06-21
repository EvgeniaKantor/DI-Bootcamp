from matplotlib import pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import seaborn as sns
from matplotlib_venn import venn2
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
class VisualizerClass:
    @staticmethod
    def word_cloud(key_phrases):
        # Concatenate all key phrases into a single string
        text = ' '.join(key_phrases.values())
        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
        # Display word cloud
        plt.figure(figsize=(10, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

    @staticmethod
    def keyword_frequency(key_words_OpenAI):
        # Count the frequency of each keyword
        keyword_counts = Counter(key_words_OpenAI)
        # Filter out keywords with a frequency less than or equal to 2
        filtered_keyword_counts = {word: count for word, count in keyword_counts.items() if count > 2}
        # Sort keywords by frequency in descending order
        sorted_keywords = dict(sorted(filtered_keyword_counts.items(), key=lambda x: x[1], reverse=True))
        # Plot the frequency of occurrence of keywords
        plt.figure(figsize=(12, 6))
        plt.bar(sorted_keywords.keys(), sorted_keywords.values(), color='skyblue')
        plt.title('Frequency of Occurrence of Keywords_OpenAI (Frequency > 2)')
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def keyword_nltk_frequency(key_words_NLTK):
        # Count the frequency of each keyword
        keyword_counts = Counter(key_words_NLTK)
        # Filter out keywords with a frequency less than or equal to 2
        filtered_keyword_counts = {word: count for word, count in keyword_counts.items() if count > 2}
        # Sort keywords by frequency in descending order
        sorted_keywords = dict(sorted(filtered_keyword_counts.items(), key=lambda x: x[1], reverse=True))
        # Plot the frequency of occurrence of keywords
        plt.figure(figsize=(12, 6))
        plt.bar(sorted_keywords.keys(), sorted_keywords.values(), color='skyblue')
        plt.title('Frequency of Occurrence of Keywords_NLTK (Frequency > 2)')
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def venn_diagram(key_words_OpenAI, key_words_NLTK):
        keyword_counts_OpenAI = Counter(key_words_OpenAI)
        # Sort keywords by frequency in descending order
        sorted_keywords_OpenAI = dict(sorted(keyword_counts_OpenAI.items(), key=lambda x: x[1], reverse=True))
        # Count the frequency of occurrence of each keyword
        keyword_counts_NLTK = Counter(key_words_NLTK)
        # Sort keywords by frequency in descending order
        sorted_keywords_NLTK = dict(sorted(keyword_counts_NLTK.items(), key=lambda x: x[1], reverse=True))

        # Calculate the intersection of keywords
        intersection = set(sorted_keywords_OpenAI.keys()).intersection(set(sorted_keywords_NLTK.keys()))

        # Calculate the sizes of the sets and the intersection
        sizes = [len(set(sorted_keywords_OpenAI.keys())), len(set(sorted_keywords_NLTK.keys())), len(intersection)]

        # Create a Venn diagram
        plt.figure(figsize=(8, 8))
        venn2(subsets=sizes, set_labels=('Keywords_OpenAI', 'Keywords_NLTK'), set_colors=('skyblue', 'blue'))
        plt.title('Overlap of Keywords between OpenAI and NLTK')
        plt.show()
    @staticmethod
    def relevant_to_corona(database, relevant_df):
        # Calculate the count of relevant articles
        relevant_articles_count = len(relevant_df)
        # Calculate the total number of articles
        total_articles = len(database)
        # Create a pie plot
        labels = ['Related to Topic', 'Not Related to Topic']
        sizes = [relevant_articles_count, total_articles - relevant_articles_count]
        colors = ['skyblue', 'beige']
        explode = (0.1, 0)  # explode the 1st slice (Related to Topic)
        plt.figure(figsize=(7, 7))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('Proportion of Articles Related to the Topic "Coronavirus"')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()

    @staticmethod
    def pie_for_max_year(database, relevant_df):
        # Group the data by publication year and count the number of publications for each year
        publication_counts = relevant_df['PublicationDate'].value_counts()
        # Find the year with the highest number of publications
        year_with_most_publications = publication_counts.idxmax()
        # Filter the relevant DataFrame to include only articles from the year with the most publications
        relevant_df_most_publications = relevant_df[
            relevant_df['PublicationDate'] == year_with_most_publications]
        # Calculate the count of relevant articles for the year with the most publications
        relevant_articles_count_most_publications = len(relevant_df_most_publications)
        # Calculate the total number of articles for the year with the most publications
        total_articles_most_publications = len(
            database[database['PublicationDate'] == year_with_most_publications])
        # Create a pie plot
        labels = ['Publication Related to Corona', 'All Publication']
        sizes = [relevant_articles_count_most_publications,
                 total_articles_most_publications - relevant_articles_count_most_publications]
        colors = ['skyblue', 'beige']
        explode = (0.1, 0)  # explode the 1st slice (Related to Topic)
        plt.figure(figsize=(7, 7))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title(f'Proportion of Articles Related to the Topic "Coronavirus" in {year_with_most_publications}')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        plt.show()
    @staticmethod
    def country_publication_bins(database, relevant_df):
        # Count the frequency of publications by country for all publications
        all_country_counts = database['CountryOfPublication'].value_counts()
        # Count the frequency of publications by country for coronavirus-related publications
        corona_country_counts = relevant_df['CountryOfPublication'].value_counts()
        # Create a figure and axes
        fig, ax = plt.subplots(figsize=(22, 6))
        # Plot the frequency of publications by country for all publications
        ax.bar(all_country_counts.index, all_country_counts.values, color='beige', label='All Publications')
        # Plot the frequency of publications by country for coronavirus-related publications
        ax.bar(corona_country_counts.index, corona_country_counts.values, color='skyblue', label='Coronavirus-related Publications')
        # Set labels and title
        ax.set_xlabel('Country')
        ax.set_ylabel('Frequency')
        ax.set_title('Publication Frequency by Country')
        ax.legend()
        # Display the plot
        plt.show()

    @staticmethod
    def total_articles(database, relevant_df):
        # Count the number of articles published each year
        corona_publication_count_per_year = relevant_df['PublicationDate'].value_counts().sort_index()
        all_publication_count_per_year = database['PublicationDate'].value_counts().sort_index()

        # Plot the number of articles per year using Seaborn
        plt.figure(figsize=(10, 6))
        plt.plot(all_publication_count_per_year.index, all_publication_count_per_year.values, color='beige',
                 label='All Publications', linewidth=5)
        plt.plot(corona_publication_count_per_year.index, corona_publication_count_per_year.values, color='skyblue',
                 label='Coronavirus Publications', linewidth=5)
        plt.title('Number of Printed Articles in DataBase')
        plt.xlabel('Year')
        plt.ylabel('Number of Articles')
        plt.grid(True)
        plt.xticks(fontsize=8)
        plt.tight_layout()
        plt.legend()
        plt.show()

    @staticmethod
    def count_articles(database, relevant_df):
        # Get unique publication years for all articles and corona-relevant articles
        all_publication_years = database['PublicationDate']
        corona_publication_years = relevant_df['PublicationDate']

        # Count the number of publications for each year for all articles and corona-relevant articles
        all_publication_counts = all_publication_years.value_counts().sort_index()
        corona_publication_counts = corona_publication_years.value_counts().sort_index()

        # Plotting
        plt.figure(figsize=(10, 6))
        sns.histplot(data=all_publication_years, bins=len(all_publication_counts), kde=True, color='beige', label='All Articles')
        sns.histplot(data=corona_publication_years, bins=len(corona_publication_counts), kde=True, color='skyblue',
                     label='Corona Relevant Articles')
        plt.title('Number of Publications Each Year')
        plt.xlabel('Year')
        plt.ylabel('Number of Publications')
        plt.legend()
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_relative_counts(database, relevant_df):
        # Get counts for each year
        corona_publication_counts = relevant_df['PublicationDate'].value_counts().sort_index()
        all_publication_counts = database['PublicationDate'].value_counts().sort_index()
        # Calculate relative percentage
        relative_counts = (corona_publication_counts / all_publication_counts) * 100
        # Plot the relative percentages
        plt.figure(figsize=(10, 6))
        plt.plot(relative_counts.index, relative_counts.values, color='skyblue', marker='o', linewidth=5)
        plt.title('Relative Number of Coronavirus Publications Over Time')
        plt.xlabel('Year')
        plt.ylabel('Percentage of Coronavirus Publications from All Publications (%)')
        plt.grid(True)
        plt.xticks(relative_counts.index)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def vaccines_heatmap(yearly_doses):
        plt.figure(figsize=(12, 8))
        sns.heatmap(yearly_doses.T, cmap='YlGnBu', annot=True, fmt=',.0f')
        plt.title('Doses Administered for Each Vaccine Over Time')
        plt.xlabel('Year')
        plt.ylabel('Vaccine')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def vaccines_plot(yearly_doses):
        # Define custom colors
        colors = ['#FFFF00', '#87CEEB', '#90EE90']
        # Plotting the overall graph
        plt.figure(figsize=(10, 6))
        # Plotting Pfizer/BioNTech doses
        plt.plot(yearly_doses.index, yearly_doses['Pfizer/BioNTech'], marker='o', linestyle='-', color=colors[1],
                 label='Pfizer/BioNTech, Germany')
        # Plotting Moderna doses
        plt.plot(yearly_doses.index, yearly_doses['Moderna'], marker='o', linestyle='-', color=colors[2],
                 label='Moderna, United States')
        # Plotting Oxford/AstraZeneca doses
        plt.plot(yearly_doses.index, yearly_doses['Oxford/AstraZeneca'], marker='o', linestyle='-', color=colors[0],
                 label='Oxford/AstraZeneca, England and Swedish')
        # Adding labels and title
        plt.xlabel('Year')
        plt.ylabel('Total Doses Administered')
        plt.title('Vaccines Administered by Year')
        plt.legend()
        # Displaying the plot
        plt.grid(True)
        plt.tight_layout()
        plt.show()



