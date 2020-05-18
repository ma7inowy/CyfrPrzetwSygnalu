import math
import numpy as np
from Sygnal import Sygnal


class Antena:
    def __init__(self, czestotliwosc_probkowania, dlugosc_bufforu, liczba_pomiarow, okres, predkosc_rzeczywista):
        self.czestotliwosc_probkowania = czestotliwosc_probkowania
        self.dlugosc_bufforu = dlugosc_bufforu
        self.liczba_pomiarow = liczba_pomiarow
        self.okres = okres
        self.predkosc_rzeczywista = predkosc_rzeczywista

    def create_signal(self, start_time, duration):
        values, values1, values2, res, x = [], [], [], [], []
        j = start_time
        while j < start_time + duration:
            values.append(3 * math.sin(2 * math.pi * j / 4))
            values1.append(2 * math.sin(2 * math.pi * j / 2))
            values2.append(1 * math.sin(2 * math.pi * j / 1))
            res.append(values[-1] + values1[-1] + values2[-1])
            x.append(j)
            j += 1 / self.czestotliwosc_probkowania
        return Sygnal(x, res)

    def count_distance(self, abstract_speed):
        result_distances = []
        duration = self.dlugosc_bufforu / self.czestotliwosc_probkowania
        for i in range(0, self.liczba_pomiarow * self.okres, self.okres):
            delay = i * self.predkosc_rzeczywista * 2 / abstract_speed
            correlation_samples = Sygnal.korelacja_z_uzyciem_splotu(
                self.create_signal(i - duration, duration),
                self.create_signal(i - delay, duration))
            result_distances.append(self.calculate_distance(correlation_samples.wartosci_y, abstract_speed))
        return result_distances

    def calculate_distance(self, twined_values, abstract_speed):
        second_half = twined_values[int(len(twined_values) / 2):]
        max_sample = np.argmax(second_half)
        t_delay = max_sample / self.czestotliwosc_probkowania
        return t_delay

    def original_distance(self):
        values = []
        for i in range(0, self.liczba_pomiarow * self.okres, self.okres):
            values.append(i * self.predkosc_rzeczywista)
        return values

    def antene_diffrence(self, speed_abs):
        values1 = self.original_distance()
        print(values1)
        values2 = self.count_distance(speed_abs)
        res_list = [math.fabs(values1[i] - values2[i]) for i in range(len(values1))]
        return res_list
