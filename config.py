import os
from decouple import config

if os.environ.get('API_KEY_PLACES') is not None:
    API_KEY_PLACES = os.environ.get('API_KEY_PLACES')
else:
    API_KEY_PLACES = config("PLACES")
