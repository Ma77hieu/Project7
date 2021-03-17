import os

if os.environ.get('API_KEY_PLACES') is not None:
    API_KEY_PLACES = os.environ.get('API_KEY_PLACES')
else:
    API_KEY_PLACES = ""
