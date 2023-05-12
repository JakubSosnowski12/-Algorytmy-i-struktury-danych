def lexicographic_sort(numbers):
    return sorted(numbers, key=lambda x: str(x))

while True:
    user_input = input("Wprowadź liczby oddzielone przecinkami: ")
    numbers = [int(num.strip()) for num in user_input.split(",")]
    sorted_numbers = lexicographic_sort(numbers)
    print(sorted_numbers)
    restart = input("Czy chcesz ponownie uruchomić program? (T/N): ")
    if restart.upper() != "T":
        break