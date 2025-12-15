import sqlite3
import pandas as pd
from recommender import OrchestraRecommender

def get_user_input():
    """Ask user questions about their concert needs"""
    print("\n" + "="*70)
    print("ORCHESTRA REPERTOIRE PROGRAM BUILDER")
    print("="*70)
    print("\nLet's build your perfect concert program!\n")
    
    # Question 1: Orchestra skill level
    print("1. What is your orchestra's skill level?")
    print("   1 - Student/Youth Orchestra (Difficulty 3-4)")
    print("   2 - Community/Amateur Orchestra (Difficulty 4)")
    print("   3 - Semi-Professional Orchestra (Difficulty 4-5)")
    print("   4 - Professional Orchestra (Difficulty 5)")
    
    while True:
        try:
            skill = int(input("\nEnter choice (1-4): "))
            if skill in [1, 2, 3, 4]:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Map skill to difficulty
    difficulty_map = {1: 4, 2: 4, 3: 5, 4: 5}
    max_difficulty = difficulty_map[skill]
    
    # Question 2: Concert duration
    print("\n2. What is your target concert duration?")
    print("   1 - Short concert (45-60 minutes)")
    print("   2 - Standard concert (75-90 minutes)")
    print("   3 - Long concert (90-120 minutes)")
    
    while True:
        try:
            duration_choice = int(input("\nEnter choice (1-3): "))
            if duration_choice in [1, 2, 3]:
                break
            print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")
    
    duration_map = {1: (45, 60), 2: (75, 90), 3: (90, 120)}
    target_min, target_max = duration_map[duration_choice]
    
    # Question 3: Period preference
    print("\n3. Do you have a period preference?")
    print("   1 - Classical/Romantic")
    print("   2 - Late Romantic")
    print("   3 - 20th Century")
    print("   4 - Modern/Contemporary")
    print("   5 - Mixed (no preference)")
    
    while True:
        try:
            period_choice = int(input("\nEnter choice (1-5): "))
            if period_choice in [1, 2, 3, 4, 5]:
                break
            print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    period_map = {
        1: "Classical/Romantic",
        2: "Late Romantic", 
        3: "20th Century",
        4: "Modern",
        5: None
    }
    preferred_period = period_map[period_choice]
    
    # Question 4: Concert theme/structure
    print("\n4. What concert structure do you prefer?")
    print("   1 - Traditional (Overture + Concerto + Symphony)")
    print("   2 - All Symphonies")
    print("   3 - Thematic (all same composer or period)")
    print("   4 - Audience Favorites (popular pieces)")
    
    while True:
        try:
            structure = int(input("\nEnter choice (1-4): "))
            if structure in [1, 2, 3, 4]:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    return {
        'max_difficulty': max_difficulty,
        'target_min': target_min,
        'target_max': target_max,
        'preferred_period': preferred_period,
        'structure': structure,
        'skill_level': skill
    }

