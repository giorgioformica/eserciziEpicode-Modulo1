# Esercizio 1 Booleani : chiedi età e patente e stampa true se può guidare o false se non può
eta = int(input("Quanti anni hai? "))
patente = input("Hai la patente?(si/no)").lower()
print(eta>=18 and (patente == 'si' or patente == 's'))

# Esercizio 2 Biblioteca
premium = False
ritardo = True
consentito = premium or not ritardo
print("può entrare in biblioteca?", consentito)