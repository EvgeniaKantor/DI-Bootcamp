from DF import CreatDF
from CleanDF import CleanDF
# List of Excel files
excel_files = [
    "250071021.xlsx",
    "251481580.xlsx",
    "253032708.xlsx",
    "254285020.xlsx",
    "254474731.xlsx",
    "256225279.xlsx",
    "257596234.xlsx",
    "258244699.xlsx",
    "260540432.xlsx",
    "261270550.xlsx",
    "261805955.xlsx",
    "262214918.xlsx",
    "262547816.xlsx",
    "263015104.xlsx",
    "263442090.xlsx",
    "50994487.xlsx",
    "54994084.xlsx",
    "53509805.xlsx",
    "53005540.xlsx",
    "53253100.xlsx",
    "53509805.xlsx",
    "54994084.xlsx",
    "52083221.xlsx",
    "51821584.xlsx"
]

#################################
excel_file_name = "Sales.xlsx"
excel_sheet_name = "Sales"
#################################

if __name__ == "__main__":
    # Call the function and store the result in df_sales
    df_sales = CreatDF.merge_and_sort_excel_files(excel_files)

    CleanDF.find_duplicates(df_sales)
    CleanDF.drop_duplicates(excel_file_name, excel_sheet_name, df_sales)

