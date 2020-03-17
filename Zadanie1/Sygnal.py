import matplotlib.pyplot as plt
import numpy as np


class Sygnal:

    def __init__(self, x, y):
        self.sygDyskretny = False
        self.wartosci_x = x
        self.wartosci_y = y
        self.czas_poczatkowy = 0
        self.czas_trwania_sygnalu = 0

    # do rysowania wykresow
    def __init__(self, x, y, t1, d):
        # t1 - czas poczatkowyy
        # d - czas trwania sygnalu
        self.sygDyskretny = False
        self.czas_poczatkowy = t1
        self.czas_trwania_sygnalu = d
        self.wartosci_x = x
        self.wartosci_y = y

    # dodaje dany sygnal z innym
    def dodawanie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] + sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y, self.czas_poczatkowy, self.czas_trwania_sygnalu)
        return sygnal_nowy

    def odejmowanie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] - sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y, self.czas_poczatkowy, self.czas_trwania_sygnalu)
        return sygnal_nowy

    def mnozenie(self, sygnal2):
        y = []
        for i in range(len(self.wartosci_y)):
            # x[i] = self.wartosci_x[i] + sygnal2.wartosc_x[i]
            y.append(self.wartosci_y[i] * sygnal2.wartosci_y[i])
        sygnal_nowy = Sygnal(self.wartosci_x, y, self.czas_poczatkowy, self.czas_trwania_sygnalu)
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
        sygnal_nowy = Sygnal(self.wartosci_x, y, self.czas_poczatkowy, self.czas_trwania_sygnalu)
        return sygnal_nowy

    def rysuj_sygnal(self):
        if not self.sygDyskretny:
            plt.plot(self.wartosci_x, self.wartosci_y)
            plt.xlim(self.czas_poczatkowy, self.czas_poczatkowy + self.czas_trwania_sygnalu)  # od do X
            plt.xlabel('t[s]')
            plt.ylabel('Amplituda')
            plt.show()
        else:
            plt.scatter(self.wartosci_x, self.wartosci_y)
            plt.xlim(self.czas_poczatkowy, self.czas_poczatkowy + self.czas_trwania_sygnalu)  # od do X
            plt.xlabel('t[s]')
            plt.ylabel('Amplituda')
            plt.show()

    def rysuj_histogram(self, ilosc_przedzialow):
        plt.hist(self.wartosci_y, bins=int(ilosc_przedzialow), rwidth=0.85)
        plt.show()
