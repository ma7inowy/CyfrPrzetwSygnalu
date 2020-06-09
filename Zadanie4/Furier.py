import cmath
import time

import numpy as np

from Sygnal import Sygnal


def show_complex_signal_w1(signal):
    print("W1")
    real_values = [y.real for y in signal.wartosci_y]
    Sygnal(signal.wartosci_x, real_values).rysuj_sygnal()
    img_values = [y.imag for y in signal.wartosci_y]
    Sygnal(signal.wartosci_x, img_values).rysuj_sygnal()


def show_complex_signal_w2(signal):
    print("W2")
    module_values = [np.sqrt(y.real * y.real + y.imag * y.imag) for y in signal.wartosci_y]
    Sygnal(signal.wartosci_x, module_values).rysuj_sygnal()
    arg_values = [np.angle(v) for v in signal.wartosci_y]
    Sygnal(signal.wartosci_x, arg_values).rysuj_sygnal()


class Furier:
    # twiddledfactor to wcoefficient
    # Dyskretna transformata furiera do W1, W2
    def transform(self, signal):
        start = time.time()
        complex_values = self.real_to_complex(signal.wartosci_y)
        values = []
        for i in range(0, len(signal.wartosci_y)):
            cmplx = complex(0, 0)
            for j in range(0, len(signal.wartosci_y)):
                cmplx += complex_values[j] * self.wcoefficient(i, j, len(signal.wartosci_y))
            values.append(cmplx / len(signal.wartosci_y))
        end = time.time()
        print("dyskretna transformata furiera: ", round(end - start, 6))

            # lista_x = []
            # for ii in range(len(values)):
            #     lista_x.append(ii)
        show_complex_signal_w1(Sygnal(signal.wartosci_x, values))
        show_complex_signal_w2(Sygnal(signal.wartosci_x, values))

        return Sygnal(signal.wartosci_x, values)

    # DiscreteFourierBackwardTransformation
    def reverse_transform(self, signal):
        values = []
        for i in range(0, len(signal.wartosci_y)):
            val = 0
            for j in range(0, len(signal.wartosci_y)):
                val += (signal.wartosci_y[j] * self.reverse_wcoefficient(i, j, len(signal.wartosci_y))).real
            values.append(val)
        signal = Sygnal(signal.wartosci_x, values)

        return signal

    # szybka dla czasu a ja mam dla czestotliwosci (F2)
    def fast_transform(self, signal):
        start = time.time()
        complex_values = self.real_to_complex(signal.wartosci_y)
        transformed = self.switch_samples(complex_values)
        values = [x / len(signal.wartosci_y) for x in transformed]
        end = time.time()
        print("szybka transformata furiera: ", round(end - start, 6))

        show_complex_signal_w1(Sygnal(signal.wartosci_x, values))
        show_complex_signal_w2(Sygnal(signal.wartosci_x, values))
        return Sygnal(signal.wartosci_x, values)

    def switch_samples(self, values, reverse=False):
        if len(values) < 2:
            return values
        odd, even = [], []
        for i in range(0, int(len(values) / 2)):
            even.append(values[i * 2])
            odd.append(values[i * 2 + 1])
        value = self.connection(self.switch_samples(even, reverse),
                                self.switch_samples(odd, reverse), reverse)
        return value

    def connection(self, even, odd, reverse):
        values, right_values = [], []
        for i in range(0, len(odd)):
            if not reverse:
                values.append(even[i] + self.wcoefficient(i, 1, len(odd) * 2) * odd[i])
                right_values.append(even[i] - self.wcoefficient(i, 1, len(odd) * 2) * odd[i])
            else:
                values.append(even[i] + self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
                right_values.append(even[i] - self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
        values.extend(right_values)
        return values

    @staticmethod
    def wcoefficient(param, param1, n):
        return cmath.exp(complex(0, -2 * np.pi * param1 * param / n))

    @staticmethod
    def reverse_wcoefficient(param, param1, n):
        return cmath.exp(complex(0, 2 * np.pi * param1 * param / n))

    @staticmethod
    def real_to_complex(values):
        return [(complex(x, 0)) for x in values]

    # transformacja falkowa T3 DB4


lista_H = [0.482, 0.8365, 0.224, -0.129]
lista_G = [-0.129, -0.224, 0.8365, -0.482]


class FalkowaTransformacja:

    def transformation(self, signal):
        start = time.time()
        h_samples = np.convolve(signal.wartosci_y, lista_H)
        g_samples = np.convolve(signal.wartosci_y, lista_G)
        h_half = [x for i, x in enumerate(h_samples) if i % 2 == 0]
        g_half = [x for i, x in enumerate(g_samples) if i % 2 != 0]
        values = []
        for i in range(0, len(g_half)):
            values.append(complex(h_half[i], g_half[i]))
        end = time.time()
        print("dyskretna transformata falkowa: ", round(end - start, 6))
        signal = Sygnal(np.linspace(0, 10, len(values)), values)
        show_complex_signal_w1(signal)
        show_complex_signal_w2(signal)
        return signal

    def reverse_transform(self, signal):
        h_samples, g_samples = [], []
        for i in range(0, len(signal.wartosci_y)):
            h_samples.append(signal.wartosci_y[i].real)
            h_samples.append(0)
            g_samples.append(0)
            g_samples.append(signal.wartosci_y[i].imag)
        h_result = np.convolve(h_samples, list(reversed(lista_H)))
        g_result = np.convolve(g_samples, list(reversed(lista_G)))
        values = [(h_result[i] + g_result[i]) / 2 for i in range(len(g_result))]

        return Sygnal(np.linspace(0, 10, len(values)), values)
