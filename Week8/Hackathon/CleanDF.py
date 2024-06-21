from DFJackets import DFJackets
import pandas as pd
import os


class CleanDF:
    @staticmethod
    def find_duplicates(df_sales):
        duplicates = df_sales.duplicated()
        # Print the count of duplicate rows
        print("Number of duplicate rows:", duplicates.sum())

    @staticmethod
    def drop_duplicates(excel_file_name, excel_sheet_name, df_sales):
        # Drop duplicate rows from the DataFrame
        df_sales_cleaned = df_sales.drop_duplicates()

        if not ExcelTable.excel_database_exists(excel_file_name):
            df_jackets = DFJackets.create_df_jackets(df_sales_cleaned)
            ExcelTable.database_to_excel(df_jackets, excel_file_name, excel_sheet_name)
            print(f"DataFrame has been saved to '{excel_file_name}' in sheet '{excel_sheet_name}'.")
            print(df_jackets.head())
        else:
            df_jackets = ExcelTable.database_from_excel(excel_file_name, excel_sheet_name)
            print(df_jackets.head())

        return df_jackets


class ExcelTable:
    @staticmethod
    def database_to_excel(df_sales, excel_file_name, excel_sheet_name):
        df_sales.to_excel(excel_file_name, sheet_name=excel_sheet_name, index=False)

    @staticmethod
    def excel_database_exists(excel_file_name):
        return os.path.isfile(excel_file_name)

    @staticmethod
    def database_from_excel(excel_file_name, excel_sheet_name):
        df_sales = pd.read_excel(excel_file_name, sheet_name=excel_sheet_name)
        return df_sales
