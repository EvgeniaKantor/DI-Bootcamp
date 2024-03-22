import requests
import psycopg2
import random

def fetch_countries():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch countries')
        return None

def create_countries_table():
    conn = psycopg2.connect(database="bootcamp", user="postgres", password="654321t", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255),
            capital VARCHAR(255),
            flag VARCHAR(255),
            subregion VARCHAR(255),
            population INT
        )
    """)
    conn.commit()
    conn.close()

def insert_countries(data):
    conn = psycopg2.connect(database="bootcamp", user="postgres", password="654321t", host="localhost", port="5432")
    cursor = conn.cursor()
    for country in random.sample(data, 10):
        name = country.get('name', {}).get('common', 'No name')
        capital = str(country.get('capital', 'No Capital'))
        flag = country.get('flags', {}).get('png', 'No flag')
        subregion = country.get('subregion', 'No subregion')
        population = country.get('population', 0)
        cursor.execute("INSERT INTO countries (name, capital, flag, subregion, population) VALUES (%s, %s, %s, %s, %s)", (name, capital, flag, subregion, population))
    conn.commit()
    conn.close()

def main():
    create_countries_table()  # Create the countries table if it doesn't exist
    countries_data = fetch_countries()
    if countries_data:
        insert_countries(countries_data)

if __name__ == "__main__":
    main()
