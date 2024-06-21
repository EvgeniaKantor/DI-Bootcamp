import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price=0):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        conn = psycopg2.connect(database="restaurant", user="postgres", password="654321t", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
        val = (self.item_name, self.item_price)
        cursor.execute(query, val)
        conn.commit()
        conn.close()  # Close the connection after committing changes

    def delete(self):
        conn = psycopg2.connect(database="restaurant", user="postgres", password="654321t", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "DELETE FROM menu_items WHERE item_name = %s"
        val = (self.item_name,)
        cursor.execute(query, val)
        conn.commit()
        conn.close()

    def update(self, new_name=None, new_price=None):
        """
        Updates the name and/or price of an item.
        """
        conn = psycopg2.connect(database="restaurant", user="postgres", password="654321t", host="localhost", port="5432")
        cursor = conn.cursor()
        update_query = "UPDATE menu_items SET "
        val = []
        if new_name:
            update_query += "item_name = %s, "
            val.append(new_name)
        if new_price:
            update_query += "item_price = %s, "
            val.append(new_price)
        update_query = update_query.rstrip(", ")
        update_query += " WHERE item_name = %s"
        val.append(self.item_name)

        cursor.execute(update_query, val)
        conn.commit()
        conn.close()

# Example usage:
# Create an instance of MenuItem
menu_item = MenuItem("Burger", 10)

# Save the menu item
menu_item.save()

# Delete the menu item
menu_item.delete()

# Update a menu item
menu_item.update(new_name="New Burger", new_price=12)

