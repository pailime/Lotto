import random

menu = "Podaj liczbę w zakresie od 1 do 49: "
print(menu)


def user_number():
    while True:
        try:
            number = int(input())
            break
        except (ValueError, TypeError):
            print("Błędna wartość")
    return number


def user_numbers():
    numbers = []
    # lista = range(1, 50)
    while len(numbers) < 6:
        number = user_number()
        if number not in numbers and 0 < number <= 49:
            numbers.append(number)
        elif number in numbers:
            print("Taka liczba już została podana")
        else:
            print("Błędna liczba")
    return sorted(numbers)


def computer_numbers():
    num = list(range(1, 50))
    random.shuffle(num)
    return sorted(num[:6])


def lotto():
    play_num = user_numbers()
    comp_num = computer_numbers()
    print(f"Twoje liczby: ", play_num)
    print(f"Liczby LOTTO: ", comp_num)

    hits = 0

    for i in play_num:
        if i in comp_num:
            hits += 1
    if hits == 6:
        print("Trafiłeś 6! GRATULACJE")
    elif hits == 5:
        print("Trafiłeś 5!")
    elif hits == 4:
        print("Trafiłeś 4!")
    elif hits <= 3:
        print(f"Słabo wyszło, trafiłeś: ", hits)


if __name__ =='__main__':
    lotto()
