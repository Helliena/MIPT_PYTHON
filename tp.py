import sqlite3

tp_themes = []
tp_links = []

with sqlite3.connect('tp_database.sqlite') as db:
    cursor = db.cursor()
    query_data = """ SELECT theme, callback, link FROM themes """
    cursor.execute(query_data)
    for i in cursor:
        tp_themes.append((i[0], i[1]))
        tp_links.append(i[2])
    db.commit()
  
def get_link_tp(theme):
    if theme == "Patterns":
        return tp_links[0]
 