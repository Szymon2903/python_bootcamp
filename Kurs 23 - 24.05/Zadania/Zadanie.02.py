

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
    f_path = "Kurs/users.txt"

last_login = {}
last_logout = {}
last_total_time = {}

with open(f_path) as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN":
            last_login[login] = time
        elif action == "LOGOUT":
            user_total_time[login] = user_total_time.get(login, 0) + time - last_login[login]

print("Czas przebywania w systemie: ")
for user, time in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
    print(f" - {user:>8} {time}")

print(last_login)


