def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

# Meminta input dari pengguna saat program dijalankan
user_input = input("Masukkan sebuah bilangan bulat: ")

try:
    number = int(user_input)
    if is_palindrome(number):
        print(f"{number} adalah sebuah palindrome.")
    else:
        print(f"{number} bukan sebuah palindrome.")
except ValueError:
    print("Input tidak valid! Silakan masukkan bilangan bulat.")
