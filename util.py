import os


def get_api_key():
    return os.environ.get('GOOGLE_API_KEY')
