import os
import ctypes

def clear_wastebasket():
    try:
        if os.name == 'nt':
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
            print("Trash successfully emptied!")
        else:
            raise NotImplementedError("Automatic deletion of the recycle bin is not supported for this operating system.")
    except Exception as e:
        print(f"Error while emptying the Trash: {e}")

def clear_recent_items():
    try:
        if os.name == 'nt':
            recent_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Recent')
            for file in os.listdir(recent_folder):
                file_path = os.path.join(recent_folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting the file {file}: {e}")
            print("Recent successfully deleted!")
        else:
            raise NotImplementedError("Automatic deletion of Recent is not supported for this operating system.")
    except Exception as e:
        print(f"Error deleting Recent: {e}")

def clear_prefetch():
    try:
        if os.name == 'nt':
            prefetch_folder = os.path.join(os.environ['SystemRoot'], 'Prefetch')
            for file in os.listdir(prefetch_folder):
                file_path = os.path.join(prefetch_folder, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting the file {file}: {e}")
            print("Prefetch successfully emptied!")
        else:
            raise NotImplementedError("Automatic deletion of the prefetch folder is not supported for this operating system.")
    except Exception as e:
        print(f"Error while deleting the prefetch folder: {e}")

def main():
    print("-------------")
    print("A8ton_Cleaner")
    print("-------------")
    print("1 - Delete trash content")
    print("2 - Delete recent content")
    print("3 - Delete prefetch content")

    choice = input("Please select an option: ")

    if choice == '1':
        clear_wastebasket()
    elif choice == '2':
        clear_recent_items()
    elif choice == '3':
        clear_prefetch()
    else:
        print("Invalid input. Please enter '1', '2' or '3'.")

if __name__ == "__main__":
    main()
