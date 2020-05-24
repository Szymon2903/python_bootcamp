import json

"""
load - odczytywanie danych z pliku
dump - zapisywanie danych do pliku 
loads - odczyt danych z tekstu 
dumps - serializacja do tekstu 
"""

text = '{"a":2, "b":4}'


dane = json.loads(text)
