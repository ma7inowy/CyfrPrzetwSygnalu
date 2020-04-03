import matplotlib.pyplot as plt
import numpy as np
import math


class Sygnal:

    def __init__(self, x, y):
        self.sygDyskretny = False
        self.wartosci_x = x
        self.wartosci_y = y
        # self.t1 = 0
        # self.d = 0

    # dodaje dany sygnal z innym
    def dodawanie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] + sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y)
        return sygnal_nowy

    def odejmowanie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] - sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y)
        return sygnal_nowy

    def mnozenie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] * sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y)
        return sygnal_nowy

    # jak 0 to 1 ??? mozna tak?
    def dzielenie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            if sygnal2.wartosci_y[i] == 0:
                y.append(self.wartosci_y[i] / 1)
            else:
                y.append(self.wartosci_y[i] / sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y)
        return sygnal_nowy

    def rysuj_sygnal(self):
        if not self.sygDyskretny:
            plt.plot(self.wartosci_x, self.wartosci_y)
            plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
            plt.xlabel('t[s]')
            plt.ylabel('Amplituda')
            plt.show()
        else:
            plt.scatter(self.wartosci_x, self.wartosci_y)
            plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
            plt.xlabel('t[s]')
            plt.ylabel('Amplituda')
            plt.show()

    def rysuj_histogram(self, ilosc_przedzialow):
        plt.hist(self.wartosci_y, bins=int(ilosc_przedzialow), rwidth=0.85)
        plt.show()

    def wartosc_srednia(self):
        ulamek = 1 / (len(self.wartosci_x) - 0 + 1)
        suma = 0
        for i in range(len(self.wartosci_y)):
            suma += self.wartosci_y[i]
        wynik = ulamek * suma
        # print("Wartosc srednia to: ", wynik)
        return wynik

    def wartosc_bezwzgledna(self):
        # ulamek = 1 / (self.wartosci_x[len(self.wartosci_x) - 1] - self.wartosci_x[0] + 1)
        ulamek = 1 / (len(self.wartosci_x) - 0 + 1)
        suma = 0
        for i in range(len(self.wartosci_x)):
            suma += math.fabs(self.wartosci_y[i])
        wynik = ulamek * suma
        # print("Wartosc srednia bezwzgledna to: ", wynik)
        return wynik

    def wartosc_skuteczna(self):
        return math.sqrt(self.moc_srednia())

    def wariancja(self):
        # ulamek = 1 / (self.wartosci_x[len(self.wartosci_x) - 1] - self.wartosci_x[0] + 1)
        ulamek = 1 / (len(self.wartosci_x) - 0 + 1)
        suma = 0
        for i in range(len(self.wartosci_x)):
            suma += (self.wartosci_y[i] - self.wartosc_srednia()) ** 2
        wynik = ulamek * suma
        # print("Wartosc wariancji to : ", wynik)
        return wynik

    def moc_srednia(self):
        ulamek = 1 / (len(self.wartosci_x) - 0 + 1)
        suma = 0
        for i in range(len(self.wartosci_x)):
            suma += self.wartosci_y[i] ** 2  # x^2(n) to x(n) * x(n) no nie?
        wynik = ulamek * suma
        # print("Wartosc mocy sredniej to: ", wynik)
        return wynik

    def pokazWynikiParametrow(self):
        str1 = "Wartosc srednia to: " + str(self.wartosc_srednia())
        str2 = "\nWartosc bezwzględna to: " + str(self.wartosc_bezwzgledna())
        str3 = "\nWartosc skuteczna to: " + str(self.wartosc_skuteczna())
        str4 = "\nWartosc wariancji to: " + str(self.wariancja())
        str5 = "\nWartosc mocy średniej to: " + str(self.moc_srednia())

        return str1 + str2 + str3 + str4 + str5

    # DO ZADANIA2

    def probkowanie(self, czestotliwosc):
        x = []
        y = []
        j = 0
        # for i in range(self.t1, self.t1 + self.d):
        #     x.append(j)
        #     j += 1 / czestotliwosc
        #
        # for i in range(0, 1000, int(1000 / czestotliwosc)):
        #     y.append(self.wartosci_y[i + czestotliwosc])
        for i in range(0, 1000, czestotliwosc):
            x.append(self.wartosci_x[i])
            y.append(self.wartosci_y[i])
        sygnal = Sygnal(x, y)
        sygnal.sygDyskretny = True
        print(sygnal.wartosci_x)
        return sygnal
