import csv
import pandas as pd

def search():
    global lib
    # Create search query
    search = input("Search: ").lower()
    query = []
    for i, book in enumerate(lib.loc[:, 'Title']):
        if search in book.lower():
            query.append((i, lib.loc[i, 'Title'], lib.loc[i, 'Obtained Status'], lib.loc[i, 'Read Status']))
            print(f'# {i}')
            print(f'Title: {lib.loc[i, 'Title']}')
            print(f'Obtained Status: {lib.loc[i, 'Obtained Status']}')
            print(f'Read Status: {lib.loc[i, 'Read Status']}\n')

def change_status():
    global lib
    book = int(input("Choose which book: # "))
    print(lib.loc[book])

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


# Pull library
lib = pd.read_csv('tables.csv')



# TODO: Write changes to csv
# TODO: Make search function and update status function