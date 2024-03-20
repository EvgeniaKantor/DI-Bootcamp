from menu_item import MenuItem
from menu_manager import MenuManager

class MenuEditor:
    @staticmethod
    def show_user_menu():
        print("Program Menu:")
        while True:
            choice = input("Push the button (V-view, A-add, D-delete, U-update, S-show, E-exit): ").upper()
            if choice == 'V':
                MenuEditor.show_menu()
            elif choice == 'A':
                MenuEditor.add_item()
            elif choice == 'D':
                MenuEditor.delete_item()
            elif choice == 'U':
                MenuEditor.update_item()
            elif choice == 'S':
                MenuEditor.show_menu()
            elif choice == 'E':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def add_item():
        item_name = input("Enter the name of the item: ")
        item_price = float(input("Enter the price of the item: "))
        item = MenuItem(item_name, item_price)  # Create an instance of MenuItem
        item.save()  # Call the save method on the instance
        print("Item was added successfully.")

    @staticmethod
    def delete_item():
        item_name = input("Enter the name of the item to delete: ")
        item = MenuItem(item_name)  # Create an instance of MenuItem with the name
        if item.delete():
            print("Item was deleted successfully.")
        else:
            print("Failed to delete item.")

    @staticmethod
    def update_item():
        item_name = input("Enter the name of the item to update: ")
        new_name = input("Enter the new name of the item: ")
        new_price = float(input("Enter the new price of the item: "))
        if MenuManager.get_by_name(item_name):
            if MenuItem.update_by_name(item_name, new_name, new_price):
                print("Item was updated successfully.")
            else:
                print("Failed to update item.")
        else:
            print("Item not found.")

    @staticmethod
    def show_menu():
        menu_items = MenuManager.all()
        print("Restaurant Menu:")
        for item in menu_items:
            print(f"Item Name: {item[0]}, Item Price: {item[1]}")

if __name__ == "__main__":
    editor = MenuEditor()
    editor.show_user_menu()
