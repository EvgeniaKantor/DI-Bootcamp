import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        conn = psycopg2.connect(database="restaurant", user="postgres", password="654321t", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "SELECT * FROM menu_items WHERE item_name = %s"
        cursor.execute(query, (item_name,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result  # Assuming item_name is at index 1 and item_price is at index 2
        else:
            return None

    @classmethod
    def all(cls):
        conn = psycopg2.connect(database="restaurant", user="postgres", password="654321t", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "SELECT item_name, item_price FROM menu_items"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results

# Usage example
all_items = MenuManager.all()
print("All items:")
for item in all_items:
    print(item)

get_by_name = MenuManager.get_by_name("Burger")
print(get_by_name)