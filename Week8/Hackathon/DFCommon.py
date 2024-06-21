import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DFCommon:
    @staticmethod
    def create_common_df(df_jackets, df_feedback):
        # title = 'Correlation Heatmap'
        # filename = 'create_common_df.png'
        # Merge df_jackets and df_feedback on 'Barcode'
        df_both = pd.merge(df_jackets, df_feedback, on='Barcode', how='inner')
#############################################################################
        # Create Databases
        df_both_without_no_value = df_both[(df_both['Review_Text'] != 'No info')]
        sale_df = df_both_without_no_value[(df_both_without_no_value['Payment Reason'] == 'Sale')]
        return_df = df_both_without_no_value[(df_both_without_no_value['Payment Reason'] == 'Return')]
#############################################################################
        # DataFrame where Payment Reason is 'Return' is != No info, Star_Count is != 5
        filtered_df_return = return_df[(return_df['Star_Count'] != 5)]
        print(filtered_df_return[['Star_Count', 'Review_Text']].head(20))
 #############################################################################
        # return sale_df, return_df, df_both_without_no_value
        # Copy the DataFrame to avoid modifying the original
        df = df_both_without_no_value.copy()

        # Calculate Delivery Days
        df['Delivery Days'] = (df['Sales Date'] - df['Customer Order Date']).dt.days

        # Add Day of the Week
        df['Day of Week'] = df['Customer Order Date'].dt.dayofweek

        # Encode 'Payment Reason' into dummy variables
        df_encoded = pd.get_dummies(df, columns=['Payment Reason', 'Star_Count'])

        df_encoded = df_encoded.drop(
            ['Item Code', 'Brand_x', 'Supplier Article', 'Name_x', 'Size_x', 'Customer Order Date',
             'Sales Date', 'Quantity', 'Warehouse', 'Country', 'Barcode', 'Date', 'Seller_Article', 'WB_Article', 'Brand_y', 'Review_Text', 'Name_y', 'Region', 'Size_y'], axis=1)

        # Calculate correlations
        correlations = df_encoded.corr()

        # Plot heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()

        plt.savefig('create_common_df.png', format='png', dpi=300)
        plt.show()
        plt.close()
    @staticmethod
    def create_histogram(sale_df, return_df, df_both_without_no_value):
            # Plot histogram for the distribution of prices for purchased and returned jackets
            plt.figure(figsize=(8, 6))
            sns.histplot(data=sale_df, x='Star_Count', bins=20, color='blue', label='Purchased',
                         kde=True)
            sns.histplot(data=return_df, x='Star_Count', bins=20, color='red', label='Returned',
                         kde=True)

            # Set title and labels
            plt.title('Distribution of Feedback (Stars) for Purchased and Returned Jackets', fontsize=16)
            plt.xlabel('Stars', fontsize=14)
            plt.ylabel('Frequency', fontsize=14)
            plt.legend()
            plt.grid(True)
            plt.xticks(sorted(df_both_without_no_value['Star_Count'].unique()))

            # Show plot
            plt.show()

    @staticmethod
    def create_heatmap(df_both_without_no_value):

        # Calculate Delivery Days
        df_both_without_no_value['Delivery Days'] = (df_both_without_no_value['Sales Date'] - df_both_without_no_value['Customer Order Date']).dt.days

        # Add Day of the Week
        df_both_without_no_value['Day of Week'] = df_both_without_no_value['Customer Order Date'].dt.dayofweek

        print(df_both_without_no_value.info())

        # Encode categorical columns using one-hot encoding
        df_encoded = pd.get_dummies(df_both_without_no_value, columns=['Payment Reason'])

        print(df_encoded.info())
        # Create numerical data
        df_encoded_new = df_encoded[['Payment Reason', 'Day of Week', 'Delivery Days', 'Star_Count']].copy()

        # Calculate correlations
        correlations = df_encoded_new.corr()

        # Plot heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Heatmap')
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.show()



