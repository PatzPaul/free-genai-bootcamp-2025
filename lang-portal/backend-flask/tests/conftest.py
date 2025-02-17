import pytest
import sqlite3
import sys
from pathlib import Path
from flask import g
from datetime import datetime

# Add the parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent))

from app import create_app

def adapt_datetime(val):
    """Convert datetime to string for SQLite."""
    return val.isoformat()

def convert_datetime(val):
    """Convert string from SQLite to datetime."""
    return datetime.fromisoformat(val)

@pytest.fixture
def app():
    # Create the app with test configuration
    app = create_app(test_config={
        "TESTING": True,
        "DATABASE": ":memory:"
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app):
    """Create a new database connection for each test."""
    with app.app_context():
        # Register datetime adapter
        sqlite3.register_adapter(datetime, adapt_datetime)
        sqlite3.register_converter("timestamp", convert_datetime)
        
        db = sqlite3.connect(":memory:", 
                           detect_types=sqlite3.PARSE_DECLTYPES,
                           isolation_level=None)
        db.row_factory = sqlite3.Row
        app.db = db

        # Create tables
        cursor = db.cursor()
        
        # Create groups table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        
        # Create study_activities table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        
        # Create study_sessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_id INTEGER NOT NULL,
                study_activity_id INTEGER NOT NULL,
                created_at TIMESTAMP NOT NULL,
                FOREIGN KEY (group_id) REFERENCES groups (id),
                FOREIGN KEY (study_activity_id) REFERENCES study_activities (id)
            )
        ''')
        
        # Insert test data
        cursor.execute("INSERT INTO groups (id, name) VALUES (1, 'Test Group')")
        cursor.execute("INSERT INTO study_activities (id, name) VALUES (1, 'Test Activity')")
        
        db.commit()
        yield db
        db.close()

@pytest.fixture
def test_client(client, db):
    """Combine client and db fixtures for tests that need both."""
    return client 