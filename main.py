import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
df = pd.read_csv('data/WielkiKanionKolorado.csv')

# Wybór pierwszej i drugiej kolumny
dane = df.iloc[:, [0, 1]]

# Przypisanie kolumn do zmiennych
dystans = dane.iloc[:, 0]
wysokosc = dane.iloc[:, 1]


def lagrange_interpolation(x, y, x_interp, n, stride):

    n_points = len(x)
    if n > n_points:
        n = n_points

    y_interp = []

    for xi in x_interp:
        y_i = 0.0

        indices = range(0, n_points, stride)

        for i in indices[:n]:
            numerator = 1.0
            denominator = 1.0

            for j in indices[:n]:
                if j != i:
                    numerator *= (xi - x[j])
                    denominator *= (x[i] - x[j])
                    #print(x[j])

            y_i += y[i] * (numerator / denominator)
        y_interp.append(y_i)

    return y_interp


# Przykładowe wartości x_interp dla interpolacji
x_interp = list(range(int(dystans.min()), int(dystans.max()) + 1))

# Liczba używanych węzłów i odstęp między nimi
n = 15  # Możesz dostosować tę wartość do wybranej liczby węzłów
stride = int(
    len(dystans) / (n-1))  # Możesz dostosować ten odstęp do większych wartości dla większych odstępów między punktami

# Wywołanie interpolacji
y_interp = lagrange_interpolation(dystans, wysokosc, x_interp, n, stride)

# Wyświetlenie wyników
print("Dystans (m)\tWysokość interpolowana (m)")
for x, y in zip(x_interp, y_interp):
    print(f"{x}\t\t{y}")


# Wyświetlanie wyników na wykresie
plt.figure()
plt.semilogy(dystans, wysokosc, 'b--', label='Dane rzeczywiste')
plt.semilogy(x_interp, y_interp, 'r-', label='Interpolacja Lagrange\'a')
plt.scatter(dystans[::stride], wysokosc[::stride], color='k', label='Węzły')
plt.xlabel('Dystans (m)')
plt.ylabel('Wysokość (m)')
plt.title('Interpolacja Lagrange\'a: Wielki Kanion Kolorado dla 15 punktów')
plt.legend()
plt.show()
