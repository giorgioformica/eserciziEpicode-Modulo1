#Esercizio MODULO I Stringhe e Operazioni sulle stringhe
frase = input("Inserisci una frase palindroma:")
frase_normalizzata = frase.strip().lower()
print(frase_normalizzata)
frase_inversa = frase[::-1]
print(frase_inversa)
print("La frase è palindroma? ",frase_normalizzata == frase_inversa)