def build_program(preferences):
    """Build a program based on user preferences"""
    conn = sqlite3.connect('data/orchestra_repertoire.db')
    
    # Get all viable pieces
    query = '''
        SELECT piece_id, title, composer, period, duration_minutes, 
               difficulty_overall, popularity_score, notes
        FROM pieces
        WHERE difficulty_overall <= ?
    '''
    params = [preferences['max_difficulty']]
    
    if preferences['preferred_period']:
        query += ' AND period = ?'
        params.append(preferences['preferred_period'])
    
    query += ' ORDER BY popularity_score DESC, duration_minutes'
    
    pieces = pd.read_sql_query(query, conn, params=params)
    conn.close()
    
    if pieces.empty:
        return None
    
    programs = []
    target_min = preferences['target_min']
    target_max = preferences['target_max']
    structure = preferences['structure']
    
    # Build programs based on structure preference
    if structure == 1:  # Traditional: Overture + Symphony
        short_pieces = pieces[pieces['duration_minutes'] <= 25]
        long_pieces = pieces[pieces['duration_minutes'] >= 30]
        
        for _, opener in short_pieces.head(3).iterrows():
            for _, closer in long_pieces.head(3).iterrows():
                total = opener['duration_minutes'] + closer['duration_minutes']
                if target_min <= total <= target_max:
                    programs.append({
                        'pieces': [opener, closer],
                        'total_duration': total,
                        'structure': 'Overture + Symphony',
                        'avg_difficulty': (opener['difficulty_overall'] + closer['difficulty_overall']) / 2
                    })
    
    elif structure == 2:  # All Symphonies (long pieces)
        long_pieces = pieces[pieces['duration_minutes'] >= 30]
        
        for _, piece1 in long_pieces.head(3).iterrows():
            for _, piece2 in long_pieces.head(3).iterrows():
                if piece1['piece_id'] != piece2['piece_id']:
                    total = piece1['duration_minutes'] + piece2['duration_minutes']
                    if target_min <= total <= target_max:
                        programs.append({
                            'pieces': [piece1, piece2],
                            'total_duration': total,
                            'structure': 'Two Major Works',
                            'avg_difficulty': (piece1['difficulty_overall'] + piece2['difficulty_overall']) / 2
                        })
    
    elif structure == 3:  # Thematic (same period or composer)
        # Group by composer
        for composer in pieces['composer'].unique()[:5]:
            composer_pieces = pieces[pieces['composer'] == composer]
            if len(composer_pieces) >= 2:
                total = composer_pieces.iloc[0]['duration_minutes'] + composer_pieces.iloc[1]['duration_minutes']
                if target_min <= total <= target_max:
                    programs.append({
                        'pieces': [composer_pieces.iloc[0], composer_pieces.iloc[1]],
                        'total_duration': total,
                        'structure': f'All {composer}',
                        'avg_difficulty': composer_pieces['difficulty_overall'].mean()
                    })
    
    elif structure == 4:  # Audience Favorites
        popular_pieces = pieces.nlargest(10, 'popularity_score')
        
        for _, piece1 in popular_pieces.head(5).iterrows():
            for _, piece2 in popular_pieces.head(5).iterrows():
                if piece1['piece_id'] != piece2['piece_id']:
                    total = piece1['duration_minutes'] + piece2['duration_minutes']
                    if target_min <= total <= target_max:
                        programs.append({
                            'pieces': [piece1, piece2],
                            'total_duration': total,
                            'structure': 'Audience Favorites',
                            'avg_difficulty': (piece1['difficulty_overall'] + piece2['difficulty_overall']) / 2
                        })
    
    # Sort programs by how close they are to target
    target_avg = (target_min + target_max) / 2
    for program in programs:
        program['distance'] = abs(program['total_duration'] - target_avg)
    
    programs.sort(key=lambda x: x['distance'])
    
    return programs[:5]  # Return top 5 programs

def display_programs(programs, preferences):
    """Display the recommended programs"""
    if not programs:
        print("\n❌ Sorry, couldn't find any programs matching your criteria.")
        print("Try adjusting your difficulty or duration requirements.")
        return
    
    print("\n" + "="*70)
    print("RECOMMENDED CONCERT PROGRAMS")
    print("="*70)
    
    skill_names = {1: "Student/Youth", 2: "Community", 3: "Semi-Professional", 4: "Professional"}
    print(f"\nFor: {skill_names[preferences['skill_level']]} Orchestra")
    print(f"Target Duration: {preferences['target_min']}-{preferences['target_max']} minutes")
    if preferences['preferred_period']:
        print(f"Period: {preferences['preferred_period']}")
    
    for i, program in enumerate(programs, 1):
        print(f"\n{'-'*70}")
        print(f"PROGRAM {i}: {program['structure']}")
        print(f"Total Duration: {program['total_duration']} minutes")
        print(f"Average Difficulty: {program['avg_difficulty']:.1f}/5")
        print(f"{'-'*70}")
        
        for j, piece in enumerate(program['pieces'], 1):
            print(f"\n{j}. {piece['composer']}")
            print(f"   {piece['title']}")
            print(f"   Duration: {piece['duration_minutes']} min | Difficulty: {piece['difficulty_overall']}/5")
            if piece['notes']:
                print(f"   Notes: {piece['notes']}")
    
    # Ask if user wants to see instrumentation
    print("\n" + "="*70)
    while True:
        choice = input("\nWould you like to see instrumentation for any piece? (y/n): ").lower()
        if choice in ['y', 'n']:
            break
    
    if choice == 'y':
        recommender = OrchestraRecommender()
        while True:
            try:
                program_num = int(input(f"Which program (1-{len(programs)}): "))
                if 1 <= program_num <= len(programs):
                    piece_num = int(input(f"Which piece (1-{len(programs[program_num-1]['pieces'])}): "))
                    if 1 <= piece_num <= len(programs[program_num-1]['pieces']):
                        selected_piece = programs[program_num-1]['pieces'][piece_num-1]
                        print(f"\nInstrumentation for {selected_piece['title']}:")
                        print("-"*70)
                        inst = recommender.get_piece_instrumentation(selected_piece['piece_id'])
                        print(inst.to_string(index=False))
                        break
            except ValueError:
                print("Please enter valid numbers.")
            
            again = input("\nSee another? (y/n): ").lower()
            if again != 'y':
                break

def main():
    # Get user preferences
    preferences = get_user_input()
    
    # Build programs
    print("\n🎵 Building your programs...")
    programs = build_program(preferences)
    
    # Display results
    display_programs(programs, preferences)
    
    print("\n" + "="*70)
    print("Thank you for using the Orchestra Repertoire Recommender!")
    print("="*70)

if __name__ == "__main__":
    main()