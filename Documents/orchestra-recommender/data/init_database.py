import sqlite3

def create_database():
    conn = sqlite3.connect('data/orchestra_repertoire.db')
    cursor = conn.cursor()
    
    # Pieces table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pieces (
            piece_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            composer TEXT NOT NULL,
            year_composed INTEGER,
            period TEXT,
            duration_minutes INTEGER,
            difficulty_overall INTEGER,
            popularity_score INTEGER,
            notes TEXT
        )
    ''')
    
    # Instrumentation table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instrumentation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            piece_id INTEGER,
            instrument TEXT NOT NULL,
            quantity_required INTEGER,
            difficulty_rating INTEGER,
            has_solo BOOLEAN,
            FOREIGN KEY (piece_id) REFERENCES pieces(piece_id)
        )
    ''')
    
    # Performances table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS performances (
            performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            orchestra TEXT,
            piece_id INTEGER,
            performance_date TEXT,
            season TEXT,
            concert_theme TEXT,
            FOREIGN KEY (piece_id) REFERENCES pieces(piece_id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database created successfully!")

if __name__ == "__main__":
    create_database()