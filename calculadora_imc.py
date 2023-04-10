nombre = input("Introduce tu nombre completo ")

edad = int(input("Introduce tu edad en años "))

m = float(input("Peso en kilogramos " ))

est = float(input("Estatura en metros "))

print(f"Soy {nombre}, tengo {edad}  años, peso {m} kilogramos y mido {est} metros")

IMC = m/est**2

print(f"IMC: " + str(IMC))

if IMC >= 0  and IMC <= 15.99 :
    print("IMC Delgadez Severa")

elif IMC >= 16.00 and IMC <= 16.99 :
    print("IMC Delgadez Moderada")

elif IMC >= 17.00 and IMC <= 18.49 :
    print("IMC Delgadez Leve")

elif IMC >= 18.50 and IMC <= 24.99 :
    print("IMC Normal")

elif IMC >= 25.00 and IMC <= 29.99 :
    print("IMC Sobrepeso")

elif IMC >= 30.00 and IMC <= 34.99 :
    print("IMC Obesidad Leve")

elif IMC >= 35.00 and IMC <= 39.00 :
    print("IMC Obesidad Media")

elif IMC <= 40.00 :
    print("IMC Obesidad Morbida")







