import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
import calendar


class VisualClass:

    @staticmethod
    def plot_sales_quantity_by_brand(df_jackets):
        title = 'Total Sales Quantity by Brand'
        filename = 'plot_sales_quantity_by_brand.png'

        # Filter rows where Payment Reason is 'Sale'
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']

        # Total Sales Quantity by Brand
        brand_sales = sale_df.groupby('Brand')['Quantity'].sum().sort_values(ascending=False)
        plt.figure(figsize=(8, 5))
        brand_sales.plot(kind='bar', color='Blue')
        plt.title(title)
        plt.xlabel('Brand')
        plt.ylabel('Total Quantity Sold')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_sales_for_brand(df_jackets):
        title = 'Sales of Each Brand per Month'
        filename = 'plot_sales_for_brand.png'
        # Extract month and year from the 'Sales Date' column
        df_jackets['Sales Month'] = df_jackets['Sales Date'].dt.to_period('M')

        # Group by brand and sales month, then sum the quantity sold
        sales_per_brand_month = df_jackets.groupby(['Brand', 'Sales Month'])['Quantity'].sum().reset_index()

        # Pivot the table to have brands as columns and sales month as index
        sales_per_brand_month_pivot = sales_per_brand_month.pivot(index='Sales Month', columns='Brand',
                                                                  values='Quantity')

        # Plotting
        sales_per_brand_month_pivot.plot(kind='line', marker='o', figsize=(12, 6))
        plt.title(title)
        plt.xlabel('Month')
        plt.ylabel('Quantity Sold')
        plt.xticks(rotation=45)
        plt.legend(title='Brand')
        plt.grid(True)
        plt.tight_layout()

        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_sales_and_returns(df_jackets):
        title = 'Quantity and Percentage of Sales and Returns of Jackets for January-April 2024'
        filename = 'sales_returns_plot.png'
        # Group by month and 'Payment Reason' and sum the 'Quantity' for each category
        sales_returns_monthly = df_jackets.groupby([df_jackets['Sales Date'].dt.month, 'Payment Reason'])[
            'Quantity'].sum()
        # Calculate total quantity for each month
        total_quantity_monthly = df_jackets.groupby(df_jackets['Sales Date'].dt.month)['Quantity'].sum()

        # Calculate percentages of sales and returns for each month
        percentages_monthly = (sales_returns_monthly / total_quantity_monthly) * 100

        # Plot the quantity and percentages of sales and returns for each month
        plt.figure(figsize=(10, 6))
        # Plot stacked bars for quantity
        sales_returns_monthly.unstack().plot(kind='bar', stacked=True, color=['red', 'blue'], ax=plt.gca())
        # Plot percentages as text annotations
        for i, month in enumerate(percentages_monthly.index.levels[0]):
            for j, reason in enumerate(percentages_monthly.index.levels[1]):
                plt.text(i, sales_returns_monthly.loc[month, reason] / 2,
                         f'{percentages_monthly.loc[month, reason]:.2f}%', ha='center', va='center', color='white')
        plt.title(title)
        plt.xlabel('Month')
        plt.ylabel('Quantity')
        plt.xticks(range(len(percentages_monthly.index.levels[0])),
                   [calendar.month_name[m] for m in percentages_monthly.index.levels[0]], rotation=45)
        plt.legend(title='Payment Reason')
        plt.tight_layout()

        # Save it to a file
        plt.savefig(filename, format='png', dpi=300)  # Save plot as PNG with higher resolution
        plt.show()
        plt.close()

    @staticmethod
    def plot_daily_orders(df_jackets):
        title = 'Daily Order Dynamic for 4 months'
        filename = 'plot_daily_orders.png'
        # Filter data for sales after January 1, 2024
        df_filtered = df_jackets[(df_jackets['Customer Order Date'] >= '2024-01-01') &
                                 (df_jackets['Customer Order Date'] <= '2024-04-30')]
        # Group by 'Sales Date' and sum the 'Quantity' for each day
        daily_sales = df_filtered.groupby('Customer Order Date')['Quantity'].sum()

        # Calculate the average sales per day
        average_sales = daily_sales.mean()

        # Plot the daily sales data
        plt.figure(figsize=(10, 6))
        plt.plot(daily_sales.index, daily_sales.values, label='Customer Order Date')

        # Add average line
        plt.axhline(y=average_sales, color='r', linestyle='--', label=f'Average Sales: {average_sales:.2f}')

        # Set labels and title
        plt.xlabel('Order Date')
        plt.ylabel('Sales Quantity')
        plt.title(title)
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save it to a file
        plt.savefig(filename, format='png', dpi=300)  # Save plot as PNG with higher resolution
        plt.show()
        plt.close()

    @staticmethod
    def plot_price_distribution(df_jackets):
        title = 'Distribution of Jacket Prices for Purchased and Returned Jackets'
        filename = 'plot_price_distribution.png'
        # Filter the DataFrame to include only purchased and returned jackets
        purchased_jackets = df_jackets[df_jackets['Payment Reason'] == 'Sale']
        returned_jackets = df_jackets[df_jackets['Payment Reason'] == 'Return']

        # Plot histogram for the distribution of prices for purchased and returned jackets
        plt.figure(figsize=(10, 6))
        sns.histplot(data=purchased_jackets, x='To Seller for Sold Goods', bins=20, color='blue', label='Purchased',
                     kde=True)
        sns.histplot(data=returned_jackets, x='To Seller for Sold Goods', bins=20, color='red', label='Returned',
                     kde=True)

        # Set title and labels
        plt.title(title, fontsize=16)
        plt.xlabel('Price', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.legend()
        plt.grid(True)

        # Show plot
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_scatterplot_sales_and_returns(df_jackets):
        title = 'Sales vs. Returns for Each Jacket'
        filename = 'plot_scatterplot_sales_and_returns.png'
        # Group by 'Supplier Article' and 'Payment Reason' and sum the 'Quantity' for each category
        sales_returns_jackets = df_jackets.groupby(['Supplier Article', 'Payment Reason'])[
            'Quantity'].sum().reset_index()
        # Pivot the table to have 'Supplier Article' as index and 'Quantity' for each 'Payment Reason'
        sales_returns_pivot = sales_returns_jackets.pivot(index='Supplier Article', columns='Payment Reason',
                                                          values='Quantity').fillna(0)

        # Plot using Seaborn's scatterplot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=sales_returns_pivot, x='Sale', y='Return', hue=sales_returns_pivot.index, s=100)
        plt.xlabel('Sales Quantity')
        plt.ylabel('Returns Quantity')
        plt.title(title)
        plt.legend(title='Supplier Article', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_most_popular_jackets(df_jackets):
        title = 'Daily Orders of Top 4 Jackets'
        filename = 'plot_most_popular_jackets.png'
        # Filter rows where Payment Reason is 'Sale'
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']
        # Group by 'Sales Date' and 'Supplier Article', and sum up the sales quantity for each day and jacket
        daily_sales_sale = sale_df.groupby(['Customer Order Date', 'Supplier Article']).agg({'Quantity': 'sum'}).reset_index()
        # Pivot the DataFrame to have 'Sales Date' as index, 'Supplier Article' as columns, and 'Quantity' as values
        pivot_daily_sales_sale = daily_sales_sale.pivot(index='Customer Order Date', columns='Supplier Article',
                                                        values='Quantity')

        # Plot the daily sales of the top 4 jackets
        top_4_jackets = pivot_daily_sales_sale.sum().nlargest(4).index
        pivot_daily_sales_sale[top_4_jackets].plot(kind='line', marker='o', figsize=(12, 6))
        plt.title(title)
        plt.xlabel('Orders Date')
        plt.ylabel('Quantity Sold')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend(title='Supplier Article')
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_analyze_sales_performance(df_jackets):
        title = 'Sales Performance of Jackets'
        filename = 'plot_analyze_sales_performance.png'

        # Filter rows where Payment Reason is 'Sale'
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']

        # Calculate total quantity sold and total price for each jacket article
        total_quantity_sold = sale_df.groupby('Supplier Article')['Quantity'].sum()
        total_price = sale_df.groupby('Supplier Article')['To Seller for Sold Goods'].sum()

        # Sort columns based on total quantity sold
        sorted_articles = total_quantity_sold.sort_values(ascending=False).index

        # Plotting
        fig, ax1 = plt.subplots(figsize=(12, 6))

        ax1.bar(sorted_articles, total_quantity_sold[sorted_articles], color='skyblue', label='Total Quantity Sold')
        ax1.set_xlabel('Supplier Article')
        ax1.set_ylabel('Total Quantity Sold', color='skyblue')
        ax1.tick_params(axis='y', labelcolor='skyblue')
        ax1.set_xticks(range(len(sorted_articles)))
        ax1.set_xticklabels(sorted_articles, rotation=45, ha='right')

        ax2 = ax1.twinx()
        ax2.plot(sorted_articles, total_price[sorted_articles], color='orange', marker='o', label='Total Price')
        ax2.set_ylabel('Total Price', color='orange')
        ax2.tick_params(axis='y', labelcolor='orange')

        plt.title(title)
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()



    @staticmethod
    def plot_sales_quantity_by_size(df_jackets):
        title = 'Total Sales Quantity by Size'
        filename = 'plot_sales_quantity_by_size.png'
        # Filter rows where Payment Reason is 'Sale'
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']

        # Total Sales Quantity by Size
        size_sales = sale_df.groupby('Size (Numerical)')['Quantity'].sum().sort_values(ascending=False)
        plt.figure(figsize=(8, 6))
        size_sales.plot(kind='bar', color='lightcoral')
        plt.title(title)
        plt.xlabel('Size')
        plt.ylabel('Total Quantity Sold')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_scatterplot_sales_vs_returns(df_jackets):
        title = 'Sales vs. Returns for Each Jacket for Each Size'
        filename = 'scatterplot_sales_vs_returns.png'
        # Filter flipper sales and returns
        flipper_sales_returns = df_jackets[df_jackets['Payment Reason'].isin(['Sale', 'Return'])]

        # Group by 'Supplier Article', 'Size', and 'Payment Reason' and sum the 'Quantity' for each category
        flipper_sales_returns_grouped = \
            flipper_sales_returns.groupby(['Supplier Article', 'Size (Numerical)', 'Payment Reason'])[
                'Quantity'].sum().reset_index()

        # Filter only flipper sales and returns
        flipper_sales_returns_grouped = flipper_sales_returns_grouped[
            flipper_sales_returns_grouped['Payment Reason'].isin(['Sale', 'Return'])]

        # Pivot the DataFrame to have separate columns for sales and returns
        pivot_table = flipper_sales_returns_grouped.pivot_table(index=['Supplier Article', 'Size (Numerical)'],
                                                                columns='Payment Reason', values='Quantity',
                                                                fill_value=0).reset_index()

        # Increase the figure size and font sizes
        plt.figure(figsize=(12, 10))
        sns.set_context("paper", font_scale=1.5)

        # Plot scatter plot using Seaborn
        sns.scatterplot(data=pivot_table, x='Sale', y='Return', hue='Size (Numerical)', style='Supplier Article',
                        palette='Set2', s=100)
        plt.xlabel('Sales')
        plt.ylabel('Returns')
        plt.title(title)

        # Adjust legend position
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_analyze_return_percentage(df_jackets):
        title = 'Return Percentage by Jacket Model and Size'
        filename = 'plot_analyze_return_percentage.png'
        # Filter rows where Payment Reason is 'Return'
        return_df = df_jackets[df_jackets['Payment Reason'] == 'Return']

        # Group by 'Supplier Article' and 'Size', count the number of returns for each combination
        return_counts = return_df.groupby(['Supplier Article', 'Size (Numerical)']).size().reset_index(name='Return Count')

        # Group by 'Supplier Article' and 'Size', count the total number of sales for each combination
        total_sales = df_jackets.groupby(['Supplier Article', 'Size (Numerical)']).size().reset_index(name='Total Sales')

        # Merge return counts and total sales
        return_percentage_df = pd.merge(return_counts, total_sales, on=['Supplier Article', 'Size (Numerical)'], how='outer')

        # Calculate return percentage
        return_percentage_df['Return Percentage'] = (return_percentage_df['Return Count'] / return_percentage_df[
            'Total Sales']) * 100

        # Find the combination with the highest return percentage
        max_return_percentage = return_percentage_df.loc[return_percentage_df['Return Percentage'].idxmax()]
        print("Return Percentage DataFrame:")
        print(return_percentage_df)

        print("\nJacket Model and Size with the Highest Return Percentage:")
        print(max_return_percentage)

        # Pivot the DataFrame for visualization
        return_percentage_pivot = return_percentage_df.pivot(index='Supplier Article', columns='Size (Numerical)',
                                                             values='Return Percentage')

        # Plot heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(return_percentage_pivot, cmap='YlGnBu', annot=True, fmt=".2f", linewidths=.5)
        plt.title(title)
        plt.xlabel('Size')
        plt.ylabel('Supplier Article')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()


    @staticmethod
    def subplot_top4_sales_vs_returns(df_jackets):
        # Filter flipper sales and returns
        flipper_sales_returns = df_jackets[df_jackets['Payment Reason'].isin(['Sale', 'Return'])]

        # Group by 'Supplier Article', 'Size', and 'Payment Reason' and sum the 'Quantity' for each category
        flipper_sales_returns_grouped = flipper_sales_returns.groupby(['Supplier Article', 'Size (Numerical)', 'Payment Reason'])[
            'Quantity'].sum().reset_index()

        # Pivot the DataFrame to have separate columns for sales and returns
        pivot_table = flipper_sales_returns_grouped.pivot_table(index=['Supplier Article', 'Size (Numerical)'],
                                                                columns='Payment Reason', values='Quantity',
                                                                fill_value=0).reset_index()

        # Filter to include only the top 4 jackets based on total sales
        top_4_jackets = pivot_table.groupby('Supplier Article')['Sale'].sum().nlargest(4).index

        # Filter the pivot table to include only the top 4 jackets
        top_4_pivot_table = pivot_table[pivot_table['Supplier Article'].isin(top_4_jackets)]

        # Create subplots for each jacket
        fig, axes = plt.subplots(2, 2, figsize=(15, 10), sharex=True, sharey=True)

        for i, (jacket, data) in enumerate(top_4_pivot_table.groupby('Supplier Article')):
            ax = axes[i // 2, i % 2]
            sns.scatterplot(data=data, x='Sale', y='Return', hue='Size (Numerical)', palette='Set2', s=100, ax=ax)
            ax.set_title(f'Jacket: {jacket}')
            ax.set_xlabel('Sales')
            ax.set_ylabel('Returns')
            ax.legend(title='Size')

        # Adjust layout
        plt.tight_layout()
        plt.savefig('subplot_top4_sales_vs_returns.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_histplots_top4_sales(df_jackets):
        title = 'Distribution of Sizes for Top 4 Selling Jackets'
        filename = 'plot_histplots_top4_sales.png'
        # Filter the DataFrame to include only sales transactions
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']

        # Group by 'Supplier Article Name' and sum the 'Quantity' to find the top 4 selling jackets
        top_4_sales = sale_df.groupby('Supplier Article')['Quantity'].sum().nlargest(4).index

        # Create a new DataFrame to store data for the top 4 selling jackets
        top_4_data = pd.DataFrame()

        # Populate the new DataFrame with data for the top 4 selling jackets
        for jacket_name in top_4_sales:
            top_4_data = pd.concat([top_4_data, sale_df[sale_df['Supplier Article'] == jacket_name]])

        # Plot histogram for the distribution of sizes for the top 4 selling jackets
        plt.figure(figsize=(10, 6))
        sns.histplot(data=top_4_data, x='Size (Numerical)', hue='Supplier Article', bins=10, multiple='stack',
                     palette='Set2', edgecolor='black', kde=True)

        # Set title and labels
        plt.title(title, fontsize=16)
        plt.xlabel('Size', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.xticks(sorted(top_4_data['Size (Numerical)'].unique()))
        plt.grid(True)

        # Show plot
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_boxplots_top4_sales(df_jackets):
        title = 'Distribution of Sizes for Top 4 Selling Jackets'
        filename = 'plot_boxplots_top4_sales.png'
        # Filter the DataFrame to include only sales transactions
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']

        # Group by 'Supplier Article Name' and sum the 'Quantity' to find the top 4 selling jackets
        top_4_sales = sale_df.groupby('Supplier Article')['Quantity'].sum().nlargest(4).index

        # Create a new DataFrame to store data for the top 4 selling jackets
        top_4_data = pd.DataFrame()

        # Populate the new DataFrame with data for the top 4 selling jackets
        for jacket_name in top_4_sales:
            top_4_data = pd.concat([top_4_data, sale_df[sale_df['Supplier Article'] == jacket_name]])

        # Create boxplot for the distribution of sizes for the top 4 selling jackets
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=top_4_data, x='Size (Numerical)', hue='Supplier Article', palette='Set2', legend=False)

        # Set title and labels
        plt.title(title, fontsize=16)
        plt.xlabel('Jacket', fontsize=14)
        plt.ylabel('Size', fontsize=14)
        plt.xticks(sorted(top_4_data['Size (Numerical)'].unique()))

        # Show plot
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()



    @staticmethod
    def plot_price_distribution(df_jackets):
        title = 'Distribution of Jacket Prices for Purchased and Returned Jackets'
        filename = 'plot_price_distribution.png'
        # Filter the DataFrame to include only purchased and returned jackets
        purchased_jackets = df_jackets[df_jackets['Payment Reason'] == 'Sale']
        returned_jackets = df_jackets[df_jackets['Payment Reason'] == 'Return']

        # Plot histogram for the distribution of prices for purchased and returned jackets
        plt.figure(figsize=(10, 6))
        sns.histplot(data=purchased_jackets, x='To Seller for Sold Goods', bins=20, color='blue', label='Purchased',
                     kde=True)
        sns.histplot(data=returned_jackets, x='To Seller for Sold Goods', bins=20, color='red', label='Returned',
                     kde=True)

        # Set title and labels
        plt.title(title, fontsize=16)
        plt.xlabel('Price', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.legend()
        plt.grid(True)

        # Show plot
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_correlation_returns(df_jackets):
        title = 'Correlation Heatmap'
        filename = 'plot_correlation_returns.png'

        # Calculate Delivery Days
        df_jackets['Delivery Days'] = (df_jackets['Sales Date'] - df_jackets['Customer Order Date']).dt.days

        # Add Day of the Week
        df_jackets['Day of Week'] = df_jackets['Customer Order Date'].dt.dayofweek

        # Encode categorical columns using one-hot encoding
        df_encoded = pd.get_dummies(df_jackets, columns=['Payment Reason', 'Day of Week'])
        # Drop non-numeric columns if any

        df_encoded = df_encoded.drop(
            ['Item Code', 'Brand', 'Supplier Article', 'Name', 'Size', 'Customer Order Date', 'Sales Date',
             'Country', 'Barcode', 'Quantity', 'Warehouse', 'Sales Month', 'Discount_Level'], axis=1)

        # Calculate correlations
        correlations = df_encoded.corr()

        # Plot heatmap
        plt.figure(figsize=(15, 12))
        sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title(title)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()

        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_monthly_size(df_jackets):
        df_jackets['Month'] = df_jackets['Sales Date'].dt.month
        # Group by month, 'Payment Reason', and 'Size' and sum the 'Quantity' for each category
        sales_monthly_size = df_jackets.groupby(['Month', 'Payment Reason', 'Size (Numerical)'])[
            'Quantity'].sum().reset_index()

        # Plot the quantity and percentages of sales and returns for each month and Size (Numerical) using sns.catplot
        g = sns.catplot(data=sales_monthly_size, x='Month', y='Quantity', hue='Size (Numerical)',
                        col='Payment Reason', kind='bar', palette='tab10', aspect=1.5, height=6, legend_out=False)
        g.set_axis_labels('Month', 'Quantity')
        plt.xticks(rotation=0)
        g.set_titles("{col_name}")
        plt.tight_layout()
        # Move the legend to the top-left corner
        plt.legend(loc='upper left')

        plt.savefig('plot_monthly_size.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_quantity_per_day_of_week(df_jackets):
        # Convert Customer Order Date to datetime
        df_jackets['Customer Order Date'] = pd.to_datetime(df_jackets['Customer Order Date'])

        # Extract day of the week from Customer Order Date
        df_jackets['Day of Week'] = df_jackets['Customer Order Date'].dt.dayofweek

        # Group by Day of the Week and sum the quantities and Wildberries Sold Goods (Pro)
        quantity_per_day = df_jackets.groupby('Day of Week')['Quantity'].sum()
        wildberries_per_day = df_jackets.groupby('Day of Week')['Wildberries Sold Goods (Pro)'].sum()

        # Plot the graphs
        fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 12))

        # Plot total quantity purchased per day
        quantity_per_day.plot(kind='bar', color='skyblue', ax=axes[0])
        axes[0].set_title('Total Quantity Purchased per Day of the Week')
        axes[0].set_xlabel('Day of the Week')
        axes[0].set_ylabel('Total Quantity Purchased')
        axes[0].set_xticks(range(7))
        axes[0].set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], rotation=45)

        # Plot total Wildberries Sold Goods (Pro) per day
        wildberries_per_day.plot(kind='bar', color='lightgreen', ax=axes[1])
        axes[1].set_title('Total Cost of Jackets Sold on Each Single Day of the Week')
        axes[1].set_xlabel('Day of the Week')
        axes[1].set_ylabel('Total cost of jackets')
        axes[1].set_xticks(range(7))
        axes[1].set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], rotation=45)

        plt.tight_layout()

        plt.savefig('plot_quantity_per_day_of_week.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def categorize_discount(df_jackets):
        discount_levels = []
        for discount in df_jackets['Permanent Customer Discount (%)']:
            if discount == 0:
                discount_levels.append('Zero')
            elif discount <= 0.05:
                discount_levels.append('Low')
            elif discount <= 0.15:
                discount_levels.append('Medium-Low')
            elif discount <= 0.2:
                discount_levels.append('Medium-High')
            else:
                discount_levels.append('High')
        df_jackets['Discount_Level'] = discount_levels

        return_df = df_jackets[df_jackets['Payment Reason'] == 'Return']
        sale_df = df_jackets[df_jackets['Payment Reason'] == 'Sale']
        # Calculate return rate per discount level
        return_rates = return_df.groupby('Discount_Level')['Wildberries Sold Goods (Pro)'].sum() / \
                       return_df.groupby('Discount_Level')['Quantity'].sum()

        sale_rates = sale_df.groupby('Discount_Level')['Wildberries Sold Goods (Pro)'].sum() / \
                       sale_df.groupby('Discount_Level')['Quantity'].sum()

        # Calculate average discount per discount level
        avg_discount = sale_df.groupby('Discount_Level')['Permanent Customer Discount (%)'].mean()

        # Calculate frequency and recency of transactions per discount level
        frequency_sale = sale_df.groupby('Discount_Level').size()
        ferquency_return = return_df.groupby('Discount_Level').size()
        recency = (pd.Timestamp.now() - sale_df.groupby('Discount_Level')['Customer Order Date'].max()).dt.days

        # Create a DataFrame to store discount level analysis results
        discount_level_analysis = pd.DataFrame({
            'Frequency_Sales': frequency_sale,
            'Frequency_Returns': ferquency_return,
            'Recency': recency,
            'Avg_Discount': avg_discount,
            'Return_Rate': return_rates,
            'Sale_Rate': sale_rates
        })

        # Display the discount level analysis
        print(discount_level_analysis)

        # Sort discount level segments by frequency of transactions
        most_active_buying = discount_level_analysis.sort_values(by='Frequency_Sales', ascending=False).index[0]

        # Sort discount level segments by return rate
        most_active_returning = discount_level_analysis.sort_values(by='Frequency_Returns', ascending=False).index[0]

        print("Most Actively Buying Segment:", most_active_buying)
        print("Most Actively Returning Segment:", most_active_returning)

        discount_level_analysis.sort_index(ascending=False, inplace=True)
        # Plot frequency of sales and average discount
        fig, ax1 = plt.subplots(figsize=(8, 4))
        color = 'tab:blue'
        ax1.set_xlabel('Discount Level')
        ax1.set_ylabel('Frequency', color=color)
        ax1.bar(discount_level_analysis.index, discount_level_analysis['Frequency_Sales'], color=color, alpha=0.7)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:red'
        ax2.set_ylabel('Average Discount', color=color)
        ax2.plot(discount_level_analysis.index, discount_level_analysis['Avg_Discount'], color=color, marker='o')
        ax2.tick_params(axis='y', labelcolor=color)

        fig.tight_layout()
        plt.title('Frequency of Sales and Average Discount by Discount Level')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig('categorize_discount_1.png', format='png', dpi=300)
        plt.show()
        plt.close()

        # Plot return rates
        plt.figure(figsize=(8, 4))
        plt.bar(discount_level_analysis.index, discount_level_analysis['Frequency_Returns'], color='salmon')
        plt.title('Return Rate by Discount Level')
        plt.xlabel('Discount Level')
        plt.ylabel('Return Rate')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig('categorize_discount_2.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_warehouses(df_jackets):
        # Calculate total quantity of jackets sold and returned for each warehouse
        warehouse_sales = df_jackets.groupby('Warehouse')['Quantity'].sum().sort_values(ascending=False)
        warehouse_returns = df_jackets[df_jackets['Payment Reason'] == 'Return'].groupby('Warehouse')[
            'Quantity'].sum().sort_values(ascending=False)

        # Plot top warehouses for sales
        plt.figure(figsize=(10, 6))
        warehouse_sales.head(10).plot(kind='bar', color='skyblue')
        plt.title('Top 10 Warehouses by Jacket Sales')
        plt.xlabel('Warehouse')
        plt.ylabel('Total Quantity Sold')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig('plot_warehouses_1.png', format='png', dpi=300)
        plt.show()
        plt.close()

        # Plot top warehouses for returns
        plt.figure(figsize=(10, 6))
        warehouse_returns.head(10).plot(kind='bar', color='salmon')
        plt.title('Top 10 Warehouses by Jacket Returns')
        plt.xlabel('Warehouse')
        plt.ylabel('Total Quantity Returned')
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        plt.savefig('plot_warehouses_2.png', format='png', dpi=300)
        plt.show()
        plt.close()
############################################################################
        # To find the percentage of returns for each warehouse, we can calculate the total quantity of jackets returned for each warehouse and then divide it by the total quantity of jackets sold for that warehouse.

        # Calculate total quantity of jackets sold and returned for each warehouse
        total_sales_per_warehouse = df_jackets.groupby('Warehouse')['Quantity'].sum()
        total_returns_per_warehouse = df_jackets[df_jackets['Payment Reason'] == 'Return'].groupby('Warehouse')[
            'Quantity'].sum()

        # Calculate return percentage for each warehouse
        return_percentage_per_warehouse = (total_returns_per_warehouse / total_sales_per_warehouse) * 100
        # Sort the return percentage DataFrame by the return percentage values in descending order
        return_percentage_per_warehouse_sorted = return_percentage_per_warehouse.sort_values(ascending=False)

        # Display the sorted return percentage for each warehouse
        print("Return Percentage for Each Warehouse (Sorted):")
        print(return_percentage_per_warehouse_sorted)
###########################################################################
        # Sort the data by total sales per warehouse in ascending order
        sorted_total_sales_per_warehouse = total_sales_per_warehouse.sort_values()

        # Create figure and axis objects
        fig, ax = plt.subplots(figsize=(12, 8))

        # Plot total number of deliveries
        ax.bar(range(len(sorted_total_sales_per_warehouse)), sorted_total_sales_per_warehouse,
               color='skyblue',
               label='Total Deliveries')

        # Create a secondary y-axis for return percentage
        ax2 = ax.twinx()
        sorted_return_percentage_per_warehouse = return_percentage_per_warehouse.reindex(
            sorted_total_sales_per_warehouse.index)  # Reorder to match the index
        ax2.plot(range(len(sorted_return_percentage_per_warehouse)), sorted_return_percentage_per_warehouse,
                 color='salmon',
                 marker='o',
                 label='Return Percentage', linestyle='--')

        # Set y-axis labels
        ax.set_ylabel('Total Deliveries')
        ax2.set_ylabel('Return Percentage')

        # Set title and legend
        plt.title('Total Deliveries and Return Percentage by Warehouse')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Rotate x-axis labels for better readability
        ax.set_xticks(range(len(sorted_total_sales_per_warehouse)))
        ax.set_xticklabels(sorted_total_sales_per_warehouse.index, rotation=45, ha='right')

        # Display grid
        ax.grid(True)
        ax2.grid(False)

        # Show plot
        plt.tight_layout()

        plt.savefig('plot_warehouses_3.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def cloud_feedbacks(df_feedback):

        # Filter out rows with 'No info' in the 'Review_Text' column
        text_reviews = df_feedback[df_feedback['Review_Text'] != 'No info']

        # Concatenate all feedback text into a single string
        feedback_text = ' '.join(text_reviews['Review_Text'].dropna())

        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(feedback_text)

        # Display the word cloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title('Word Cloud of Feedback Text')
        plt.axis('off')

        plt.savefig('cloud_feedbacks_1.png', format='png', dpi=300)
        plt.show()
        plt.close()

        # Tokenize the text
        tokens = nltk.word_tokenize(feedback_text)

        # Remove stopwords
        russian_stopwords = set(stopwords.words('russian'))
        filtered_tokens = [word for word in tokens if word.lower() not in russian_stopwords]

        # Join the filtered tokens back into a single string
        filtered_text = ' '.join(filtered_tokens)

        # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

        # Display the word cloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title('Word Cloud of Feedback Text (Without Russian Stopwords)')
        plt.axis('off')

        plt.savefig('cloud_feedbacks_2.png', format='png', dpi=300)
        plt.show()
        plt.close()

    @staticmethod
    def plot_star_count(df_feedback):
        title = 'Distribution of Star Ratings'
        filename = 'plot_star_count.png'
        # Set style
        sns.set_style("whitegrid")

        # Plot histogram of Star_Count
        plt.figure(figsize=(8, 6))
        ax = sns.histplot(data=df_feedback, x='Star_Count', bins=5, color='skyblue', edgecolor='black', alpha=0.7)

        # Add labels to the bars
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center',
                        va='center', xytext=(0, 5), textcoords='offset points')

        # Set title and labels
        plt.title(title)
        plt.xlabel('Star Count')
        plt.ylabel('Frequency')

        # Set ticks for each star rating
        plt.xticks(range(1, 6))

        # Show plot
        plt.savefig(filename, format='png', dpi=300)
        plt.show()
        plt.close()


