"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    TRELLO_KEY = os.environ.get('TRELLO_KEY')
    if not TRELLO_KEY:
        raise ValueError("No TRELLO_KEY set for Flask application.")

    TRELLO_TOKEN = os.environ.get('TRELLO_TOKEN')
    if not TRELLO_TOKEN:
        raise ValueError("No TRELLO_TOKEN set for Flask application.")
