
# Esercizio 1
totale = float(input("Quanti euro hai?"))
prezzo = float(input("Quanti costano al pezzo?"))
print(f"Ne puoi acquistare {totale//prezzo}")
print(f"Ti rimarrà {totale%prezzo:.2f} euro")
