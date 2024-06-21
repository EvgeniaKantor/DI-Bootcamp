import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer

# # Download required NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def extract_keywords(database):
    # Initialize NLTK resources
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    # Combine all titles into a single list
    titles = database['Title'].tolist()
    keywords_list = []  # List to store keywords extracted from all titles

    for title in titles:
        # Tokenization
        tokens = word_tokenize(title)

        # Remove stopwords
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Part-of-speech tagging
        tagged_tokens = pos_tag(filtered_tokens)

        # Lemmatization of nouns only
        lemmatized_tokens = [lemmatizer.lemmatize(word, pos='n') for word, pos in tagged_tokens if pos.startswith('NN')]

        # Join tokens back into a sentence
        preprocessed_title = ' '.join(lemmatized_tokens)

        # TF-IDF Vectorization
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([preprocessed_title])

        # Get feature names (i.e., words)
        feature_names = vectorizer.get_feature_names_out()

        # Get TF-IDF scores
        tfidf_scores = tfidf_matrix.toarray()

        # Get top keywords with highest TF-IDF scores
        top_keywords_indices = tfidf_scores.argsort()[0][::-1][:2]  # Get indices of top 2 keywords
        top_keywords =' '.join(feature_names[index] for index in top_keywords_indices)


        # Append top keywords to the list
        keywords_list.append(top_keywords)

    return keywords_list

