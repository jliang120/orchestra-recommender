import sqlite3
import pandas as pd

conn = sqlite3.connect('data/orchestra_repertoire.db')

# See all pieces
print("=" * 60)
print("PIECES IN DATABASE:")
print("=" * 60)
pieces = pd.read_sql_query("SELECT * FROM pieces", conn)
print(pieces[['piece_id', 'title', 'composer', 'difficulty_overall', 'popularity_score']])

print("\n" + "=" * 60)
print("INSTRUMENTATION FOR BEETHOVEN 5:")
print("=" * 60)
instrumentation = pd.read_sql_query("""
    SELECT instrument, quantity_required, difficulty_rating, has_solo
    FROM instrumentation 
    WHERE piece_id = 1
    ORDER BY instrument
""", conn)
print(instrumentation)

conn.close()