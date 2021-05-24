import sqlite3

dsa_themes = []
dsa_links = []

with sqlite3.connect('data/dsa_database.sqlite') as db:
    cursor = db.cursor()
    query_data = """ SELECT theme, callback, link FROM themes """
    cursor.execute(query_data)
    for i in cursor:
        dsa_themes.append((i[0], i[1]))
        dsa_links.append(i[2])
    db.commit()


def get_link_dsa(theme):
    if theme == "FindDividers":
        return dsa_links[0]
    elif theme == "BinSearch":
        return dsa_links[1]
    elif theme == "BinPow":
        return dsa_links[2]
    elif theme == "TwoPointers":
        return dsa_links[3]
    elif theme == "CountSort":
        return dsa_links[4]
    elif theme == "MergeSort":
        return dsa_links[5]
