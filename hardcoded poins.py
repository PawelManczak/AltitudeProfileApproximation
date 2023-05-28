import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
df = pd.read_csv('data/MountEverest.csv')

# Wybór pierwszej i drugiej kolumny
dane = df.iloc[:, [0, 1]]
print("dane: ")
print(dane)
# Przypisanie kolumn do zmiennych
dystans = dane.iloc[:, 0]
wysokosc = dane.iloc[:, 1]


def lagrange_interpolation(x, y, x_interp, punkty):

    y_interp = []

    for xi in x_interp:
        y_i = 0.0

        indices = punkty

        for i in indices:
            numerator = 1.0
            denominator = 1.0

            for j in indices:
                if j != i:
                    numerator *= (xi - x[j])
                    denominator *= (x[i] - x[j])
                    #print(x[j])

            y_i += y[i] * (numerator / denominator)
        y_interp.append(y_i)

    return y_interp


nodes = [0, 20, 50, 75, 100, 150, 180, 250, 300, 350, 400, 425, 450, 460, 485, 510]
xx = [dystans[i] for i in nodes]
yy = [wysokosc[i] for i in nodes]
x_interp = dystans
y_interp = lagrange_interpolation(dystans, wysokosc, x_interp, nodes)

# Wyświetlenie wyników
print("Dystans (m)\tWysokość interpolowana (m)")
for x, y in zip(x_interp, y_interp):
    print(f"{x}\t\t{y}")

# Wyświetlanie wyników na wykresie
plt.figure()
plt.plot(dystans, wysokosc, 'b--', label='Dane rzeczywiste')
plt.plot(x_interp, y_interp, 'r-', label='Interpolacja Lagrange\'a')
plt.scatter(xx, yy, color='k', label='Węzły')
plt.xlabel('Dystans (m)')
plt.ylabel('Wysokość (m)')
plt.title('Interpolacja Lagrange\'a: Mount Everest dla 15 punktów rozłożonych nierównomiernie')
plt.legend()
plt.show()
