import re
from datetime import datetime

# Funkcja sprawdzająca poprawność e-mail
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Funkcja do obliczeń pola prostokąta
def calculate_rectangle_area(length, width):
    return length * width

# Funkcja przetwarzająca listę danych (filtracja liczb większych od 10 i sortowanie rosnące)
def process_list(data):
    filtered_data = [x for x in data if x > 10]
    return sorted(filtered_data)

# Funkcja konwertująca format dat
def convert_date_format(date_str, current_format, target_format):
    try:
        date_obj = datetime.strptime(date_str, current_format)
        return date_obj.strftime(target_format)
    except ValueError:
        return "Niepoprawny format daty"

# Funkcja sprawdzająca czy tekst jest palindromem
def is_palindrome(text):
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

# Przykład użycia funkcji
if __name__ == "__main__":
    print(is_valid_email("example@domain.com"))
    print(calculate_rectangle_area(5, 10))
    print(process_list([3, 15, 7, 20, 1]))
    print(convert_date_format("21-03-2025", "%d-%m-%Y", "%Y/%m/%d"))
    print(is_palindrome("kajak"))