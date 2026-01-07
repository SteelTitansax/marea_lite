import sqlite3
from constants import DATA_DIR
import random


def create_connection(db_file=f"{DATA_DIR}/database.db"):
    """
    Creates a connection to the SQLite database.
    
    Parameters:
        db_file (str): Path to the SQLite database file.
        
    Returns:
        sqlite3.Connection: Connection object if successful, None otherwise.
    """
    conn = None
    
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def display_technologies():
    """
    Searches information in the 'posts' table and return all technologies information.
    
    Returns:
        tuple: 
            - data (list of str): List of unique 'technology' values from the table.
    """

    cnxn = create_connection()
    data = []
    cur = cnxn.cursor()

    try:
        cur.execute('SELECT DISTINCT technology FROM posts')
        data = cur.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}", 'error')
        
    finally:
        cur.close()
        cnxn.close()

    return data

def insert_sqlite_information(technology,post):
    """
    Insert information in the 'posts' table.
    
    Returns:
        boolean value
    """
    random_id = random.randint(1000, 9999)

    cnxn = create_connection()
    data = []
    cur = cnxn.cursor()

    try:
        cur.execute("INSERT INTO posts (id, technology, post) VALUES (?, ?, ?)",
            (random_id, technology, post))
        cnxn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}", 'error')
        
    finally:
        cur.close()
        cnxn.close()

    return True


def search_sqllite_information(search_term=None):
    """
    Searches information in the 'posts' table.
    If search_term is provided, it filters rows where the 'technology' column
    contains the search term. Otherwise, it returns all rows.
    
    Parameters:
        search_term (str, optional): Term to search in the 'technology' column.
        
    Returns:
        tuple: 
            - data (list of tuples): All rows matching the search term or all rows if None.
            - uniquedata (list of str): List of unique 'technology' values from the table.
    """
    cnxn = create_connection()
    data = []
    cur = cnxn.cursor()

    try:

        cur.execute("SELECT * FROM posts WHERE technology LIKE ?", (f"%{search_term}%",))
        data = cur.fetchall()

    except sqlite3.Error as e:
        print(f"Database error: {e}", 'error')
        
    finally:
        cur.close()
        cnxn.close()

    return data