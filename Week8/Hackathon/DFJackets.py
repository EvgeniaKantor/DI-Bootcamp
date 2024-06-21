import pandas as pd


class DFJackets:
    @staticmethod
    def create_df_jackets(df_sales_cleaned):
        """
        Create a DataFrame specifically for jacket-related sales data.
        Args: df_sales (pandas.DataFrame): DataFrame containing sales data.
        Returns: pandas.DataFrame: DataFrame with selected columns.
        """
        # Select specific columns for jacket-related sales data
        df_jackets = df_sales_cleaned[['Код номенклатуры', 'Бренд', 'Артикул поставщика', 'Название', 'Размер',
                               'Обоснование для оплаты', 'Дата заказа покупателем', 'Дата продажи',
                               'Кол-во', 'Цена розничная', 'Вайлдберриз реализовал Товар (Пр)',
                               'Скидка постоянного Покупателя (СПП), %',
                               'К перечислению Продавцу за реализованный Товар',
                               'Склад', 'Страна', 'ШК']].copy()

        # Replace None values with 0 in the 'prices' column
        df_jackets['Скидка постоянного Покупателя (СПП), %'] = df_jackets['Скидка постоянного Покупателя (СПП), %'].fillna(0)

        # Translate column names
        translated_column_names = {
            'Код номенклатуры': 'Item Code',
            'Бренд': 'Brand',
            'Артикул поставщика': 'Supplier Article',
            'Название': 'Name',
            'Размер': 'Size',
            'Обоснование для оплаты': 'Payment Reason',
            'Дата заказа покупателем': 'Customer Order Date',
            'Дата продажи': 'Sales Date',
            'Кол-во': 'Quantity',
            'Цена розничная': 'Retail Price',
            'Вайлдберриз реализовал Товар (Пр)': 'Wildberries Sold Goods (Pro)',
            'Скидка постоянного Покупателя (СПП), %': 'Permanent Customer Discount (%)',
            'К перечислению Продавцу за реализованный Товар': 'To Seller for Sold Goods',
            'Склад': 'Warehouse',
            'Страна': 'Country',
            'ШК': 'Barcode'
        }

        # Rename columns
        df_jackets.rename(columns=translated_column_names, inplace=True)

        # Translate and rename values in the 'Payment Reason' column
        df_jackets['Payment Reason'] = df_jackets['Payment Reason'].replace({'Продажа': 'Sale', 'Возврат': 'Return'})

        # Filter purchases for January, February, March, and April
        df_jackets = df_jackets[df_jackets['Sales Date'].dt.month.isin([1, 2, 3, 4])]

        # Reset index if needed
        df_jackets.reset_index(drop=True, inplace=True)

        # Define the size mapping dictionary
        size_mapping = {
            'XXS': 40,
            'XS': 42,
            'S': 44,
            'M': 46,
            'L': 48,
            'XL': 50,
            'XXL': 52,
            '3XL': 54,
            '34': 34,
            '40': 40,
            '42': 42,
            '46': 46,
            '48': 48,
            '50': 50,
            '52': 52,
        }

        # Use the map function to create a new column with numerical values based on the size labels
        df_jackets['Size (Numerical)'] = df_jackets['Size'].map(size_mapping)

        # Define the mapping of old values to new values
        warehouse_mapping = {
            'Астана': 'Astana',
            'Атакент': 'Atakent',
            'Белая дача': 'Belaya Dacha',
            'Белые Столбы': 'Belye Stolby',
            'Волгоград': 'Volgograd',
            'Екатеринбург - Испытателей 14г': 'Yekaterinburg - Ispytatelei',
            'Екатеринбург - Перспективный 12': 'Yekaterinburg - Perspektivny',
            'Казань': 'Kazan',
            'Коледино': 'Koledino',
            'Краснодар': 'Krasnodar',
            'Невинномысск': 'Nevinnomyssk',
            'Новосибирск': 'Novosibirsk',
            'Подольск': 'Podolsk',
            'Рязань (Тюшевское)': 'Ryazan (Tyushevskoe)',
            'Санкт-Петербург Уткина Заводь': 'St. Petersburg Utkina Zavod',
            'Санкт-Петербург Шушары': 'St. Petersburg Shushary',
            'Тула': 'Tula',
            'Хабаровск': 'Khabarovsk',
            'Электросталь': 'Elektrostal'
        }

        # Replace the old values with the new values
        df_jackets['Warehouse'] = df_jackets['Warehouse'].replace(warehouse_mapping)

        return df_jackets
