import sqlite3

oop_themes = []
oop_links = []

with sqlite3.connect('oop_database.sqlite') as db:
    cursor = db.cursor()
    query_data = """ SELECT theme, callback, link FROM themes """
    cursor.execute(query_data)
    for i in cursor:
        oop_themes.append((i[0], i[1]))
        oop_links.append(i[2])
    db.commit()

def get_link_oop(theme):
    if theme == "Introduction":
        return oop_links[0]
    elif theme == "Behavior":
        return oop_links[1]
    elif theme == "Types":
        return oop_links[2]
