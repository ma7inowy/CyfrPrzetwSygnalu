import matplotlib.pyplot as plt
import numpy as np
import random
import math

from Sygnal import Sygnal


class SygnalDyskretny:

    def impuls_jednostkowy(self, amplituda, t1, d):
        # amplituda, ns, n1, l, f
        # n1 - numer pierwszej probki
        # ns - numer probki, dla ktorej nastepuje skok amplitudy
        # f - czestotliwosc probkowania
        # NAWET Z NICH NIE KORZYSTAMY XDDDDDDDDDD?
        y = []
        # TUTAJ INNY SPOSOB ODLEGLOSCI MIEDZY KROPKAMI! MOZE Z TEGO SKORZYSTAMY? t1+d?
        # ZAOKRAGLAM DO 0 BO TYLKO ZERO MA DAC 1 WIEC INNEJ OPCJI NIE WIDZE???
        # POSTAC UOGOLNIONA???????????????????????????????????
        zakres = int(math.fabs(t1) + d)
        x = np.linspace(t1, t1 + d, zakres)
        for i in range(zakres):
            if int(x[i]) == 0:
                y.append(1)
            else:
                y.append(0)

        sygnal = Sygnal(x, y)
        sygnal.sygDyskretny = True
        return sygnal

    def szum_impulsowy(self, amplituda, t1, d, p):
        # p - prawdopodobienstwo wystapienia A roznego od 0
        y = []
        x = np.linspace(t1, t1 + d, t1 + d)

        for i in range(t1 + d):
            # obliczam rand od 0 do 99, jesli wartosc bedzie wieksza od
            # p(prawdopodobienstwo ktore podalismy) to ustawi na 0
            prawdopodobienstwo_a = random.randrange(100)
            if prawdopodobienstwo_a > p:
                y.append(0)
            else:
                y.append(amplituda)

        sygnal = Sygnal(x, y)
        sygnal.sygDyskretny = True
        return sygnal
