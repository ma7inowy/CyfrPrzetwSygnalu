import cmath


class Filtracja:

    @staticmethod
    def filtr_dolnoprzepustowy(m, fo, fp, k=-1):
        # fp - czestotliwosc probkowania sygnalu
        # fo - czestotliwosc odciecia filtru
        # m - liczba przeszlych probek sygnalu wejsciowego
        lista_y = []
        if k == -1:
            k = fp / fo
        for i in range(m+1):
            if i == ((m - 1) / 2):
                lista_y.append(2.0 / k)
            else:
                lista_y.append(cmath.sin(2 * cmath.pi * (i - (m - 1) / 2) / k) / (cmath.pi * (i - (m - 1) / 2)))
        return lista_y
    @staticmethod
    def filtr_srodkowoprzepustowy(m, fo, fp):
        lista_y_filtrowana = Filtracja.filtr_dolnoprzepustowy(m, fo, fp, fp / (fp / 4 - fo))
        nowa_lista_y = []

        for i in range(len(lista_y_filtrowana)):
            wartosc_y = lista_y_filtrowana[i] * 2 * cmath.sin((cmath.pi * i) / 2.0)
            nowa_lista_y.append(wartosc_y)

        return nowa_lista_y
    @staticmethod
    def okno_hanninga(pofiltrowane_wartosci):
        nowa_lista_y_filtrowana = []
        for i in range(len(pofiltrowane_wartosci)):
            wartosc = 0.5-(0.5*cmath.cos((2*cmath.pi*i)/(1.0*len(pofiltrowane_wartosci))))
            nowa_lista_y_filtrowana.append(wartosc*pofiltrowane_wartosci[i])

        return nowa_lista_y_filtrowana
