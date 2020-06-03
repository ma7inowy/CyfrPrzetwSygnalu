import cmath
import numpy as np

from Sygnal import Sygnal


class Furier:
    # twiddledfactor to wcoefficient
    # Dyskretna transformata furiera do W1, W2
    def transform(self, signal):
        complex_values = self.real_to_complex(signal.wartosci_y)
        values = []
        for i in range(0, len(signal.wartosci_y)):
            cmplx = complex(0, 0)
            for j in range(0, len(signal.wartosci_y)):
                cmplx += complex_values[i] * self.wcoefficient(i, j, len(signal.wartosci_y))
            values.append(cmplx / len(signal.wartosci_y))

            # lista_x = []
            # for ii in range(len(values)):
            #     lista_x.append(ii)

        return Sygnal(signal.wartosci_x, values)

    # szybka dla czasu a ja mam dla czestotliwosci (F2)
    def fast_transform(self, signal):
        complex_values = self.real_to_complex(signal.wartosci_y)
        transformed = self.switch_samples(complex_values)
        values = [x / len(signal.wartosci_y) for x in transformed]
        return Sygnal(signal.wartosci_x, values)

    def switch_samples(self, values, reverse=False):
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
        return [complex(x, 0) for x in values]

    # transformacja falkowa T3 DB4
    Hdb4 = []
