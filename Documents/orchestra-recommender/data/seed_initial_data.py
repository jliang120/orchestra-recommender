import sqlite3

def add_piece(conn, title, composer, year, period, duration, difficulty, popularity, notes=""):
    """Add a piece to the database and return its ID"""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pieces (title, composer, year_composed, period, duration_minutes, 
                          difficulty_overall, popularity_score, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, composer, year, period, duration, difficulty, popularity, notes))
    conn.commit()
    return cursor.lastrowid

def add_instrumentation(conn, piece_id, instrument, quantity, difficulty, has_solo=False):
    """Add instrumentation requirements for a piece"""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO instrumentation (piece_id, instrument, quantity_required, 
                                     difficulty_rating, has_solo)
        VALUES (?, ?, ?, ?, ?)
    ''', (piece_id, instrument, quantity, difficulty, has_solo))
    conn.commit()

def seed_data():
    conn = sqlite3.connect('data/orchestra_repertoire.db')
    
    # Piece 1: Beethoven Symphony No. 5
    print("Adding Beethoven 5...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 5 in C minor, Op. 67",
        composer="Ludwig van Beethoven",
        year=1808,
        period="Classical/Romantic",
        duration=33,
        difficulty=4,
        popularity=5,
        notes="Iconic opening motif. Challenging rhythmic precision for all sections."
    )
    
    instruments = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 2, 4, False),
        ("Trumpet", 2, 4, False),
        ("Timpani", 1, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)
    
    # Piece 2: Dvorak New World Symphony
    print("Adding Dvorak New World...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 9 in E minor, Op. 95 'From the New World'",
        composer="Antonín Dvořák",
        year=1893,
        period="Romantic",
        duration=40,
        difficulty=4,
        popularity=5,
        notes="Famous Largo movement. English horn solo in second movement."
    )
    
    instruments_dvorak = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("English Horn", 1, 4, True),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 2, 4, False),
        ("Trombone", 3, 4, False),
        ("Timpani", 1, 4, False),
        ("Triangle", 1, 2, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 3, False),
    ]
    
    for instrument, qty, diff, solo in instruments_dvorak:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)
    
    # Piece 3: Mahler Symphony No. 2 "Resurrection"
    print("Adding Mahler 2...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 2 in C minor 'Resurrection'",
        composer="Gustav Mahler",
        year=1894,
        period="Late Romantic",
        duration=85,
        difficulty=5,
        popularity=4,
        notes="Massive forces. Requires chorus and soloists. Offstage brass. Extremely long and demanding."
    )
    
    instruments_mahler2 = [
        ("Piccolo", 2, 5, False),
        ("Flute", 4, 5, False),
        ("Oboe", 4, 5, False),
        ("English Horn", 1, 5, False),
        ("Clarinet", 3, 5, False),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 4, 5, False),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 10, 5, False),
        ("Trumpet", 10, 5, False),
        ("Trombone", 4, 5, False),
        ("Tuba", 1, 5, False),
        ("Timpani", 2, 5, False),
        ("Percussion", 4, 5, False),
        ("Harp", 2, 4, False),
        ("Organ", 1, 4, False),
        ("Violin I", 20, 5, False),
        ("Violin II", 18, 5, False),
        ("Viola", 14, 5, False),
        ("Cello", 12, 5, False),
        ("Double Bass", 10, 5, False),
        ("Soprano", 1, 5, True),
        ("Alto", 1, 5, True),
        ("Chorus", 100, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_mahler2:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 4: Stravinsky The Rite of Spring
    print("Adding Rite of Spring...")
    piece_id = add_piece(
        conn,
        title="The Rite of Spring",
        composer="Igor Stravinsky",
        year=1913,
        period="Modern",
        duration=35,
        difficulty=5,
        popularity=5,
        notes="Revolutionary rhythms and orchestration. Extremely challenging for all sections. Infamous 1913 premiere."
    )
    
    instruments_rite = [
        ("Piccolo", 1, 5, False),
        ("Flute", 3, 5, False),
        ("Alto Flute", 1, 5, False),
        ("Oboe", 4, 5, False),
        ("English Horn", 1, 5, False),
        ("Clarinet", 3, 5, False),
        ("Bass Clarinet", 2, 5, False),
        ("Bassoon", 4, 5, False),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 8, 5, False),
        ("Trumpet", 5, 5, False),
        ("Bass Trumpet", 1, 5, False),
        ("Trombone", 3, 5, False),
        ("Tuba", 2, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 5, 5, False),
        ("Violin I", 16, 5, False),
        ("Violin II", 16, 5, False),
        ("Viola", 12, 5, False),
        ("Cello", 10, 5, False),
        ("Double Bass", 8, 5, False),
    ]
    
    for instrument, qty, diff, solo in instruments_rite:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 5: Prokofiev Romeo and Juliet Suite
    print("Adding Prokofiev Romeo and Juliet...")
    piece_id = add_piece(
        conn,
        title="Romeo and Juliet Suite No. 2, Op. 64",
        composer="Sergei Prokofiev",
        year=1936,
        period="20th Century",
        duration=30,
        difficulty=5,
        popularity=4,
        notes="Ballet suite with famous movements. Dance of the Knights, Balcony Scene. Technically demanding."
    )
    
    instruments_prokofiev = [
        ("Piccolo", 1, 4, False),
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("English Horn", 1, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bass Clarinet", 1, 4, False),
        ("Bassoon", 2, 4, False),
        ("Contrabassoon", 1, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 3, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Percussion", 3, 4, False),
        ("Harp", 1, 4, False),
        ("Piano", 1, 4, False),
        ("Violin I", 16, 5, False),
        ("Violin II", 14, 5, False),
        ("Viola", 12, 5, False),
        ("Cello", 10, 5, False),
        ("Double Bass", 8, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_prokofiev:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 6: Tchaikovsky Romeo and Juliet Fantasy Overture
    print("Adding Tchaikovsky Romeo and Juliet...")
    piece_id = add_piece(
        conn,
        title="Romeo and Juliet Fantasy Overture",
        composer="Pyotr Ilyich Tchaikovsky",
        year=1869,
        period="Romantic",
        duration=20,
        difficulty=4,
        popularity=5,
        notes="Famous love theme. Dramatic conflict sections. Popular concert opener."
    )
    
    instruments_tchaik_rj = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("English Horn", 1, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 2, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Cymbals", 1, 3, False),
        ("Bass Drum", 1, 3, False),
        ("Harp", 1, 3, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_tchaik_rj:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 7: Sibelius Symphony No. 2
    print("Adding Sibelius 2...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 2 in D major, Op. 43",
        composer="Jean Sibelius",
        year=1902,
        period="Late Romantic",
        duration=43,
        difficulty=4,
        popularity=5,
        notes="Triumphant finale. Nordic character. Popular symphony with audiences."
    )
    
    instruments_sibelius = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 3, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_sibelius:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 8: Richard Strauss Ein Heldenleben
    print("Adding Ein Heldenleben...")
    piece_id = add_piece(
        conn,
        title="Ein Heldenleben (A Hero's Life), Op. 40",
        composer="Richard Strauss",
        year=1898,
        period="Late Romantic",
        duration=45,
        difficulty=5,
        popularity=4,
        notes="Massive tone poem. Extensive solo violin representing the hero's companion. Very challenging for all."
    )
    
    instruments_heldenleben = [
        ("Piccolo", 1, 5, False),
        ("Flute", 3, 5, False),
        ("Oboe", 3, 5, True),
        ("English Horn", 1, 5, False),
        ("Clarinet", 3, 5, False),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 3, 5, False),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 8, 5, True),
        ("Trumpet", 5, 5, False),
        ("Trombone", 3, 5, False),
        ("Tuba", 1, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 4, 5, False),
        ("Harp", 2, 4, False),
        ("Violin I", 16, 5, True),
        ("Violin II", 16, 5, False),
        ("Viola", 12, 5, False),
        ("Cello", 10, 5, False),
        ("Double Bass", 8, 5, False),
    ]
    
    for instrument, qty, diff, solo in instruments_heldenleben:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 9: Shostakovich Symphony No. 5
    print("Adding Shostakovich 5...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 5 in D minor, Op. 47",
        composer="Dmitri Shostakovich",
        year=1937,
        period="20th Century",
        duration=45,
        difficulty=5,
        popularity=5,
        notes="'A Soviet artist's response to just criticism.' Powerful and emotionally intense. Challenging rhythms."
    )
    
    instruments_shosty5 = [
        ("Piccolo", 1, 5, False),
        ("Flute", 2, 5, False),
        ("Oboe", 2, 5, False),
        ("Clarinet", 2, 5, False),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 2, 5, False),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 4, 5, False),
        ("Trumpet", 3, 5, False),
        ("Trombone", 3, 5, False),
        ("Tuba", 1, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 4, 5, False),
        ("Harp", 1, 4, False),
        ("Piano", 1, 4, False),
        ("Violin I", 16, 5, False),
        ("Violin II", 14, 5, False),
        ("Viola", 12, 5, False),
        ("Cello", 10, 5, False),
        ("Double Bass", 8, 5, False),
    ]
    
    for instrument, qty, diff, solo in instruments_shosty5:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 10: Brahms Symphony No. 2
    print("Adding Brahms 2...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 2 in D major, Op. 73",
        composer="Johannes Brahms",
        year=1877,
        period="Romantic",
        duration=42,
        difficulty=4,
        popularity=5,
        notes="Pastoral and lyrical. Called 'Brahms' Pastoral'. Beautiful horn writing. Challenging ensemble precision."
    )
    
    instruments_brahms2 = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Contrabassoon", 1, 4, False),
        ("Horn", 4, 4, True),
        ("Trumpet", 2, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_brahms2:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 11: Bernstein West Side Story Symphonic Dances
    print("Adding West Side Story...")
    piece_id = add_piece(
        conn,
        title="Symphonic Dances from West Side Story",
        composer="Leonard Bernstein",
        year=1961,
        period="20th Century",
        duration=24,
        difficulty=5,
        popularity=5,
        notes="Broadway meets symphony. Jazz and Latin rhythms. Extremely popular with audiences. Technically demanding."
    )
    
    instruments_wss = [
        ("Piccolo", 1, 5, False),
        ("Flute", 2, 5, False),
        ("Oboe", 2, 5, False),
        ("Clarinet", 2, 5, False),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 2, 5, False),
        ("Horn", 4, 5, False),
        ("Trumpet", 3, 5, False),
        ("Trombone", 3, 5, False),
        ("Tuba", 1, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 5, 5, False),
        ("Piano", 1, 5, False),
        ("Violin I", 14, 5, False),
        ("Violin II", 12, 5, False),
        ("Viola", 10, 5, False),
        ("Cello", 8, 5, False),
        ("Double Bass", 6, 5, False),
    ]
    
    for instrument, qty, diff, solo in instruments_wss:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 12: Dvořák Symphony No. 8
    print("Adding Dvorak 8...")
    piece_id = add_piece(
        conn,
        title="Symphony No. 8 in G major, Op. 88",
        composer="Antonín Dvořák",
        year=1889,
        period="Romantic",
        duration=37,
        difficulty=4,
        popularity=4,
        notes="Czech character, nature themes. Lyrical and optimistic. Beautiful flute passages."
    )
    
    instruments_dvorak8 = [
        ("Piccolo", 1, 4, False),
        ("Flute", 2, 4, True),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 2, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_dvorak8:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 13: Kodály Dances of Galánta
    print("Adding Kodály Dances of Galánta...")
    piece_id = add_piece(
        conn,
        title="Dances of Galánta",
        composer="Zoltán Kodály",
        year=1933,
        period="20th Century",
        duration=16,
        difficulty=4,
        popularity=3,
        notes="Hungarian folk dances. Colorful orchestration. Clarinet featured prominently. Exciting closer."
    )
    
    instruments_kodaly = [
        ("Piccolo", 1, 4, False),
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, True),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 2, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Percussion", 3, 4, False),
        ("Harp", 1, 3, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_kodaly:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 14: Copland Appalachian Spring Suite
    print("Adding Copland Appalachian Spring...")
    piece_id = add_piece(
        conn,
        title="Appalachian Spring Suite",
        composer="Aaron Copland",
        year=1944,
        period="20th Century",
        duration=25,
        difficulty=4,
        popularity=5,
        notes="Quintessentially American. Simple Gift variations. Pastoral and optimistic. Very audience-friendly."
    )
    
    instruments_copland = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 2, 4, False),
        ("Trumpet", 2, 4, False),
        ("Trombone", 2, 4, False),
        ("Timpani", 1, 4, False),
        ("Percussion", 2, 4, False),
        ("Harp", 1, 3, False),
        ("Piano", 1, 4, False),
        ("Violin I", 12, 4, False),
        ("Violin II", 10, 4, False),
        ("Viola", 8, 4, False),
        ("Cello", 6, 4, False),
        ("Double Bass", 4, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_copland:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 15: Bartók Concerto for Orchestra
    print("Adding Bartók Concerto for Orchestra...")
    piece_id = add_piece(
        conn,
        title="Concerto for Orchestra",
        composer="Béla Bartók",
        year=1943,
        period="20th Century",
        duration=38,
        difficulty=5,
        popularity=5,
        notes="Showcases every section. Folk influences. 'Game of Pairs' movement. Extremely popular and challenging."
    )
    
    instruments_bartok = [
        ("Piccolo", 1, 5, False),
        ("Flute", 3, 5, False),
        ("Oboe", 3, 5, True),
        ("English Horn", 1, 5, False),
        ("Clarinet", 3, 5, True),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 3, 5, True),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 4, 5, True),
        ("Trumpet", 3, 5, True),
        ("Trombone", 3, 5, True),
        ("Tuba", 1, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 4, 5, False),
        ("Harp", 1, 4, False),
        ("Violin I", 16, 5, False),
        ("Violin II", 14, 5, False),
        ("Viola", 12, 5, False),
        ("Cello", 10, 5, False),
        ("Double Bass", 8, 5, False),
    ]
    
    for instrument, qty, diff, solo in instruments_bartok:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 16: Khachaturian Adagio from Spartacus
    print("Adding Khachaturian Spartacus Adagio...")
    piece_id = add_piece(
        conn,
        title="Adagio of Spartacus and Phrygia from Spartacus",
        composer="Aram Khachaturian",
        year=1954,
        period="20th Century",
        duration=9,
        difficulty=4,
        popularity=4,
        notes="Heartbreaking ballet adagio. Lyrical and emotional. Famous from The Onedin Line TV series."
    )
    
    instruments_khach = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, True),
        ("Trumpet", 2, 3, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 3, False),
        ("Timpani", 1, 3, False),
        ("Percussion", 2, 3, False),
        ("Harp", 1, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 3, False),
    ]
    
    for instrument, qty, diff, solo in instruments_khach:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 17: Sibelius Finlandia
    print("Adding Sibelius Finlandia...")
    piece_id = add_piece(
        conn,
        title="Finlandia, Op. 26",
        composer="Jean Sibelius",
        year=1899,
        period="Late Romantic",
        duration=8,
        difficulty=4,
        popularity=5,
        notes="Finnish national tone poem. Patriotic hymn theme. Powerful and stirring. Popular concert closer."
    )
    
    instruments_finlandia = [
        ("Flute", 2, 4, False),
        ("Oboe", 2, 4, False),
        ("Clarinet", 2, 4, False),
        ("Bassoon", 2, 4, False),
        ("Horn", 4, 4, False),
        ("Trumpet", 3, 4, False),
        ("Trombone", 3, 4, False),
        ("Tuba", 1, 4, False),
        ("Timpani", 1, 4, False),
        ("Percussion", 2, 4, False),
        ("Violin I", 14, 4, False),
        ("Violin II", 12, 4, False),
        ("Viola", 10, 4, False),
        ("Cello", 8, 4, False),
        ("Double Bass", 6, 4, False),
    ]
    
    for instrument, qty, diff, solo in instruments_finlandia:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    # Piece 18: Holst The Planets Suite
    print("Adding Holst The Planets...")
    piece_id = add_piece(
        conn,
        title="The Planets, Op. 32",
        composer="Gustav Holst",
        year=1916,
        period="20th Century",
        duration=50,
        difficulty=5,
        popularity=5,
        notes="Seven-movement suite. Mars is iconic. Jupiter very popular. Requires huge forces and offstage chorus."
    )
    
    instruments_planets = [
        ("Piccolo", 2, 5, False),
        ("Flute", 4, 5, False),
        ("Oboe", 3, 5, False),
        ("English Horn", 1, 5, False),
        ("Clarinet", 3, 5, False),
        ("Bass Clarinet", 1, 5, False),
        ("Bassoon", 3, 5, False),
        ("Contrabassoon", 1, 5, False),
        ("Horn", 6, 5, False),
        ("Trumpet", 4, 5, False),
        ("Trombone", 3, 5, False),
        ("Tuba", 2, 5, False),
        ("Timpani", 1, 5, False),
        ("Percussion", 6, 5, False),
        ("Harp", 2, 5, False),
        ("Organ", 1, 4, False),
        ("Celesta", 1, 4, False),
        ("Violin I", 16, 5, False),
        ("Violin II", 16, 5, False),
        ("Viola", 14, 5, False),
        ("Cello", 12, 5, False),
        ("Double Bass", 10, 5, False),
        ("Female Chorus", 40, 3, False),
    ]
    
    for instrument, qty, diff, solo in instruments_planets:
        add_instrumentation(conn, piece_id, instrument, qty, diff, solo)

    conn.close()
    print("\n✅ Added 13 total pieces successfully!")

if __name__ == "__main__":
    seed_data()