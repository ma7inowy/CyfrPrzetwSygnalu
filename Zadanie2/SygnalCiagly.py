import random
import matplotlib.pyplot as plt
import numpy as np
import math

from Sygnal import Sygnal


class SygnalCiagly:


    def szum_o_rozkladzie_jednostajnym(self, amplituda, t1, d):
        # t1 - czas poczatkowyy
        # d - czas trwania sygnalu
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        for i in range(1000):
            y.append(random.randrange(-amplituda, amplituda + 1))
        return Sygnal(x, y)

    def szum_gaussowski(self, amplituda, t1, d):
        # probl3m bo nigdzie nie zostaine wykorzystana amplituda i o chuj chodzi !!!
        # A ta funkcja to rozklad GESTOSCI prawdopodobienstwa wystapienia jakiejs wartosci amplitudy np w przedziale
        # -10 i 10, ale gdzie niby tutaj dopisac amplitude?
        u = 0
        odch_standard = 1
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        # amp = random.randrange(-amplituda, amplituda + 1)
        for i in range(1000):
            potega_e = -((x[i] - u) ** 2) / 2 * (odch_standard ** 2)
            y.append((1 / (odch_standard * math.sqrt(2 * math.pi))) * math.exp(potega_e))
        return Sygnal(x, y)

    def sygnal_sinusoidalny(self, amplituda, okres_T, t1, d):
        # t - czas podstawowy
        # self.t1 = t1
        # self.d = d
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        for i in range(1000):
            y.append(amplituda * math.sin(2 * math.pi / okres_T * (x[i] - t1)))

        syg = Sygnal(x, y)
        syg.t1 = t1
        syg.d = d
        return syg
        # t_duze - okres, czas trwania jednego drgania

    def sygnal_sinusoidalny_wyprostowany_jednopolowkowo(self, amplituda, okres_T, t1, d):
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        for i in range(1000):
            wzor = 0.5 * amplituda * (math.sin(2 * math.pi / okres_T * (x[i] - t1)) + math.fabs(
                math.sin(2 * math.pi / okres_T * (x[i] - t1))))
            y.append(wzor)
        return Sygnal(x, y)

    def sygnal_sinusoidalny_wyprostowany_dwupolowkowo(self, amplituda, okres_T, t1, d):
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        for i in range(1000):
            wzor = amplituda * math.fabs(math.sin(2 * math.pi / okres_T * (x[i] - t1)))
            y.append(wzor)
        return Sygnal(x, y)

    def sygnal_prostokatny(self, amplituda, okres_T, t1, d):
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        kw = okres_T / 2 / okres_T  # skoro ma byc czas trwania wart max przez okres, dlatego wlasnie takie wzor
        # dlaczego za K nie mozna int(x[i]) tylko int(x[i]/okres_T) skoro k e C
        for i in range(1000):
            k = int(x[i] / okres_T)
            if k * okres_T + t1 <= x[i] < kw * okres_T + okres_T * k + t1:
                y.append(amplituda)
            else:
                y.append(0)
        return Sygnal(x, y)

    def sygnal_prostokatny_symetryczny(self, amplituda, okres_T, t1, d):
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        kw = okres_T / 2 / okres_T

        for i in range(1000):
            k = int(x[i] / okres_T)
            if k * okres_T + t1 <= x[i] < kw * okres_T + okres_T * k + t1:
                y.append(amplituda)
            else:
                y.append(-amplituda)
        return Sygnal(x, y)

    def sygnal_trojkatny(self, amplituda, okres_T, t1, d):
        y = []
        x = np.linspace(t1, t1 + d, 1000)
        kw = (okres_T / 2) / okres_T  # jaki wzor tutaj na kw?

        for i in range(1000):
            k = int((x[i] - t1) / okres_T)
            if ((k * okres_T) + t1) <= x[i] < ((kw * okres_T) + (k * okres_T) + t1):
                wzor = (amplituda / (kw * okres_T)) * (x[i] - (k * okres_T) - t1)
                y.append(wzor)
            else:
                wzor2 = ((-amplituda) / (okres_T * (1 - kw))) * (x[i] - (k * okres_T) - t1) + (amplituda / (1 - kw))
                y.append(wzor2)
        return Sygnal(x, y)

    def skok_jednostkowy(self, amplituda, t1, d, ts):
        y = []
        # polowa_czasu = d / 2
        x = np.linspace(t1, t1 + d, 1000)

        for i in range(1000):
            if x[i] > ts:
                y.append(amplituda)
            elif x[i] == ts:
                y.append(amplituda * 0.5)
            else:
                y.append(0)
        return Sygnal(x, y)
