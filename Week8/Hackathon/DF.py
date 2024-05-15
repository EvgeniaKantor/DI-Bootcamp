import pandas as pd


class CreatDF:
    @staticmethod
    def merge_and_sort_excel_files(files):
        """
            Merge and sort Excel files containing sales data.
            Args: files (list): List of Excel file paths.
            Returns: pandas.DataFrame: Sorted and filtered DataFrame.
        """
        # Initialize an empty list to store DataFrames
        dfs = []

        # Read each Excel file and append its DataFrame to the list
        for file in files:
            try:
                df = pd.read_excel(file)
                dfs.append(df)
            except FileNotFoundError:
                print(f"File {file} not found. Skipping...")

        # Concatenate all DataFrames into a single DataFrame
        combined_df = pd.concat(dfs)

        # Convert "Дата продажи" to date type
        combined_df['Дата продажи'] = pd.to_datetime(combined_df['Дата продажи'])
        combined_df['Дата заказа покупателем'] = pd.to_datetime(combined_df['Дата заказа покупателем'])

        # Filter rows where "Предмет" is 'Пиджаки'
        filtered_df = combined_df[combined_df['Предмет'] == 'Пиджаки']

        # Sort the filtered DataFrame by the column "Дата продажи"
        sorted_df = filtered_df.sort_values(by="Дата продажи")

        # Filter rows where 'Обоснование для оплаты' is either 'Продажа' or 'Возврат'
        sorted_df = sorted_df[sorted_df['Обоснование для оплаты'].isin(['Продажа', 'Возврат'])].copy()

        return sorted_df

