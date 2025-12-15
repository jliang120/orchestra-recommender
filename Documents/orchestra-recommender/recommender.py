import sqlite3
import pandas as pd

class OrchestraRecommender:
    def __init__(self, db_path='data/orchestra_repertoire.db'):
        self.db_path = db_path
    
    def get_all_pieces(self):
        """Get all pieces from database"""
        conn = sqlite3.connect(self.db_path)
        pieces = pd.read_sql_query('''
            SELECT piece_id, title, composer, period, duration_minutes, 
                   difficulty_overall, popularity_score, notes
            FROM pieces
            ORDER BY composer
        ''', conn)
        conn.close()
        return pieces
    
    def filter_by_difficulty(self, max_difficulty):
        """Get pieces at or below a difficulty level"""
        conn = sqlite3.connect(self.db_path)
        pieces = pd.read_sql_query('''
            SELECT piece_id, title, composer, period, duration_minutes, 
                   difficulty_overall, popularity_score
            FROM pieces
            WHERE difficulty_overall <= ?
            ORDER BY popularity_score DESC, composer
        ''', conn, params=(max_difficulty,))
        conn.close()
        return pieces
    
    def filter_by_duration(self, min_duration=0, max_duration=100):
        """Get pieces within a duration range"""
        conn = sqlite3.connect(self.db_path)
        pieces = pd.read_sql_query('''
            SELECT piece_id, title, composer, period, duration_minutes, 
                   difficulty_overall, popularity_score
            FROM pieces
            WHERE duration_minutes >= ? AND duration_minutes <= ?
            ORDER BY duration_minutes
        ''', conn, params=(min_duration, max_duration))
        conn.close()
        return pieces
    
    def filter_by_period(self, period):
        """Get pieces from a specific period"""
        conn = sqlite3.connect(self.db_path)
        pieces = pd.read_sql_query('''
            SELECT piece_id, title, composer, period, duration_minutes, 
                   difficulty_overall, popularity_score
            FROM pieces
            WHERE period = ?
            ORDER BY composer
        ''', conn, params=(period,))
        conn.close()
        return pieces
    
    def get_piece_instrumentation(self, piece_id):
        """Get instrumentation details for a specific piece"""
        conn = sqlite3.connect(self.db_path)
        instrumentation = pd.read_sql_query('''
            SELECT instrument, quantity_required, difficulty_rating, has_solo
            FROM instrumentation
            WHERE piece_id = ?
            ORDER BY instrument
        ''', conn, params=(piece_id,))
        conn.close()
        return instrumentation
    
    def suggest_program(self, target_duration=90, max_difficulty=4):
        """Suggest a balanced concert program"""
        conn = sqlite3.connect(self.db_path)
        
        # Get all viable pieces
        pieces = pd.read_sql_query('''
            SELECT piece_id, title, composer, period, duration_minutes, 
                   difficulty_overall, popularity_score
            FROM pieces
            WHERE difficulty_overall <= ?
            ORDER BY popularity_score DESC
        ''', conn, params=(max_difficulty,))
        conn.close()
        
        if pieces.empty:
            return None
        
        # Simple greedy algorithm: pick popular pieces that fit duration
        programs = []
        
        # Try to build: Short opener (5-20 min) + Medium piece (20-40 min) + Long piece (30-50 min)
        short_pieces = pieces[pieces['duration_minutes'] <= 20]
        medium_pieces = pieces[(pieces['duration_minutes'] > 20) & (pieces['duration_minutes'] <= 40)]
        long_pieces = pieces[(pieces['duration_minutes'] > 30) & (pieces['duration_minutes'] <= 50)]
        
        # Build a few program options
        if not short_pieces.empty and not long_pieces.empty:
            opener = short_pieces.iloc[0]
            closer = long_pieces.iloc[0]
            
            programs.append({
                'total_duration': opener['duration_minutes'] + closer['duration_minutes'],
                'pieces': [opener, closer],
                'balance': 'Opener + Symphony'
            })
        
        if not medium_pieces.empty and not medium_pieces.empty:
            piece1 = medium_pieces.iloc[0]
            piece2 = medium_pieces.iloc[1] if len(medium_pieces) > 1 else medium_pieces.iloc[0]
            
            programs.append({
                'total_duration': piece1['duration_minutes'] + piece2['duration_minutes'],
                'pieces': [piece1, piece2],
                'balance': 'Two Medium Works'
            })
        
        return programs

def main():
    recommender = OrchestraRecommender()
    
    print("=" * 70)
    print("ORCHESTRA REPERTOIRE RECOMMENDATION ENGINE")
    print("=" * 70)
    
    # Example 1: Get all pieces at difficulty 4 or below
    print("\n1. PIECES FOR DIFFICULTY 4 OR BELOW:")
    print("-" * 70)
    easy_pieces = recommender.filter_by_difficulty(4)
    print(easy_pieces[['composer', 'title', 'difficulty_overall', 'duration_minutes']].to_string(index=False))
    
    # Example 2: Get short pieces (under 25 minutes)
    print("\n\n2. SHORT PIECES (UNDER 25 MINUTES):")
    print("-" * 70)
    short_pieces = recommender.filter_by_duration(0, 25)
    print(short_pieces[['composer', 'title', 'duration_minutes', 'difficulty_overall']].to_string(index=False))
    
    # Example 3: Get 20th Century pieces
    print("\n\n3. 20TH CENTURY REPERTOIRE:")
    print("-" * 70)
    modern_pieces = recommender.filter_by_period("20th Century")
    print(modern_pieces[['composer', 'title', 'duration_minutes']].to_string(index=False))
    
    # Example 4: Suggest a program
    print("\n\n4. SUGGESTED CONCERT PROGRAMS:")
    print("-" * 70)
    programs = recommender.suggest_program(target_duration=90, max_difficulty=4)
    
    if programs:
        for i, program in enumerate(programs, 1):
            print(f"\nProgram Option {i} ({program['balance']}):")
            print(f"Total Duration: {program['total_duration']} minutes")
            for piece in program['pieces']:
                print(f"  - {piece['composer']}: {piece['title']} ({piece['duration_minutes']} min)")
    
    # Example 5: Show instrumentation for a specific piece
    print("\n\n5. INSTRUMENTATION FOR BEETHOVEN 5:")
    print("-" * 70)
    beethoven_inst = recommender.get_piece_instrumentation(1)  # piece_id 1 is Beethoven 5
    print(beethoven_inst.to_string(index=False))

if __name__ == "__main__":
    main()