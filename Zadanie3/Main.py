import os
import sys
import matplotlib.pyplot as plt
import numpy as np

from Filtracja import Filtracja
from Sygnal import Sygnal
from SygnalCiagly import SygnalCiagly
from SygnalDyskretny import SygnalDyskretny


class Main:

    def wybor_sygnalu(self):
        print("---SYGNALY---")
        print("1. szum_o_rozkladzie_jednostajnym")
        print("2. szum_gaussowski")
        print("3. sygnal_sinusoidalny")
        print("4. sygnal_sinusoidalny_wyprostowany_jednopolowkowo")
        print("5. sygnal_sinusoidalny_wyprostowany_dwupolowkowo")
        print("6. sygnal_prostokatny")
        print("7. sygnal_prostokatny_symetryczny")
        print("8. sygnal_trojkatny")
        print("9. skok_jednostkowy")
        print("10. impuls_jednostkowy")
        print("11. szum_impulsowy")
        print("------------------")

    def menu_glowne(self, argument):
        sc = SygnalCiagly()
        sd = SygnalDyskretny()

        amp = int(input('Podaj amplitude : '))
        t1 = int(input('Podaj czas poczatkowy : '))
        d = int(input('Podaj czas trwania sygnalu : '))

        if argument == 1:
            # ??? czy tak chce zrobic? czy zostawic ze rysowanie w SygnalCiagly????????????????
            sc.szum_o_rozkladzie_jednostajnym(amp, t1, d).rysuj_sygnal()
            # sc.szum_o_rozkladzie_jednostajnym(30, 0, 50),
        elif argument == 2:
            sc.szum_gaussowski(amp, t1, d).rysuj_sygnal()
            # sc.szum_gaussowski(30, 0, 50),
        elif argument == 3:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_sinusoidalny(10, 7, 0, 10),
        elif argument == 4:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(10, 6, 0, 10),
        elif argument == 5:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(10, 6, 0, 10),
        elif argument == 6:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_prostokatny(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_prostokatny(10, 2, 0, 10),
        elif argument == 7:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_prostokatny_symetryczny(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_prostokatny_symetryczny(10, 2, 0, 10),
        elif argument == 8:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_trojkatny(amp, okres_T, t1, d).rysuj_sygnal()
            # sc.sygnal_trojkatny(10, 2, 0, 10),
        elif argument == 9:
            ts = int(input('Podaj współczynnik wypełnienia : '))
            sc.skok_jednostkowy(amp, t1, d, ts).rysuj_sygnal()
            # sc.skok_jednostkowy(10, -10, 20),
        elif argument == 10:
            sd.impuls_jednostkowy(amp, t1, d).rysuj_sygnal()
            # sd.impuls_jednostkowy(1, -25, 50),
        elif argument == 11:
            p = int(input('Podaj prawdopodobienstwo : '))
            sd.szum_impulsowy(amp, t1, d, p).rysuj_sygnal()
            # sd.szum_impulsowy(1, 0, 50, 80)
        else:
            print("NACISNIETO ZLY PRZYCISK!!!")

    def wczytaj_z_pliku(self, nazwa_pliku):
        # w pliku poczatek i koniec przedzialu x'ow oraz wspolrzedne y
        print("Wczytywanie z pliku...")
        plik = open(nazwa_pliku)
        caly_tekst = plik.read()
        plik.close()
        podzial_na_linie = caly_tekst.split('\n')
        wartosci_y = podzial_na_linie[1].split(', ')  # wspolrzedne y
        przedzial_wartosci_x = podzial_na_linie[0].split(', ')  # tablica z dwoma wartosciami tj.(pocz. i koniec)
        ilosc_x = len(wartosci_y)

        # konwersja tablicy str na float
        for i in range(0, len(wartosci_y)):
            wartosci_y[i] = float(wartosci_y[i])

        wartosci_x = np.linspace(int(przedzial_wartosci_x[0]), int(przedzial_wartosci_x[1]), ilosc_x)  # wspolrzedne x
        # plt.plot(wartosci_x, wartosci_y)
        # plt.xlim(int(przedzial_wartosci_x[0]), int(przedzial_wartosci_x[1]))  # od do X
        # plt.xlabel('t[s]')
        # plt.ylabel('Amplituda')
        # plt.show()

        return Sygnal(wartosci_x, wartosci_y)

    def zapisz_do_pliku(self, sygnal, nazwa_pliku):
        poczatek_przedzialu = int(sygnal.wartosci_x[0])
        koniec_przedzialu = int(sygnal.wartosci_x[len(sygnal.wartosci_x) - 1])
        wartosci_y = sygnal.wartosci_y

        print("Zapisywanie do pliku...")
        plik = open(nazwa_pliku, "w")
        przecinek = ", "
        tekst = str(poczatek_przedzialu) + przecinek + str(koniec_przedzialu)
        plik.write(tekst)
        plik.write("\n")
        plik.write(self.zamien_liste_w_str(wartosci_y))
        plik.close()

    def zamien_liste_w_str(self, tablica1):
        stringg = ""
        for i in range(len(tablica1)):
            if i != len(tablica1) - 1:
                stringg = stringg + str(tablica1[i]) + ", "
            else:
                stringg = stringg + str(tablica1[i])
        return stringg


if __name__ == '__main__':
    main = Main()
    # main.wybor_sygnalu()
    # inp = input('Podaj jaki sygnal chcesz rozpatrzec : ')
    # # os.system('cls')  # powinno czyscic ale moze zrobi tylko jak zrobbimy z tego skrypt
    # main.menu_glowne(int(inp))

    sc = SygnalCiagly()
    # dzialania na wykresach
    # sc.szum_o_rozkladzie_jednostajnym(30, 0, 50).dzielenie(sc.sygnal_prostokatny(10, 2, 0, 10)).rysuj_sygnal()
    # print(sc.szum_o_rozkladzie_jednostajnym(30, 0, 50).wariancja())
    # print(sc.szum_o_rozkladzie_jednostajnym(30, 0, 50).wariancja())
    # main.wczytaj_z_pliku()
    # tablica = [0, 1, 2, 3, 4]
    # main.zapisz_do_pliku(0, 10, tablica)
    # sc.sygnal_trojkatny(10, 2, 0, 10).rysuj_histogram(5)
    # main.wczytaj_z_pliku()
    # x = np.linspace(t1, t1 + d, 1000)
    # plt.plot(syg.wartosci_x, syg.wartosci_y)
    # plt.xlim(self.czas_poczatkowy, self.czas_poczatkowy + self.czas_trwania_sygnalu)  # od do X
    # # plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x)-1])  # od do X
    # plt.xlabel('t[s]')
    # plt.ylabel('Amplituda')
    # plt.show()

    # sc.sygnal_prostokatny(15, 5, 0, 20).rysuj_sygnal()
    # sc.sygnal_prostokatny(15, 5, 0, 20).rysuj_histogram(15)
    # sc.sygnal_prostokatny(15, 5, 0, 20).pokazWynikiParametrow()

    # sc.sygnal_sinusoidalny(15, 5, 0, 20).rysuj_histogram(15)
    # sc.sygnal_sinusoidalny(15, 5, 0, 20).pokazWynikiParametrow()
    # sc.sygnal_sinusoidalny(15, 5, 0, 20).rysuj_sygnal()

    # sc.sygnal_trojkatny(15, 5, 0, 20).rysuj_sygnal()
    # sc.sygnal_trojkatny(15, 5, 0, 20).rysuj_histogram(15)
    # sc.sygnal_trojkatny(15, 5, 0, 20).pokazWynikiParametrow()

    sd = SygnalDyskretny()
    # sd.szum_impulsowy(15, 0, 20, 70).rysuj_sygnal()
    # sd.szum_impulsowy(15, 0, 20, 70).rysuj_histogram(15)
    # sd.szum_impulsowy(15, 0, 20, 70).pokazWynikiParametrow()
    # sc.skok_jednostkowy(10, 0, 20, 3).rysuj_sygnal()
    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20).dodawanie(sc.sygnal_prostokatny(15, 5,0,20))
    # syg.rysuj_sygnal()
    # syg.rysuj_histogram(15)
    # syg.pokazWynikiParametrow()

    # syg = sc.sygnal_prostokatny(15, 5, 0, 20).odejmowanie(sc.sygnal_trojkatny(15, 5, 0, 20))
    # syg.rysuj_sygnal()
    # syg.rysuj_histogram(15)
    # syg.pokazWynikiParametrow()

    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20).mnozenie(sc.sygnal_trojkatny(15, 5, 0, 20))
    # syg.rysuj_sygnal()
    # syg.rysuj_histogram(15)
    # syg.pokazWynikiParametrow()
    #
    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20).dzielenie(sc.sygnal_prostokatny(15, 5, 0, 20))
    # syg.rysuj_sygnal()
    # syg.rysuj_histogram(15)
    # syg.pokazWynikiParametrow()

    # sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(5, 10, -5, 15).rysuj_sygnal()
    # sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(5, 10, -5, 15).pokazWynikiParametrow()
    # 1szum_o_rozk_jednost
    # 2szum_gauss
    # 3syg_sinus

    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20).pokazWynikiParametrow()
    # print(syg)
    # sc.sygnal_trojkatny(15, 5, 0, 20).kwantyzacja(10, 5).rysuj_sygnal()
    # sc.sygnal_trojkatny(16, 5, 6, 30).rysuj_sygnal()

    # sc.sygnal_trojkatny(10, 10, 1, 30).kwantyzacja(100, 15).rysuj_sygnal()
    # syg_prob = sc.sygnal_trojkatny(15, 5, 0, 20).ekstrapolacja_zerowego_rzeduNaj(88).rysuj_sygnal()
    print("XD")
    # print(len(sc.sygnal_trojkatny(15, 5, 0, 20).kwantyzacja(70, 5).wartosci_y))
    # print(len(sc.sygnal_trojkatny(15, 5, 0, 20).probkowanie(70).wartosci_y))
    ##ZADANIE 2

    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20)
    # y = syg.wartosci_y
    # x = syg.wartosci_x
    #
    # y2 = sc.sygnal_sinusoidalny(15, 5, 0, 20).kwantyzacja(200, 5).wartosci_y
    # x2 = sc.sygnal_sinusoidalny(15, 5, 0, 20).kwantyzacja(200, 5).wartosci_x
    #
    # plt.plot(x, y, color='red')
    # plt.plot(x2, y2)
    # # plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
    # plt.xlabel('t[s]')
    # plt.ylabel('Amplituda')
    # plt.show()
    #
    # Sygnal.pokaz_wyniki_miar(syg.probkowanie(200),sc.sygnal_sinusoidalny(15, 5, 0, 20).kwantyzacja(200, 5))

    # syg = sc.sygnal_prostokatny(15, 5, 0, 20)
    # y = syg.wartosci_y
    # x = syg.wartosci_x

    # y2 = sc.sygnal_prostokatny(15, 5, 0, 20).rekonstrukcja_w_oparciu_o_fun_sinc(200).wartosci_y
    # x2 = sc.sygnal_prostokatny(15, 5, 0, 20).rekonstrukcja_w_oparciu_o_fun_sinc(200).wartosci_x
    #
    # plt.plot(x, y, color='red')
    # plt.plot(x2, y2)
    # # plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
    # plt.xlabel('t[s]')
    # plt.ylabel('Amplituda')
    # plt.show()
    print("oryginal")
    # print(syg.probkowanie(200).wartosci_y)
    #
    # print(sc.sygnal_prostokatny(15, 5, 0, 20).kwantyzacja(200, 5).wartosci_y)
    # Sygnal.pokaz_wyniki_miar(syg.probkowanie(200), sc.sygnal_prostokatny(15, 5, 0, 20).kwantyzacja(200, 5)) #wychodzi 0?
    #
    # # syg = sc.sygnal_trojkatny(15, 5, 0, 20)
    # # y = syg.wartosci_y
    # # x = syg.wartosci_x
    # #
    # syg_prob = sc.sygnal_prostokatny(15, 5, 0, 20).kwantyzacja(200,5)
    # syg_prob.sygDyskretny = True
    # y2 = syg_prob.wartosci_y
    # x2 = syg_prob.wartosci_x
    # #
    # # y2 = syg.interpolacja_pierwszego_rzeduNaj(200).wartosci_y
    # # x2 = syg.interpolacja_pierwszego_rzeduNaj(200).wartosci_x
    # #
    # plt.plot(x, y, color='red')
    # plt.plot(x2, y2)
    # # plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
    # plt.xlabel('t[s]')
    # plt.ylabel('Amplituda')
    # plt.show()
    #
    # Sygnal.pokaz_wyniki_miar(syg.probkowanie(200), sc.sygnal_trojkatny(15, 5, 0, 20).kwantyzacja(200, 5))
    # syg2 = sc.sygnal_sinusoidalny(2, 0.01, 0, 1) #100hz
    # syg = sc.sygnal_sinusoidalny(2, 0.01, 0, 1).rekonstrukcja_w_oparciu_o_fun_sinc(101)
    # # syg_kwant = sc.sygnal_sinusoidalny(15, 5, 0, 20).kwantyzacja(400, 8)
    # # Sygnal.pokaz_wyniki_miar(syg_probkowany.probkowanie(100), syg_kwant)  # wychodzi 0?
    #
    # y = syg.wartosci_y
    # x = syg.wartosci_x
    # #
    # # y2 = syg_kwant.wartosci_y
    # # x2 = syg_kwant.wartosci_x
    # #
    # y2 = syg2.wartosci_y
    # x2 = syg2.wartosci_x
    # #
    # plt.plot(x, y, color='red')
    # plt.plot(x2, y2)
    # # plt.xlim(self.wartosci_x[0], self.wartosci_x[len(self.wartosci_x) - 1])  # od do X
    # plt.xlabel('t[s]')
    # plt.ylabel('Amplituda')
    # plt.show()
    #
    # print(y)
    # print(x)
    # print(len(x2))
    # print(len(y2))
    # syg = sc.sygnal_sinusoidalny(15, 5, 0, 20)
    # syg2 = sc.sygnal_prostokatny(15, 5, 0, 20)
    # syg3 = Sygnal.operacja_splotu(syg, syg2)
    # syg3.rysuj_sygnal()
    # syg.pokazWynikiParametrow()

    filtr = Filtracja.filtr_dolnoprzepustowy(67, 250, 400)
    syg = sc.sygnal_sinusoidalny(15, 5, 0, 20).probkowanie(400)  # ? ?
    filtr2 = Filtracja.okno_hanninga(filtr)
    print(len(filtr2))
    syg2 = Sygnal.operacja_splotu2(syg, filtr2, 400)
    syg2.rysuj_sygnal()
