from utils import Library
from data import save_data
from menu_flow_control import menu_flow


def main():
    library = Library()
    menu_flow({
        'New': library.create_new_book,
        'View': library.view_all_books,
        'Graphs': library.view_graphs(),
        'Update': library.update_library(),
        'Delete': library.delete_book,
        'Save': lambda: save_data(library.df, verbose=True)
    })
    save_data(library.df)


if __name__ == "__main__":
    main()
