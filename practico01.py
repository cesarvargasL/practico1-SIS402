import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def generarDatosImc(n):
    datos = []
    for i in range(n):
        estatura = round(random.uniform(0.50, 2.00), 2)
        imc = round(random.uniform(18.5, 24.9), 2)
        peso = round(imc * (estatura ** 2), 2)

        imcCalculado = peso / (estatura ** 2)
        if imcCalculado < 18.5:
            peso = round(18.5 * (estatura ** 2), 2)
        elif imcCalculado > 24.9:
            peso = round(24.9 * (estatura ** 2), 2)

        datos.append((estatura, peso))
    return datos

datos = generarDatosImc(100)

print("Datos generados")
for estatura, peso in datos:
    print("Estatura: {} m, Peso: {} kg".format(estatura, peso))


estatura = [dato[0] for dato in datos]
peso = [dato[1] for dato in datos]

def ajusteLineal(x, a, b):
    return a * x + b

rangoMinimoX = min(estatura)
rangoMaximoX = max(estatura)

generadorPuntosX = [rangoMinimoX + i * (rangoMaximoX - rangoMinimoX) / 99 for i in range(100)]

parametros = curve_fit(ajusteLineal, estatura, peso)[0]
a = parametros[0]
b = parametros[1]

calculoY = [ajusteLineal(x, a, b) for x in generadorPuntosX]

plt.scatter(estatura, peso, label="Datos")
plt.plot(generadorPuntosX, calculoY, color="red", label="Ajuste: y = {:.2f}x + ({:.2f})".format(a, b))
plt.xlabel("Estatura (m)")
plt.ylabel("Peso (kg)")
plt.legend()
plt.show()