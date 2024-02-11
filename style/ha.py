class DataManagement:
    def __init__(self):
        self.data = {}

    def insert_data(self, key, value):
        self.data[key] = value
        print(f"Data inserted: {key} - {value}")

    def update_data(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value
            print(f"Data updated: {key} - {new_value}")
        else:
            print(f"Key {key} not found.")

    def search_data(self, key):
        if key in self.data:
            print(f"Data found: {key} - {self.data[key]}")
        else:
            print(f"Key {key} not found.")

    def delete_data(self, key):
        if key in self.data:
            del self.data[key]
            print(f"Data deleted: {key}")
        else:
            print(f"Key {key} not found.")

    def view_all_data(self):
        print("All Data:")
        for key, value in self.data.items():
            print(f"{key} - {value}")


def print_menu():
    print("\nMenu:")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Search Data")
    print("4. Delete Data")
    print("5. View All Data")
    print("6. Exit")


def main():
    data_manager = DataManagement()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            data_manager.insert_data(key, value)
        elif choice == '2':
            key = input("Enter key to update: ")
            new_value = input("Enter new value: ")
            data_manager.update_data(key, new_value)
        elif choice == '3':
            key = input("Enter key to search: ")
            data_manager.search_data(key)
        elif choice == '4':
            key = input("Enter key to delete: ")
            data_manager.delete_data(key)
        elif choice == '5':
            data_manager.view_all_data()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()