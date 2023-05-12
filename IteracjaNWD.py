def NWD_iter(a,b):
    while a!=b:
        if a>b: a=a-b
        else: b=b-a
    return a
wynik = NWD_iter(24, 36)
print(wynik)