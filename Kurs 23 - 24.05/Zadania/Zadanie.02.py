

# Napisz program wczytujący plikz logami aktywności użytkowników w systemie.
# Na podstawie wczytanych danych wyświetl informacje o sumarycznym czasie przebywania każdego użytkownika w systemie.

# --> Przykład użycia:
# python read_logs.py logs.txt
# --> Czas przebywania w systemie:
# - user-1: 92 s
# - user-2: 51 s
# - user-3: 20 s

import sys

try:
    f_path = sys.argv[1]
except IndexError:
    f_path = "data\logs.txt"

last_login = {}
last_logout = {}
with open("logs.txt") as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN":
            last_login[login] = time

        elif action == "LOGOUT":

print(last_login)


