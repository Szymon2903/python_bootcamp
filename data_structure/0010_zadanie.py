# Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji
# dodawanie, odejmowanie, mnożenie,dzielenie
# W przypadku podania nieprwidłowej operacji program ma wyświetlić odpowiedni komunikat o błedzie

# Przykładowy komunikat programy;
# Podaj pierwszą liczbę: 15
# Podaj drugą liczbę: 5
# Podaj rodzaj operacji: +


number_1 = int(input('Podaj pierwsza liczbe: '))
number_2 = int(input('Podaj druga liczbe: '))
action = input('Podaj rodzaj operacji: ')

if action == '+':

    print(f'Wynik: {number_1 + number_2}')
elif action == '-':
    print(f'Wynik: {number_1 - number_2}')
elif action == '*':
    print(f'Wynik: {number_1 * number_2}')
elif action == '/' and number_2 != 0:
    print(f'Wynik: {number_1 / number_2}')
else:

    print(f'{action} nieznane dzialanie lub dzielenie przez 0')