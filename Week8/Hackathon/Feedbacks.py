import pandas as pd
import matplotlib.pyplot as plt


feedback_exel_file = 'feedback.xlsx'
df_feedback = pd.read_excel(feedback_exel_file)

# Dictionary containing old column names as keys and new column names as values
new_column_names = {
    'ID отзыва': 'Review_ID',
    'Дата': 'Date',
    'Артикул продавца': 'Seller_Article',
    'Артикул WB': 'WB_Article',
    'Количество звезд': 'Star_Count',
    'Бренд': 'Brand',
    'Текст отзыва': 'Review_Text',
    'Имя': 'Name',
    'Регион': 'Region',
    'Цвет': 'Color',
    'Размер': 'Size',
    'Полезность (количество минусов)': 'Usefulness_Minus_Count',
    'Полезность (количество плюсов)': 'Usefulness_Plus_Count',
    'Штрихкод': 'Barcode',
    'Ответ': 'Response'
}

# Rename columns
df_feedback.rename(columns=new_column_names, inplace=True)

# List of articles you want to filter
articles = ['blazer_sun', 'blazer_peach', 'blazer_dark', 'blazer_brown', 'blazer_green',
            'blazer_pink', 'blazer_grey', 'blazer_black', 'blazer_blue', 'blazer_turan',
            'blazer_bezh', 'blazer_oliva', 'tvid_blue', 'tvid_violet', 'tvid_black',
            'tvid_white', 'blazer_chess', 'blazer_darkgrey']


# Filter articles
df_feedback = df_feedback[df_feedback['Seller_Article'].isin(articles)]

# Convert 'Date' column to datetime with correct format
df_feedback['Date'] = pd.to_datetime(df_feedback['Date'], format='%d/%m/%Y')

# Filter purchases for January, February, March, and April
df_feedback = df_feedback[df_feedback['Date'].dt.month.isin([1, 2, 3, 4])]

# Drop columns
df_feedback.drop(columns=['Review_ID', 'Usefulness_Minus_Count', 'Usefulness_Plus_Count', 'Color', 'Response'], inplace=True)

# Fill empty values in specified columns with 'No info'
df_feedback[['Review_Text', 'Name', 'Size']] = df_feedback[['Review_Text', 'Name', 'Size']].fillna('No info')

# Delete rows with empty values
df_feedback.dropna(axis=0, how='any', inplace=True)

# Replace specific values in the 'Region' column
df_feedback['Region'] = df_feedback['Region'].replace({'ru': 'RU', 'by': 'BY', 'am': 'AM', 'uz': 'UZ', 'kz': 'KZ'})

# Calculate the average rating
average_rating = df_feedback['Star_Count'].mean()
print("Average Rating:", average_rating)

# Count the number of reviews by region
reviews_by_region = df_feedback['Region'].value_counts()
print("Reviews by Region:\n", reviews_by_region)

# Determine the most common names among reviewers
common_names = df_feedback['Name'].value_counts().head(10)
print("Most Common Names:\n", common_names)



