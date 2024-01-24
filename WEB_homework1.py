import os
from abc import ABC, abstractmethod
from addressbook import run as run_address_book
from NotebookD import Note, Record, Notebook, Tag
from file_sorter import Sorted


class ConsoleMenu(ABC):

    @abstractmethod
    def launch(self):
        pass


class AddressBookMenu(ConsoleMenu):

    def launch(self):
        print("Launching Address Book...")
        return_to_main_menu = run_address_book()
        if return_to_main_menu:
            input("Press Enter to return to the main menu...")


class NotebookMenu(ConsoleMenu):

    def launch(self):
        print("Launching Notebook...")

        notebook = Notebook()

        while True:
            print("**********************************************")
            print("Notebook Menu:")
            print("1. Add Note")
            print("2. Edit Note")
            print("3. Delete Note")
            print("4. List Notes")
            print("5. Search Notes by Tag")
            print("6. Save to File")
            print("7. Load from File")
            print("8. Back to Main Menu")
            print("**********************************************")

            choice = input("Enter your choice: ")

            if choice == '1':
                # Add Note
                note_text = input("Enter the note text: ")
                note = Note(note_text)
                notebook.add_record(Record(note))
                print("Note added successfully.")
            elif choice == '2':
                # Edit Note
                print("List of Notes:")
                notebook.list_records()
                note_index = int(input("Enter the index of the note to edit: "))
                if 0 <= note_index < len(notebook):
                    new_note_text = input("Enter the new note text: ")
                    notebook[note_index].note = new_note_text
                    print("Note edited successfully.")
                else:
                    print("Invalid note index. Please try again.")
            elif choice == '3':
                # Delete Note
                print("List of Notes:")
                notebook.list_records()
                note_index = int(input("Enter the index of the note to delete: "))
                if 0 <= note_index < len(notebook):
                    notebook.pop(note_index)
                    print("Note deleted successfully.")
                else:
                    print("Invalid note index. Please try again.")
            elif choice == '4':
                # List Notes
                print("List of Notes:")
                notebook.list_records()
            elif choice == '5':
                # Search Notes by Tag
                tag_to_search = input("Enter the tag to search for: ")
                matching_records = notebook.search_by_tag(Tag(tag_to_search))
                if matching_records:
                    print("Matching Notes:")
                    for i, record in enumerate(matching_records):
                        print(f"{i + 1}. {record.note}")
                else:
                    print("No matching notes found.")
            elif choice == '6':
                # Save to File
                file_name = input("Enter the file name to save to: ")
                notebook.save_to_file(file_name)
                print("Notes saved to file.")
            elif choice == '7':
                # Load from File
                file_name = input("Enter the file name to load from: ")
                notebook.load_from_file(file_name)
                print("Notes loaded from file.")
            elif choice == '8':
                # Back to Main Menu
                break
            else:
                print("Invalid choice. Please try again.")


class FileSorterMenu(ConsoleMenu):

    def launch(self):
        print("Launching File Sorter...")
        sorted_object = Sorted()
        sorted_object.run()


class MainMenu(ConsoleMenu):

    def launch(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen depending on the operating system

            print("**********************************************")
            print("Main Menu:")
            print("1. Launch Address Book")
            print("2. Launch Notebook")
            print("3. Launch File Sorter")
            print("4. Exit")
            print("**********************************************")

            choice = input("Enter your choice: ")

            if choice == '1':
                AddressBookMenu().launch()
            elif choice == '2':
                NotebookMenu().launch()
            elif choice == '3':
                FileSorterMenu().launch()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    MainMenu().launch()
