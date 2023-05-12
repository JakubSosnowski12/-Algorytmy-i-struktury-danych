def dec_to_bin(n):
    if n == 0:
        return 0
    else:
        remainder = n % 2
        n = n // 2
        return dec_to_bin(n) * 10 + remainder

# Przykładowe użycie
decimal_number = 23
binary_number = dec_to_bin(decimal_number)
print(f"Liczba dziesiętna {decimal_number} zamieniona na liczbę binarną to: {binary_number}")