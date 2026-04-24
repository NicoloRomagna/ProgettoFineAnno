import sqlite3
import os

if not os.path.exists('instance'):
    os.makedirs('instance')

db_path = os.path.join('instance', 'lego.sqlite')

connection = sqlite3.connect(db_path)

with open('app/schema.sql') as f:
    connection.executescript(f.read())

print("Database creato:", db_path)
connection.close()