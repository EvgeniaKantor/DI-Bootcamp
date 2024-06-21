from main import excel_file_name, excel_sheet_name
from VisualClass import VisualClass
from CleanDF import ExcelTable
from PresentationClass import PresentationClass
from GetFoto import GetFoto
from Feedbacks import df_feedback
import pandas as pd
from DFCommon import DFCommon
from TextAnalyse import TextAnalyse
from BackOpenAI import BackOpenAI

if not ExcelTable.excel_database_exists(excel_file_name):

    print("Excel file does not exists")
else:

    df_jackets = ExcelTable.database_from_excel(excel_file_name, excel_sheet_name)

################################################################
    # get_foto = GetFoto()
    # get_foto.fetch_images_for_top_jackets(df_jackets)
################################################################
    PresentationClass.create_presentation()
###############################################################
    #
    # VisualClass.plot_sales_quantity_by_brand(df_jackets)
    # VisualClass.plot_sales_and_returns(df_jackets)
    # VisualClass.plot_sales_for_brand(df_jackets)
    # VisualClass.plot_daily_orders(df_jackets)
    # VisualClass.plot_price_distribution(df_jackets)
    # VisualClass.plot_scatterplot_sales_and_returns(df_jackets)
    # VisualClass.plot_most_popular_jackets(df_jackets)
    # VisualClass.plot_analyze_sales_performance(df_jackets)
    # VisualClass.plot_scatterplot_sales_vs_returns(df_jackets)
    # VisualClass.plot_sales_quantity_by_size(df_jackets)
    # VisualClass.subplot_top4_sales_vs_returns(df_jackets)
    # VisualClass.plot_monthly_size(df_jackets)
    # VisualClass.plot_boxplots_top4_sales(df_jackets)
    # VisualClass.plot_analyze_return_percentage(df_jackets)
    # VisualClass.plot_histplots_top4_sales(df_jackets)
    #
    # VisualClass.plot_quantity_per_day_of_week(df_jackets)
    #
    # VisualClass.categorize_discount(df_jackets)
    #
    # VisualClass.plot_warehouses(df_jackets)
    #
    # VisualClass.plot_quantity_per_day_of_week(df_jackets)
    #
    # VisualClass.plot_correlation_returns(df_jackets)

#####################################################
    # VisualClass.cloud_feedbacks(df_feedback)
    # VisualClass.plot_star_count(df_feedback)

######################################################

    # DFCommon.create_common_df(df_jackets, df_feedback)

# #######################################################
#     TextAnalyse.create_sentiments(df_feedback)
#     TextAnalyse.my_sentiment_analysis(df_feedback)
#     TextAnalyse.print_sentences_after_no(df_feedback)
#     TextAnalyse.analyze_feedback_sentiment(df_feedback)
#     TextAnalyse.keyword_search(df_feedback)
#
    # BackOpenAI.generate_feedbacks(df_feedback)

