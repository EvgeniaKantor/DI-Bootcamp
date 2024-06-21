
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import plotly.io as pio
import numpy as np
import plotly.express as px
from matplotlib_venn import venn3

from textblob import TextBlob
from textblob.taggers import PatternTagger
# Specify the location of the Plotly JavaScript library
nltk.download('vader_lexicon')

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Initialize NLTK resources
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('russian'))

class TextAnalyse:
    @staticmethod
    def create_sentiments(df_feedback):

        # Filter rows based on the pattern in 'Review_Text' column and star count == 5
        feedbacks_without_no_info = df_feedback[df_feedback['Review_Text'] != 'No info'].copy()

        # Extract text values for sentiment analysis
        feedback_texts = feedbacks_without_no_info['Review_Text'].values

        sid = SentimentIntensityAnalyzer()
        sentiments_sid = []
        for text in feedback_texts:
            sentiment_scores = sid.polarity_scores(text)
            # Classify the sentiment based on the compound score
            if sentiment_scores['compound'] >= 0.05:
                sentiments_sid.append('Positive')
            elif sentiment_scores['compound'] <= -0.05:
                sentiments_sid.append('Negative')
            else:
                sentiments_sid.append('Neutral')

        # Add sentiment column to the DataFrame
        feedbacks_without_no_info['Sentiment_sid'] = sentiments_sid

        ###############################################################
        # Analyze sentiment for each feedback text
        sentiments_TextBlob = []
        for text in feedback_texts:
            # Create a TextBlob object with Pattern tagger for Russian
            blob = TextBlob(text, pos_tagger=PatternTagger())

            # Perform sentiment analysis
            sentiment = blob.sentiment.polarity

            # Map sentiment scores to categories
            if sentiment > 0:
                sentiments_TextBlob.append('Positive')
            elif sentiment < 0:
                sentiments_TextBlob.append('Negative')
            else:
                sentiments_TextBlob.append('Neutral')

        # Add sentiment column to the DataFrame
        feedbacks_without_no_info['Sentiment_TextBlob'] = sentiments_TextBlob

        # Display the filtered DataFrame
        # print(feedbacks_without_no_info[['Date', 'Review_Text', 'Sentiment_sid', 'Sentiment_TextBlob']])
        # Count the occurrences of each sentiment category for both analyzers
        sentiment_counts_sid = feedbacks_without_no_info['Sentiment_sid'].value_counts()
        sentiment_counts_TextBlob = feedbacks_without_no_info['Sentiment_TextBlob'].value_counts()

        # Pie chart for SentimentIntensityAnalyzer
        plt.figure(figsize=(8, 6))
        colors = ['lightgreen', 'lightblue', 'lightcoral']
        plt.pie(sentiment_counts_sid, labels=sentiment_counts_sid.index, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Sentiment Categories (SentimentIntensityAnalyzer)')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('sentiment_sid_pie_chart.png', format='png', dpi=300)
        plt.show()
        plt.close()

        # Pie chart for TextBlob
        plt.figure(figsize=(8, 6))
        # Define colors for each category
        colors = ['lightgreen', 'lightblue', 'lightcoral']
        plt.pie(sentiment_counts_TextBlob, labels=sentiment_counts_TextBlob.index, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Sentiment Categories (TextBlob)')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.savefig('sentiment_textblob_pie_chart.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def my_sentiment_analysis(df_feedback):
        # Define the pattern
        pattern = r'\b(?:но|однако)\b'

        # Filter rows based on the pattern in 'Review_Text' column and star count == 5
        feedbacks_with_no = df_feedback[
            df_feedback['Review_Text'].str.contains(pattern) & (df_feedback['Star_Count'] == 5)]

        # Initialize a new column 'Sentiment' with default value 'Positive'
        df_feedback['My_Sentiment'] = 'Positive'

        # Update the 'Sentiment' column based on star count
        df_feedback.loc[df_feedback['Star_Count'] == 4, 'My_Sentiment'] = 'Neutral'
        df_feedback.loc[df_feedback['Star_Count'] < 4, 'My_Sentiment'] = 'Negative'

        # Update 'Sentiment' column for rows containing 'но' in 'Review_Text'
        df_feedback.loc[feedbacks_with_no.index, 'My_Sentiment'] = 'Neutral'

        # Count the number of feedbacks for each sentiment
        sentiment_counts = df_feedback['My_Sentiment'].value_counts()

        # Print the sentiment counts
        print(sentiment_counts)

        # Define labels and sizes for the pie chart
        labels = sentiment_counts.index
        sizes = sentiment_counts.values

        # Define colors for each category
        colors = ['lightgreen', 'lightblue', 'lightcoral']

        # Create the pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Distribution of Sentiments')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Show the pie chart
        plt.savefig('sentiment_my_pie_chart.png', format='png', dpi=300)
        plt.show()
        plt.close()


    @staticmethod
    def print_sentences_after_no(df_feedback):
        # Define the pattern
        pattern = r'\b(?:но|однако)\b'

        # Filter rows based on the pattern in 'Review_Text' column and star count == 5
        feedbacks_with_no = df_feedback[
            df_feedback['Review_Text'].str.contains(pattern) & (df_feedback['Star_Count'] == 5)]

        # Tokenize the text
        nltk.download('punkt')
        nltk.download('stopwords')
        stop_words = set(stopwords.words('russian'))

        keywords_list_5 = []  # List to store keywords extracted from all titles
        all_feedback_text_5 = ''  # Initialize the variable to store all feedback texts

        for index, row in feedbacks_with_no.iterrows():
            text = row['Review_Text']
            tokens = word_tokenize(text)
            # Find the index of 'но' in tokens
            try:
                no_index = tokens.index('но')
            except ValueError:
                continue  # Skip if 'но' is not found
            # Print all words after 'но'
            text = " ".join(tokens[no_index + 1:])
            print(text)

            # Append text to the list of all feedback texts
            all_feedback_text_5 += text + ' '

            # Tokenize the combined text
        tokens = word_tokenize(all_feedback_text_5)

        # Remove stopwords
        filtered_tokens = [word.lower() for word in tokens if word.lower() not in stop_words and word.isalpha()]

        # Convert filtered tokens into documents
        documents = [' '.join(filtered_tokens)]

        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Get feature names (i.e., words)
        feature_names = vectorizer.get_feature_names_out()

        # Get TF-IDF scores
        tfidf_scores = tfidf_matrix.toarray()

        # Get top keywords with highest TF-IDF scores
        top_keywords_indices = tfidf_scores.argsort()[0][::-1][:20]  # Get indices of top 20 keywords
        top_keywords = ' '.join(feature_names[index] for index in top_keywords_indices)

        # Append top keywords to the list
        keywords_list_5.append(top_keywords)

        print(keywords_list_5)


    @staticmethod
    def analyze_feedback_sentiment(df_feedback):
        # Define the pattern
        pattern = r'\b(?:но|однако)\b'

        # Filter rows based on the pattern in 'Review_Text' column and star count == 5
        feedbacks_with_no = df_feedback[
            df_feedback['Review_Text'].str.contains(pattern, regex=True) & (df_feedback['Star_Count'] == 5)]

        # Tokenize the text
        nltk.download('punkt')
        nltk.download('stopwords')
        stop_words = set(stopwords.words('russian'))

        # Define the words to be removed
        words_to_remove = {'сожалению', 'поэтому', 'пиджака', 'взяла', 'рекомендую', 'оказался', 'отказ', 'очень',
                           'это', 'спасибо', 'брать', 'просто', 'хотелось', 'легко', 'нем', 'пиджак', 'решила',
                           'продавцу', 'подошел'}

        keywords_list = []  # List to store keywords extracted from all reviews

        for text in feedbacks_with_no['Review_Text']:
            tokens = word_tokenize(text)
            try:
                for i, token in enumerate(tokens):
                    if token in ['но', 'однако']:
                        # Extract words after 'но' or 'однако'
                        words_after_keyword = tokens[i + 1:]
                        # Filter out stop words and punctuation
                        words_after_keyword = [word.lower() for word in words_after_keyword if
                                               word.lower() not in stop_words and word.isalnum() and word not in words_to_remove]
                        # Add keywords to the list
                        keywords_list.extend(words_after_keyword)
            except ValueError:
                pass

        # Count the frequency of keywords
        keyword_freq = Counter(keywords_list)

        # Get the most common keywords and their frequencies
        most_common_keywords = keyword_freq.most_common(20)

        # Filter rows where star count != 5
        other_feedbacks = df_feedback[df_feedback['Star_Count'] != 5]

        # Initialize a dictionary to store the occurrence of each word for different star counts
        word_occurrence_by_star = {word: [0] * 5 for word, _ in most_common_keywords}

        # Extract occurrence of each word for different star counts
        for star_count in range(1, 6):
            feedbacks = df_feedback[df_feedback['Star_Count'] == star_count]
            for i, (word, _) in enumerate(most_common_keywords):
                word_occurrence = sum(
                    1 for text in feedbacks['Review_Text'] for token in word_tokenize(text) if token.lower() == word)
                word_occurrence_by_star[word][star_count - 1] = word_occurrence

        # Create the scatter plot
        plt.figure(figsize=(12, 10))  # Set the size of the plot

        for i, (word, _) in enumerate(most_common_keywords):
            plt.scatter(np.arange(1, 6), [i + 1] * 5, c=np.log10(np.array(word_occurrence_by_star[word]) + 1),
                        cmap='viridis', s=300)

        # Set yticks and labels
        plt.yticks(np.arange(1, len(most_common_keywords) + 1), [word for word, _ in most_common_keywords])
        plt.ylabel('Words')

        # Set xticks and labels
        plt.xticks(np.arange(1, 6), np.arange(1, 6))
        plt.xlabel('Star Count')

        # Create an Axes object for the Colorbar
        cax = plt.axes([0.95, 0.1, 0.02, 0.8])

        # Add color bar
        cb = plt.colorbar(plt.cm.ScalarMappable(cmap='viridis'), cax=cax)
        cb.set_label('Log Frequency')

        # Add title and show plot
        plt.suptitle('Customized Scatter Plot for Top 20 \nMost Common Words in Feedbacks with Different Star Counts',
                     fontsize=16, ha='center')
        plt.grid(False)

        plt.savefig('scatter_plot_top_20.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def keyword_search(df_feedback):
        # Remove rows with 'No info' value in the 'Review_Text' column
        df_feedback = df_feedback[df_feedback['Review_Text'] != 'No info']

        # Define the pattern
        pattern = r'\bно\b|,\s*но\b'

        # Define the words to be removed
        words_to_remove = {'сожалению', 'поэтому', 'пиджака', 'взяла', 'рекомендую', 'оказался', 'очень',
                           'это', 'спасибо', 'брать', 'просто', 'хотелось', 'легко', 'нем', 'пиджак', 'решила',
                           'продавцу', 'подошел', 'хороший', 'плохой', 'пиджак', 'отказ'}

        # Initialize lists to store top keywords for different star ratings
        top_keywords_4_stars = []
        top_keywords_5_stars = []

        # Loop through star ratings 4 and 5
        for star_rating in [4, 5]:
            # Filter rows based on the pattern in 'Review_Text' column and specified star count
            feedbacks_with_no = df_feedback[
                df_feedback['Review_Text'].str.contains(pattern) & (df_feedback['Star_Count'] == star_rating)]

            # Tokenize the text and initialize the variable to store all feedback texts
            all_feedback_text = ' '.join(
                row['Review_Text'].split('но', 1)[-1] for _, row in feedbacks_with_no.iterrows())

            # Tokenize the combined text
            tokens = word_tokenize(all_feedback_text.lower())

            # Remove stopwords
            stop_words = set(stopwords.words('russian'))
            filtered_tokens = [word for word in tokens if
                               word not in stop_words and word.isalpha() and word not in words_to_remove]

            # Convert filtered tokens into documents
            documents = [' '.join(filtered_tokens)]

            # TF-IDF Vectorization
            vectorizer = TfidfVectorizer()
            tfidf_matrix = vectorizer.fit_transform(documents)

            # Get feature names (i.e., words)
            feature_names = vectorizer.get_feature_names_out()

            # Get TF-IDF scores
            tfidf_scores = tfidf_matrix.toarray()

            # Get top keywords with highest TF-IDF scores
            top_keywords_indices = tfidf_scores.argsort()[0][::-1][:70]  # Get indices of top 70 keywords
            top_keywords = [feature_names[index] for index in top_keywords_indices]

            # Append top keywords to the respective lists based on star rating
            if star_rating == 4:
                top_keywords_4_stars.extend(top_keywords)
            elif star_rating == 5:
                top_keywords_5_stars.extend(top_keywords)

        # Preprocess and concatenate all feedback texts for 1, 2, and 3-star reviews
        feedbacks_1_2_3_stars = df_feedback[(df_feedback['Star_Count'] <= 3)]['Review_Text']
        all_text_1_2_3_stars = " ".join(feedbacks_1_2_3_stars)

        # Tokenize the combined text
        tokens = word_tokenize(all_text_1_2_3_stars.lower())

        # Remove stopwords and specified words
        filtered_tokens = [word for word in tokens if
                           word not in stop_words and word.isalpha() and word not in words_to_remove]

        # Convert filtered tokens into documents
        documents = [' '.join(filtered_tokens)]

        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Get feature names (i.e., words)
        feature_names = vectorizer.get_feature_names_out()

        # Get TF-IDF scores
        tfidf_scores = tfidf_matrix.toarray()

        # Get top keywords with highest TF-IDF scores
        top_keywords_indices = tfidf_scores.argsort()[0][::-1][:70]  # Get indices of top 70 keywords
        top_keywords_1_2_3_stars = [feature_names[index] for index in top_keywords_indices]

        print("Top keywords for 1, 2, and 3-star reviews:", top_keywords_1_2_3_stars)
        print("Top keywords for 4-star reviews:", top_keywords_4_stars)
        print("Top keywords for 5-star reviews:", top_keywords_5_stars)

        # Create Venn diagram
        plt.figure(figsize=(8, 8))
        venn = venn3([set(top_keywords_1_2_3_stars), set(top_keywords_4_stars), set(top_keywords_5_stars)],
                     ('1, 2, and 3 stars', '4 stars', '5 stars'))

        # Set labels
        venn.get_label_by_id('100').set_text('\n'.join(top_keywords_1_2_3_stars))
        venn.get_label_by_id('010').set_text('\n'.join(top_keywords_4_stars))
        venn.get_label_by_id('001').set_text('\n'.join(top_keywords_5_stars))

        # Show plot
        plt.title("Venn Diagram of Top Keywords")
        plt.savefig('venn_diagram.png', format='png', dpi=300)
        plt.show()
        plt.close()

        # Convert the keyword lists to sets for efficient intersection operation
        set_1_2_3_stars = set(top_keywords_1_2_3_stars)
        set_4_stars = set(top_keywords_4_stars)
        set_5_stars = set(top_keywords_5_stars)

        # Find the common words among all sets
        common_words = set_1_2_3_stars.intersection(set_4_stars, set_5_stars)
        print("Common words among all star ratings:", common_words)





