# Esercizio 1 ciclo WHILE 
x = 0
while x <= 0:
    x= int(input("Inserisci un numero positivo: "))
    if x > 0 :
        print(f"Hai inserito il numero positivo {x:.2f}")
    else :
        print("Non ha inserito un numero valido")

# Esercizio 1 ciclo WHILE : calcolare la somma delle cifre di un numero

x = 1
somma = 0
n = int(input("Inserisci un numero: "))

while x <= n:
    somma += x
    x += 1
    print(somma)

print(f"La somma di tutte le cifre fino a {n} è {somma}")
