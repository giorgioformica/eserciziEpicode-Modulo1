# Esercizio 1 ciclo WHILE 
x = 0
while x <= 0:
    x= int(input("Inserisci un numero positivo: "))
    if x > 0 :
        print(f"Hai inserito il numero positivo {x:.2f}")
    else :
        print("Non ha inserito un numero valido")

# Esercizio 2 ciclo WHILE : calcolare la somma delle cifre di un numero

x = 1
somma = 0
n = int(input("SOMMA DI I NUMERI FINO A. Inserisci un numero: "))

while x <= n:
    somma += x
    x += 1
    print(somma)

print(f"La somma di tutte le cifre fino a {n} è {somma}")

# Variante Esercizio 2 ciclo WHILE : calcolare la somma delle cifre di un numero

x= 0
somma = 0
n_str = input("SOMMA DELLE CIFRE. Inserisci un numero: ")
cifre_numero = len(n_str)

while x < cifre_numero:
    cifra = int(n_str[x])
    somma += cifra
    x += 1

print(f"La somma di tutte le cifre del numero {n_str} è {somma}")