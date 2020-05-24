

# Napisz program wczytujący listę adresów email z pliku i tworzący nowy plik z odfiltrowaną zawartością.
# Wejściowy plik może zawierać duplikaty adresów, ten sam adres pisany różną wielkością liter,
# Linie zawierające białe znaki oraz błędne adresy email (brak znaku @ lub występuje on wiele razy).
# Wynikowy plik powinien zawierać unikaln, posortowane, poprawne adresy email

# --> Przykład użycia:
# --> python clean_emails.py emails.txt cleaned_emails.txt

import sys

try:
    f_in_path = sys.argv[1]
    out_f_path = sys.argv[2]
except IndexError:
    f_in_path = "data/emails.txt"
    out_f_path = "output/cleaned_emails.txt"


emails = set()
with open(f_in_path) as f:
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            emails.add(line)

with open(out_f_path, "w") as f:
    for email in sorted(emails):
        f.write(email + "\n")