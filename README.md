# GrandPyBot application

**Scope**
This application will ask the user to write and send a text inside of which he/she asks for the localisation of a place. The app will then return 3 pieces of information:
- The exact adress of the location
- A map with a mark on this adress
- General information about the place
The bot answer will be displayed in a chat on the right hand side while the map will be displayed on the left side.

**Example**
The user will ask:
>"Salut Grandpy, j'espère que tu vas bien. Dis moi, il me semble que tu y es déjà allé, pourrais tu m'indiquer où sont situées les chutes du Niagara?"

GrandPyBot will answer:
>L'adresse que tu cherches est:Niagara Falls, NY 14303, États-Unis.
>Les chutes du Niagara ou chutes Niagara, en anglais Niagara Falls, sont un ensemble de trois chutes d’eau situées sur la rivière Niagara qui relie le lac Érié au lac Ontario, dans l’est de l’Amérique du Nord, à la frontière entre le Canada et les États-Unis :le « Fer à Cheval » ou « chutes canadiennes » ; les « chutes américaines » ; le « voile de la mariée », d’une taille moindre.

# Technical information

**Languages used**
This application uses the following languages:
- Python
- HTML/CSS/Javascript (Jquery)
- Ajax

**Requirements**
All Requirements are included in the requirements.txt file

# Known limitations

## Parser limitation

The parser that finds the location inside the user message takes what's between some words identified as "locators" (list below)  and the next punctuation.
**Locators words:**
["adresse de", "adresse d'", "adresse des", "se trouve", "se trouvent", "situe ", "situent", "situé ", "situés", "situées", "située", "trouver"]

All location-related question not using one of those terms will not be recognized.

## Case sensitivity
This app is based on wikipedia API which is **case sensitive.** It means that if you use "les chutes du **n**iagara" instead of the correct spelling "les chutes du **N**iagara", you will have a map and the adress of the location (because google maps API is not case sensitive) but you will not get detailed information about the location (because the wikimedia API did not recognize the location)