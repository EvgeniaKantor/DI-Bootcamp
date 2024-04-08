from ExcelTable import DataBaseFromAPIs

#####################################
excel_file_name = "Publications.xlsx"
excel_sheet_name = "Publications"
#####################################

if __name__ == "__main__":
    DataBaseFromAPIs.database_from_apis(excel_file_name, excel_sheet_name)
