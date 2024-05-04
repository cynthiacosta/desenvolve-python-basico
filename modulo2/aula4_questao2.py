graus_fahrenheit = int(input("Informe a temperatura em graus Fahrenheit: "))

graus_celsius = (graus_fahrenheit - 32) * 5 / 9
graus_celsius = int(graus_celsius)

print(f"{graus_fahrenheit} graus Fahrenheit são {graus_celsius} graus Celsius.")