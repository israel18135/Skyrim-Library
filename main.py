import csv
import pandas as pd

def search():
    global lib
    # Create search query
    search = input("Search: ").lower()
    matches = 0
    for i, book in enumerate(lib.loc[:, 'Title']):
        if search in book.lower():
            print(f'{lib.loc[i]}\n')
            matches += 1

    # Request to try again if no matches are found
    if matches == 0:
        print('No matches found.  Please try again.')
        return True
    
    return False

def change_status():
    global lib
    book = input("Choose which book: # ")
    
    if book.isalnum():
        print(lib.loc[book])

    else:
        return False

    status = int(input("(1) Obtained Status or (2) Read Status: "))
    if status == 1:
        if lib.loc[book, 'Obtained Status'] == 'Unobtained':
            lib.loc[book, 'Obtained Status'] = 'Obtained'
        else:
            lib.loc[book, 'Obtained Status'] = 'Unobtained'

    if status == 2:
        if lib.loc[book, 'Read Status'] == 'Not Read':
            lib.loc[book, 'Read Status'] = 'Read'

        else:
            lib.loc[book, 'Read Status'] = 'Not Read'

    print(lib.loc[book])
    lib.to_csv('tables.csv', index=False)
    print("Update complete\n")
    return input("Change another status? (boolean variable value): ")


# Pull library
lib = pd.read_csv('tables.csv')

searching = True
updating = True
while searching:
    searching = search() # Returns false if searching is done
    if not searching:
        while updating:
            updating = change_status()
        searching = input("Search again? (boolean variable value): ")