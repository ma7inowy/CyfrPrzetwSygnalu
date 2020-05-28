import math
import numpy as np
from sortedcontainers import SortedSet
import matplotlib.pyplot as plt
import cmath

skok_probkowania = 0


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
        global skok_probkowania
        skok_probkowania = wartosc
        # print("WARTOSC" + str(wartosc))
        for i in range(0, 1000, wartosc):
            if i < len(self.wartosci_y):  # ten if dolozony
                x.append(self.wartosci_x[i])
                y.append(self.wartosci_y[i])

        sygnal = Sygnal(x, y)
        sygnal.sygDyskretny = True
        # print(sygnal.wartosci_x)
        return sygnal

    def znajdz_max_z_przedzialu(self, lista, poczatek, koniec):
        temp_list = []
        for i in range(len(lista)):
            if poczatek <= lista[i] <= koniec:
                temp_list.append(lista[i])

        nowy_y = max(temp_list)

        return nowy_y

    # COS JEST NIE TAK!
    def kwantyzacja(self, czestotliwosc, poziom_kwantyzacji):

        syg_probkowany = self.probkowanie(czestotliwosc)

        syg_probkowany.sygDyskretny = False
        syg_probkowany.sygDyskretny = False
        minn = syg_probkowany.wartosci_y[0]
        maxx = syg_probkowany.wartosci_y[0]
        maxx = syg_probkowany.wartosci_y[0]
        for i in range(len(syg_probkowany.wartosci_y)):
            if minn > syg_probkowany.wartosci_y[i]:
                minn = syg_probkowany.wartosci_y[i]
            if maxx < syg_probkowany.wartosci_y[i]:
                maxx = syg_probkowany.wartosci_y[i]

        roznica = maxx - minn
        lista = []

        for i in range(poziom_kwantyzacji + 1):
            lista.append(minn + ((roznica / poziom_kwantyzacji) * i))

        lista.sort()

        nowe_y = [min(lista, key=lambda t_v: abs(t_v - v)) for v in syg_probkowany.wartosci_y]

        syg_probkowany.wartosci_y = nowe_y

        return syg_probkowany

    def rect(self, t):
        if np.math.fabs(t) > 0.5:
            return 0
        elif np.math.fabs(t) == 0.5:
            return 0.5
        else:
            return 1

    # cos moze byc nie tak, bo dziwne te krzeselka wychodza
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

    @staticmethod
    def sinc(t):
        if t == 0:
            return 1
        else:
            return math.sin(math.pi * t) / (math.pi * t)

    def rekonstrukcja_w_oparciu_o_fun_sinc(self, czestotliwosc):
        syg_probkowany = self.probkowanie(czestotliwosc)

        przedzial_czasowy = syg_probkowany.wartosci_x[1] - syg_probkowany.wartosci_x[0]
        nowa_lista_y = []
        nowa_lista_x = []
        t = syg_probkowany.wartosci_x[0]
        # while t < syg_probkowany.wartosci_x[-1] + (1.0 / (1.5 * czestotliwosc)):
        while t < syg_probkowany.wartosci_x[-1]:
            sum = 0.0
            for i in range(len(syg_probkowany.wartosci_x)):
                arg = t / przedzial_czasowy - i
                sum += syg_probkowany.wartosci_y[i] * Sygnal.sinc(arg)
            nowa_lista_x.append(t)
            nowa_lista_y.append(sum)
            t += 1 / czestotliwosc

        return Sygnal(nowa_lista_x, nowa_lista_y)

    # syg probkowany do syg kwantowanego?
    @staticmethod
    def blad_sredniokwadratowy(syg_oryginalny, syg_kwantowany):

        ilosc_pktow = len(syg_kwantowany.wartosci_x)

        suma = 0
        for i in range(ilosc_pktow):
            suma += (syg_kwantowany.wartosci_y[i] - syg_oryginalny.wartosci_y[i]) ** 2
            print(suma)

        return suma / ilosc_pktow

    # syg probkowany do syg kwantowanego?
    @staticmethod
    def stosunek_sygnal_szum(syg_oryginalny, syg_kwantowany):
        licznik = 0
        mianownik = 0
        for i in range(len(syg_oryginalny.wartosci_y)):
            licznik += syg_oryginalny.wartosci_y[i] ** 2
            mianownik += (syg_oryginalny.wartosci_y[i] - syg_kwantowany.wartosci_y[i]) ** 2

        wynik = 10 * cmath.log(licznik / mianownik, 10)

        return wynik

    @staticmethod
    def maksymalna_roznica(syg_oryginalny, syg_kwantowany):
        max = math.fabs(syg_oryginalny.wartosci_y[0] - syg_kwantowany.wartosci_y[0])
        for i in range(1, len(syg_oryginalny.wartosci_y)):
            if max < math.fabs(syg_oryginalny.wartosci_y[i] - syg_kwantowany.wartosci_y[i]):
                max = math.fabs(syg_oryginalny.wartosci_y[i] - syg_kwantowany.wartosci_y[i])
        return max

    @staticmethod
    def pokaz_wyniki_miar(syg_oryginalny, syg_kwantowany):
        str1 = "blad_sredniokwadratowy: " + str(Sygnal.blad_sredniokwadratowy(syg_oryginalny, syg_kwantowany))
        str2 = "\nstosunek_sygnal_szum: " + str(Sygnal.stosunek_sygnal_szum(syg_oryginalny, syg_kwantowany))
        str3 = "\nmaksymalna_roznica: " + str(Sygnal.maksymalna_roznica(syg_oryginalny, syg_kwantowany))
        return str1 + str2 + str3

    # do weryfikacji i poprawy
    @staticmethod
    def operacja_splotu2(syg_pierwszy, filtrowane_wartosci):
        lista_x_koncowa = []
        wartosci_splotu = []
        print(len(syg_pierwszy.wartosci_y), "syg_pierwszy rozmiar")
        print(len(filtrowane_wartosci), "filtrowane wartosci rozmiar")

        for i in range(len(syg_pierwszy.wartosci_y) + len(filtrowane_wartosci) - 1):
            sum = 0
            for j in range(len(syg_pierwszy.wartosci_y)):
                if i - j >= 0 and i - j < len(filtrowane_wartosci):
                    sum += syg_pierwszy.wartosci_y[j] * filtrowane_wartosci[len(filtrowane_wartosci) - (i - j) - 1]
            wartosci_splotu.append(sum)

        # for i in range(len(wartosci_splotu)):
        #     lista_x_koncowa.append(i)

        lista_x_koncowa = np.linspace(syg_pierwszy.wartosci_x[0], syg_pierwszy.wartosci_x[-1] + filtrowane_wartosci[-1],
                              len(wartosci_splotu))

        syg = Sygnal(lista_x_koncowa, wartosci_splotu)
        print("Wartosci splotu syg1+filtr=", len(wartosci_splotu))
        # print("operacja_splotu2")
        # print(len(lista_x_koncowa))
        # print(len(wartosci_splotu))
        syg.sygDyskretny = True
        return syg

    @staticmethod
    def operacja_splotu(syg_pierwszy, syg_drugi):
        lista_y = []
        lista_x = []
        for i in range(len(syg_pierwszy.wartosci_y) + len(syg_drugi.wartosci_y)):
            kmin = 0
            kmax = 0
            sum = 0
            if i >= (len(syg_pierwszy.wartosci_y) - 1):
                kmin = i - (len(syg_pierwszy.wartosci_y) - 1)
            else:
                kmin = 0

            if i < (len(syg_drugi.wartosci_y) - 1):
                kmax = i
            else:
                kmax = (len(syg_drugi.wartosci_y) - 1)
            for j in range(kmin, kmax, 1):
                sum += syg_drugi.wartosci_y[j] * syg_pierwszy.wartosci_y[i - j]
            lista_y.append(sum)

        # for k in range(len(lista_y)):
            # lista_x.append(k)
            lista_x=np.linspace(syg_pierwszy.wartosci_x[0], syg_pierwszy.wartosci_x[-1]+syg_drugi.wartosci_x[-1], len(lista_y))
        # czy robic to z czestotliwosica?

        return Sygnal(lista_x, lista_y)

    #korelacja bezposrednia
    @staticmethod
    def korelacja_bezposrednia(syg_pierwszy, syg_drugi):
        lista_x = []
        lista_y = []

        for i in range(len(syg_pierwszy.wartosci_y) + len(syg_drugi.wartosci_y)):
            sum = 0
            if i >= (len(syg_drugi.wartosci_y) - 1):
                k1min = i - (len(syg_drugi.wartosci_y) - 1)
            else:
                k1min = 0

            if i < (len(syg_pierwszy.wartosci_y) - 1):
                k1max = i
            else:
                k1max = (len(syg_pierwszy.wartosci_y) - 1)

            if i <= (len(syg_drugi.wartosci_y) - 1):
                k2min = (len(syg_drugi.wartosci_y) - 1 - i)
            else:
                k2min = 0

            k1 = k1min
            k2 = k2min
            while k1 <= k1max:
                sum += syg_pierwszy.wartosci_y[k1] * syg_drugi.wartosci_y[k2]
                k1 += 1
                k2 += 1
            lista_y.append(sum)

        # for k in range(len(lista_y)):
        #     lista_x.append(k)
        lista_x = np.linspace(syg_pierwszy.wartosci_x[0], syg_pierwszy.wartosci_x[-1] + syg_drugi.wartosci_x[-1],
                              len(lista_y))

        return Sygnal(lista_x, lista_y)

    @staticmethod
    def korelacja_z_uzyciem_splotu(signal_a, signal_b):
        if len(signal_a.wartosci_y) > len(signal_b.wartosci_y):
            signal_a, signal_b = signal_b, signal_a
        signal_a.wartosci_y.reverse()
        return Sygnal.operacja_splotu(signal_a, signal_b)