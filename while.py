# Esercizio ciclo WHILE 
x = 0
while x <= 0:
    x= int(input("Inserisci un numero positivo: "))
    if x > 0 :
        print(f"Hai inserito il numero positivo {x:.2f}")
    else :
        print("Non ha inserito un numero valido")