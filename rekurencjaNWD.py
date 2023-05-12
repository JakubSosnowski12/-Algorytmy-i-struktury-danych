def NWD(a,b):
    while a!=b:
        if a>b: return NWD(a-b,b)
        else: return NWD(a,b-a)
    return a
wynik = NWD(24, 36)
print(wynik)

funkcja wynik(i)
    jeżeli i<3
        zwróć 1 i zakończ;
    w przeciwnym razie
        jeżeli i mod 2 =0;
            zwróć wynik(i-3) + wynik(i-1)+1;
        w przeciwnym razie
            zwróć wynik(i-1) mod 7