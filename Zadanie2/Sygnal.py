import math
import numpy as np
from SortedSet.sorted_set import SortedSet
import matplotlib.pyplot as plt


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
        wartosc = int(1000 / czestotliwosc)
        for i in range(0, 1000, wartosc):
            x.append(self.wartosci_x[i])
            y.append(self.wartosci_y[i])
        sygnal = Sygnal(x, y)
        sygnal.sygDyskretny = True
        print(sygnal.wartosci_x)
        return sygnal

    # COS JEST NIE TAK !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def kwantyzacja(self, czestotliwosc, poziom_kwantyzacji):
        syg_probkowany = self.probkowanie(czestotliwosc)
        minn = syg_probkowany.wartosci_y[0]
        maxx = syg_probkowany.wartosci_y[0]
        for i in range(len(syg_probkowany.wartosci_y)):
            if minn > syg_probkowany.wartosci_y[i]:
                minn = syg_probkowany.wartosci_y[i]
            if maxx < syg_probkowany.wartosci_y[i]:
                maxx = syg_probkowany.wartosci_y[i]

        roznica = maxx - minn
        lista = []
        lista_y = []
        for i in range(poziom_kwantyzacji):
            lista.append(minn + ((roznica / poziom_kwantyzacji) * i))

        tree_set = SortedSet(lista)
        for i in range(len(syg_probkowany.wartosci_y)):
            y = [min(tree_set, key=lambda t_v: abs(t_v - v)) for v in syg_probkowany.wartosci_y]

        lista_y.append(y)

        syg_probkowany.wartosci_y = lista_y
        return syg_probkowany

    def rect(self, t):
        if np.math.fabs(t) > 0.5:
            return 0
        elif np.math.fabs(t) == 0.5:
            return 0.5
        else:
            return 1

    def ekstrapolacja_zerowego_rzeduNaj(self, czestotliwosc_probkowania):
        tablica_nowych_y = []
        tablica_nowych_x = []
        syg_probkowany = self.probkowanie(czestotliwosc_probkowania)
        syg_probkowany.sygDyskretny = False
        duze_t = (syg_probkowany.wartosci_x[1] - syg_probkowany.wartosci_x[0])  # krok sygnalu
        t = syg_probkowany.wartosci_x[0]
        while t < syg_probkowany.wartosci_x[-1]:
            suma = 0.0
            for n in range(len(syg_probkowany.wartosci_x)):
                srodek_rect = (t - (duze_t / 2) - (n * duze_t)) / duze_t
                suma += syg_probkowany.wartosci_y[n] * syg_probkowany.rect(srodek_rect)
            tablica_nowych_y.append(suma)
            tablica_nowych_x.append(t)
            t += 1 / czestotliwosc_probkowania

        syg_probkowany.wartosci_x = tablica_nowych_x
        syg_probkowany.wartosci_y = tablica_nowych_y

        return syg_probkowany

    # TEN WZOR TEZ OKEJ ALE NIE JEST ROBIONE ZE WZORU

    # def ekstrapolacja_zerowego_rzedu(self, czestotliwosc):
    #     wsp_x = []
    #     wsp_y = []
    #     czest = 1 / (czestotliwosc * 100)
    #     syg_ekstr_zero = self.probkowanie(czestotliwosc)
    #     syg_ekstr_zero.sygDyskretny = False
    #     krokSygnalu = syg_ekstr_zero.wartosci_x[1] - syg_ekstr_zero.wartosci_x[0]
    #     # for i in range(0, krokSygnalu, czest):  # przeskok na kolejny y
    #     #     for j in range(i, syg_probkowany.wartosci_x[-1], czest):
    #     #         wsp_x.append(syg_probkowany.wartosci_x[i])
    #     #         wsp_y.append(syg_probkowany.wartosci_y[i])
    #     for i in range(len(syg_ekstr_zero.wartosci_x)):
    #         licznik = syg_ekstr_zero.wartosci_x[i]
    #         while licznik < syg_ekstr_zero.wartosci_x[i] + krokSygnalu:
    #             # for j in range(syg_probkowany.wartosci_x[i], syg_probkowany.wartosci_x[i + 1], czest):
    #             wsp_x.append(licznik)
    #             wsp_y.append(syg_ekstr_zero.wartosci_y[i])
    #             licznik += czest
    #     syg_ekstr_zero.wartosci_x = wsp_x
    #     syg_ekstr_zero.wartosci_y = wsp_y
    #
    #     return syg_ekstr_zero

    def tri(self, t):
        return 0 if np.math.fabs(t) > 1 else 1 - np.math.fabs(t)

    def interpolacja_pierwszego_rzeduNaj(self, czestotliwosc):
        syg_int_pierw_rzedu = self.probkowanie(czestotliwosc)
        syg_int_pierw_rzedu.sygDyskretny = False
        duze_t = syg_int_pierw_rzedu.wartosci_x[1] - syg_int_pierw_rzedu.wartosci_x[0]  # krok sygnalu
        tablica_nowych_x = []
        tablica_nowych_y = []
        t = syg_int_pierw_rzedu.wartosci_x[0]

        while t < syg_int_pierw_rzedu.wartosci_x[-1]:
            suma = 0.0
            for i in range(len(syg_int_pierw_rzedu.wartosci_x)):
                suma += syg_int_pierw_rzedu.wartosci_y[i] * syg_int_pierw_rzedu.tri((t - i * duze_t) / duze_t)
            tablica_nowych_x.append(t)
            tablica_nowych_y.append(suma)
            t += 1 / czestotliwosc

        syg_int_pierw_rzedu.wartosci_x = tablica_nowych_x
        syg_int_pierw_rzedu.wartosci_y = tablica_nowych_y

        return syg_int_pierw_rzedu
