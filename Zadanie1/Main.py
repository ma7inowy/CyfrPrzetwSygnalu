from SygnalCiagly import SynalCiagly
from SygnalDyskretny import SygnalDyskretny


class Main:

    # sc = SynalCiagly()
    # sc.szum_o_rozkladzie_jednostajnym(30, 0, 50)
    # sc.szum_gaussowski(30, 0, 50)
    # sc.sygnal_sinusoidalny(10, 7, 0, 10)
    # sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(10, 6, 0, 10)
    # sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(10, 6, 0, 10)
    # sc.sygnal_prostokatny(10,2,0,10)
    # sc.sygnal_prostokatny_symetryczny(10, 2, 0, 10)
    # sc.sygnal_trojkatny(10, 2, 0, 10)
    # sc.skok_jednostkowy(10, -10, 20)

    # sd = SygnalDyskretny()

    # sd.impuls_jednostkowy(1, -25, 50)
    # sd.szum_impulsowy(1, 0, 50, 80)

    def menu_glowne(self, argument):
        sc = SynalCiagly()
        sd = SygnalDyskretny()

        amp = int(input('Podaj amplitude : '))
        t1 = int(input('Podaj czas poczatkowy : '))
        d = int(input('Podaj czas trwania sygnalu : '))

        if argument == 1:
            sc.szum_o_rozkladzie_jednostajnym(amp, t1, d)
            # sc.szum_o_rozkladzie_jednostajnym(30, 0, 50),
        elif argument == 2:
            sc.szum_gaussowski(amp, t1, d),
            # sc.szum_gaussowski(30, 0, 50),
        elif argument == 3:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny(amp, okres_T, t1, d)
            # sc.sygnal_sinusoidalny(10, 7, 0, 10),
        elif argument == 4:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp, okres_T, t1, d)
            # sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(10, 6, 0, 10),
        elif argument == 5:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amp, okres_T, t1, d)
            # sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(10, 6, 0, 10),
        elif argument == 6:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_prostokatny(amp, okres_T, t1, d)
            # sc.sygnal_prostokatny(10, 2, 0, 10),
        elif argument == 7:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_prostokatny_symetryczny(amp, okres_T, t1, d)
            # sc.sygnal_prostokatny_symetryczny(10, 2, 0, 10),
        elif argument == 8:
            okres_T = int(input('Podaj okres podstawowy : '))
            sc.sygnal_trojkatny(amp, okres_T, t1, d)
            # sc.sygnal_trojkatny(10, 2, 0, 10),
        elif argument == 9:
            sc.skok_jednostkowy(amp, t1, d)
            # sc.skok_jednostkowy(10, -10, 20),
        elif argument == 10:
            sd.impuls_jednostkowy(amp, t1, d)
            # sd.impuls_jednostkowy(1, -25, 50),
        elif argument == 11:
            p = int(input('Podaj prawdopodobienstwo : '))
            sd.szum_impulsowy(amp, t1, d, p)
            # sd.szum_impulsowy(1, 0, 50, 80)
        else:
            print("NACISNIETO ZLY PRZYCISK!!!")


if __name__ == '__main__':
    main = Main()
    inp = input('input a character : ')
    main.menu_glowne(int(inp))

    # chcialem ale nie dziala

    # switcher = {
    #     1: sc.szum_o_rozkladzie_jednostajnym(30, 0, 50),
    #     2: sc.szum_gaussowski(30, 0, 50),
    #     '3': sc.sygnal_sinusoidalny(10, 7, 0, 10),
    #     '4': sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(10, 6, 0, 10),
    #     '5': sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(10, 6, 0, 10),
    #     '6': sc.sygnal_prostokatny(10, 2, 0, 10),
    #     '7': sc.sygnal_prostokatny_symetryczny(10, 2, 0, 10),
    #     '8': sc.sygnal_trojkatny(10, 2, 0, 10),
    #     '9': sc.skok_jednostkowy(10, -10, 20),
    #     '10': sd.impuls_jednostkowy(1, -25, 50),
    #     '11': sd.szum_impulsowy(1, 0, 50, 80)
    # }
    #
    # return switcher.get(argument, "nothing")
