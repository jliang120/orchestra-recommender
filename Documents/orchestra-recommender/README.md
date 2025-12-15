# Orchestra Repertoire Recommendation Engine

An orchestra repertorie recommendation system that helps orchestra conductors select and program repertoire based on instrumentation, skill level, duration, and genre considerations.

## Motivation

While serving as principal double bassist at Northeastern University Orchestra, I observed our conductor spending hours researching and deliberating over repertoire selection for each concert. The process involved manually cross-referencing piece difficulty levels, instrumentation requirements, duration constraints, and thematic coherence—all while trying to balance educational value with audience appeal.

Recognizing this as a solvable problem, I built this recommendation engine to streamline the repertoire selection process. The tool helps conductors quickly identify pieces that match their orchestra's skill level and available instrumentation, while suggesting balanced programs that work within typical concert timeframes.

What started as a solution for my own orchestra has evolved into a comprehensive database of 30+ works that can help any conductor make informed, efficient programming decisions.

## Features

- **Interactive Program Builder**: Answer 4 questions to get customized concert program recommendations
- **Comprehensive Database**: 30+ orchestral works spanning Classical to Contemporary periods
- **Smart Filtering**: Filter by difficulty level (1-5), duration, period, and instrumentation
- **Multiple Program Styles**: Traditional (Overture + Symphony), Thematic (same composer/period), All Symphonies, or Audience Favorites
- **Detailed Instrumentation**: Complete instrumentation requirements for each piece including solo passages
- **Flexible Recommendations**: Automatically expands search if strict criteria yield limited results

## Database Contents

The database includes 30 major orchestral works spanning 200+ years:

**Classical Era (3 pieces)**
- Mozart: Symphonies No. 40 & 41 "Jupiter"
- Beethoven: Symphony No. 5

**Romantic Era (13 pieces)**
- Brahms: Symphonies No. 1, 2, 4
- Tchaikovsky: Symphonies No. 5, 6 "Pathétique"; Romeo & Juliet Overture
- Dvořák: Symphonies No. 8, 9 "New World"
- Mendelssohn: Symphony No. 4 "Italian"
- Schubert: Symphony No. 8 "Unfinished"
- Bizet: Carmen Suite No. 1
- Rimsky-Korsakov: Scheherazade
- Mussorgsky/Ravel: Pictures at an Exhibition
- Rossini: William Tell Overture

**Late Romantic Era (3 pieces)**
- Mahler: Symphony No. 2 "Resurrection"
- Richard Strauss: Ein Heldenleben
- Sibelius: Symphony No. 2, Finlandia

**20th Century (9 pieces)**
- Shostakovich: Symphony No. 5
- Bartók: Concerto for Orchestra
- Copland: Appalachian Spring Suite
- Bernstein: West Side Story Symphonic Dances
- Prokofiev: Romeo & Juliet Suite No. 2
- Holst: The Planets
- Kodály: Dances of Galánta
- Khachaturian: Spartacus Adagio

**Modern (2 pieces)**
- Stravinsky: The Rite of Spring

Difficulty ranges from 3 (student/youth level) to 5 (professional level)

## Tech Stack

- **Python 3** - Core programming language
- **SQLite** - Lightweight relational database for storing repertoire and instrumentation data
- **Pandas** - Data manipulation and querying
- **Object-Oriented Design** - Modular `OrchestraRecommender` class for extensibility
