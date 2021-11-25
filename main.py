# Shift + F6 - zmień nazwę zmiennej i wszystkie użycia
# Ctrl + Q na funkcji / klasie / zmiennej - dokumentacja do niej (jeśli jest)
# Ctrl + Alt + L - przeformatuj cały otwarty plik (jak będziesz miał coś zaznaczone to tylko formatuje zaznaczone)
import calculator
from calculator import Calculation

print("Kalkulator")


# Tuple: funckcja nie musi zwracać jednej rzeczy, może zwracać kilka


# Lekcja 1: Jak zrobić funkcję, żeby nie pisać czegoś 2,3,4,5x
def try_parse_string_to_float(maybe_number):
    # Lekcja 2 Try catch - jak się obsługuje sytuacje które mogą rzucić błędem?
    try:
        # Przypadek 1: To nie cyfra tylko "dupa" -> nic nie podmieniam, podmieniony taki sam jak oryginał
        # Przyapdek 2: To liczba ale z kropką -> Nic nie podmineiam, działa
        # Przypadek 3: To liczba całkowita -> Nic nie podmieniam, działa
        # Pryzpadek 4: To liczba z przecinkiem -> Podmieniam, DZIAŁA
        # Przypadek 5: To błędna liczba typu 3,4,5,6789 -> I TAK by nie działało

        dot_normalized_string = maybe_number.replace(",", ".")
        number = float(dot_normalized_string)
        # Lekcja 3 - funkcja może zwrócić kilka rzeczy, używaj tego dla czytelności kodu jeśli ma to sens
        return True, number
    except ValueError:
        return False, None


# Lekcja 4 - Rozdzielaj zadania - funkcja powinna robić JEDNĄ rzecz i robić ją dobrze
def prompt_user_for_number(prompt_text):
    while True:
        user_input = input(prompt_text)
        is_number, number = try_parse_string_to_float(user_input)
        if is_number:
            return number
        else:
            print("To nie była liczba!")


#
# while WarunekKontynuowania:
#    rob_cos()


def prompt_user_for_operation(prompt_text: str):
    while True:  # rób w nieskończoność
        operation = input(prompt_text)
        match operation:
            case "+":
                return Calculation.add
            case "-":
                return Calculation.subtract
            case "*":
                return Calculation.multiply
            case "/":
                return Calculation.divide
            case _:
                print("Niewłaściwa operacja!")


def get_description(operation: Calculation):
    match operation:
        case Calculation.add:
            return "dodać"
        case Calculation.subtract:
            return "odjąć"
        case Calculation.multiply:
            return "razy"
        case Calculation.divide:
            return "podzielone przez"


# Lekcja 5 - Logika główna to nic innego jak kompozycja małych funkcji o których prosto się myśli: Dziel i Rządź
first_number = prompt_user_for_number("Podaj pierwszą liczbę: ")
chosen_operation = prompt_user_for_operation(" Wskaż operacje: (+, -, *, /) ")
second_number = prompt_user_for_number("Podaj drugą liczbę: ")

result = calculator.calculate(chosen_operation, first_number, second_number)

print(f" {first_number} {get_description(chosen_operation)} {second_number} = {result}")
exit()

# else:
#     print("fatal error")
#     break

# Lekcja 6 - Interpolacja stringów - jak robić coś lepiej niż napis + napis + napis
# print(f"Podałeś następujące liczby {first_number}, {second_number}, ich suma to {first_number + second_number}")

# Lekcja 0 - jeśli nie masz wymagań dla tego co chcesz robić to co Ty robisz?!
# 1. Przywitaj użytkownika  DONE
# 2. Poproś o cyfrę         DONE
# 3. Poproś o operację      DONE
# 4. Poproś o drugą cyfrę   DONE
# 5. Pokaż wynik            DONE
