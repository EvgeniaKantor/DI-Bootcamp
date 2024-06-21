import pandas as pd
import psycopg2

# function sends dataFrame object in excel
def df_to_excel(df, sheet_name_needed, replace_or_overlay):
    # locate the last row position
    if replace_or_overlay == "overlay":
        start_row = len(pd.read_excel('cv_table.xlsx', sheet_name=sheet_name_needed)) + 1
        # put new info after the last row
        with pd.ExcelWriter('cv_table.xlsx', mode='a', engine='openpyxl',
                            if_sheet_exists=replace_or_overlay) as writer:
            df.to_excel(writer, sheet_name=sheet_name_needed, index=False, header=False, startrow=start_row)
    elif replace_or_overlay == "replace":
        with pd.ExcelWriter('cv_table.xlsx', mode='a', engine='openpyxl',
                            if_sheet_exists=replace_or_overlay) as writer:
            df.to_excel(writer, sheet_name=sheet_name_needed, index=False)

def df_to_sql(new_row_data):
    # connect to sql
    conn = psycopg2.connect(database="CV_tracking", user="postgres",
                            password="654321t", host="localhost", port="5432")
    cursor = conn.cursor()

    columns = ["cur_date", "company_name", "job_title", "address", "contact_name", "description", "feedback",
               "date_feedback"]

    sql = "INSERT INTO cv_table ({}) VALUES ({})".format(
        ", ".join(columns),
        ", ".join(["%s" for _ in columns])
    )

    cursor.execute(sql, new_row_data)
    conn.commit()
    conn.close()

