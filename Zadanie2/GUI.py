import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Main import Main
from Sygnal import Sygnal
from SygnalCiagly import SygnalCiagly
from SygnalDyskretny import SygnalDyskretny

sc = SygnalCiagly()
sd = SygnalDyskretny()
main = Main()
sygnal1 = ""
sygnal2 = ""
amp1 = 0
czas_pocz1 = 0
czas_trwania1 = 0
okres1 = 0
akcja1 = ""
akcja2 = ""
wynik2sygnalow = 0
wsp_wyp1 = 0
prawdopo1 = 0
ilosc_przedzialow1 = 0
konwersja = ""

# sygnal po konwersji
syg_konwersja = 0


def podaj_parametry():
    settings_root = Tk()
    settings_root.title("Parametry")
    settings_root.geometry("350x350")
    settings_root.resizable(False, False)

    label1 = Label(settings_root, text="Amplituda: ")
    label1.grid(row=0, column=0, padx=12, pady=12)
    amp = Entry(settings_root, width=20)
    amp.grid(row=0, column=1, padx=5, pady=5)

    label2 = Label(settings_root, text="Czas początkowy: ")
    label2.grid(row=1, column=0, padx=12, pady=12)
    czas_pocz = Entry(settings_root, width=20)
    czas_pocz.grid(row=1, column=1, padx=5, pady=5)

    label3 = Label(settings_root, text="Czas trwania sygnału: ")
    label3.grid(row=2, column=0, padx=12, pady=12)
    czas_trwania = Entry(settings_root, width=20)
    czas_trwania.grid(row=2, column=1, padx=5, pady=5)

    label4 = Label(settings_root, text="Okres: ")
    label4.grid(row=3, column=0, padx=12, pady=12)
    okres = Entry(settings_root, width=20)
    okres.grid(row=3, column=1, padx=5, pady=5)

    label5 = Label(settings_root, text="Wsp. wypełnienia: ")
    label5.grid(row=4, column=0, padx=12, pady=12)
    wsp_wyp = Entry(settings_root, width=20)
    wsp_wyp.grid(row=4, column=1, padx=5, pady=5)

    label6 = Label(settings_root, text="Prawdopodobieństwo: ")
    label6.grid(row=5, column=0, padx=12, pady=12)
    prawdopo = Entry(settings_root, width=20)
    prawdopo.grid(row=5, column=1, padx=5, pady=5)

    def zatwierdzParam():
        try:
            global amp1
            amp1 = int(amp.get())
            global czas_pocz1
            czas_pocz1 = int(czas_pocz.get())
            global czas_trwania1
            czas_trwania1 = int(czas_trwania.get())
            global okres1
            okres1 = int(okres.get())
            global wsp_wyp1
            wsp_wyp1 = int(wsp_wyp.get())
            global prawdopo1
            prawdopo1 = int(prawdopo.get())
        except Exception:
            messagebox.showinfo("ERROR", 'WYPEŁNIJ WSZYSKTIE POLA!!!\n(NIEPOTRZEBNE DANE WYPEŁNIIJ: 0)')

    zatwierdz_button2 = Button(settings_root, text=" AKCEPTUJ ", command=zatwierdzParam)
    zatwierdz_button2.grid(row=6, column=1, padx=12, pady=12)


def getSygnal1():
    if sygnal1 == "1szum_o_rozk_jednost":
        syg = sc.szum_o_rozkladzie_jednostajnym(amp1, czas_pocz1, czas_trwania1)
    if sygnal1 == "2szum_gauss":
        syg = sc.szum_gaussowski(amp1, czas_pocz1, czas_trwania1)
    if sygnal1 == "3syg_sinus":
        syg = sc.sygnal_sinusoidalny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "4syg_sinus_wypr_jedn":
        syg = sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "5syg_sinus_wypr_dwu":
        syg = sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "6syg_prostokat":
        syg = sc.sygnal_prostokatny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "7syg_prostokat_sym":
        syg = sc.sygnal_prostokatny_symetryczny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "8syg_trojkat":
        syg = sc.sygnal_trojkatny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "9skok_jednost":
        syg = sc.skok_jednostkowy(amp1, czas_pocz1, czas_trwania1, wsp_wyp1)
    if sygnal1 == "10impuls_jedn":
        syg = sd.impuls_jednostkowy(amp1, czas_pocz1, czas_trwania1)
    if sygnal1 == "11szum_impuls":
        syg = sd.szum_impulsowy(amp1, czas_pocz1, czas_trwania1, prawdopo1)
    if sygnal1 == "12WCZYTAJ_Z_ZAPIS1.TXT":
        syg = main.wczytaj_z_pliku("zapis1.txt")
    if sygnal1 == "13WCZYTAJ_Z_ZAPIS2.TXT":
        syg = main.wczytaj_z_pliku("zapis2.txt")

    return syg


def getSygnal2():
    if sygnal2 == "1szum_o_rozk_jednost":
        syg = sc.szum_o_rozkladzie_jednostajnym(amp1, czas_pocz1, czas_trwania1)
    if sygnal2 == "2szum_gauss":
        syg = sc.szum_gaussowski(amp1, czas_pocz1, czas_trwania1)
    if sygnal2 == "3syg_sinus":
        syg = sc.sygnal_sinusoidalny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "4syg_sinus_wypr_jedn":
        syg = sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "5syg_sinus_wypr_dwu":
        syg = sc.sygnal_sinusoidalny_wyprostowany_dwupolowkowo(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "6syg_prostokat":
        syg = sc.sygnal_prostokatny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "7syg_prostokat_sym":
        syg = sc.sygnal_prostokatny_symetryczny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "8syg_trojkat":
        syg = sc.sygnal_trojkatny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal2 == "9skok_jednost":
        syg = sc.skok_jednostkowy(amp1, czas_pocz1, czas_trwania1, wsp_wyp1)
    if sygnal2 == "10impuls_jedn":
        syg = sd.impuls_jednostkowy(amp1, czas_pocz1, czas_trwania1)
    if sygnal2 == "11szum_impuls":
        syg = sd.szum_impulsowy(amp1, czas_pocz1, czas_trwania1, prawdopo1)
    if sygnal2 == "12WCZYTAJ_Z_ZAPIS2.TXT":
        syg = main.wczytaj_z_pliku("zapis2.txt")
    return syg


def rysowanie_wykresu():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        wynik2sygnalow.rysuj_sygnal()
    elif konwersja != "KONWERSJA":
        global syg_konwersja
        syg_konwersja.rysuj_sygnal()
    else:
        getSygnal1().rysuj_sygnal()


def rysowanie_histogramu():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        wynik2sygnalow.rysuj_histogram(ilosc_przedzialow1)
    else:
        print("rysuj 1")
        getSygnal1().rysuj_histogram(ilosc_przedzialow1)


def zapis_do_pliku():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        main.zapisz_do_pliku(wynik2sygnalow, "zapis1.txt")
    else:
        main.zapisz_do_pliku(getSygnal1(), "zapis1.txt")


def zapis_do_pliku2():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        main.zapisz_do_pliku(wynik2sygnalow, "zapis2.txt")
    else:
        main.zapisz_do_pliku(getSygnal1(), "zapis2.txt")


def wykonaj_akcje2():
    if akcja2 == "RYSUJ WYKRES":
        rysowanie_wykresu()
    elif akcja2 == "RYSUJ HISTOGRAM":
        rysowanie_histogramu()
    elif akcja2 == "ZAPISZ DO PLIKU ZAPIS1.TXT":
        zapis_do_pliku()
    elif akcja2 == "ZAPISZ DO PLIKU ZAPIS2.TXT":
        zapis_do_pliku2()


def dodawanie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().dodawanie(getSygnal2())
    print("+")


def odejmowanie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().odejmowanie(getSygnal2())
    print("-")


def mnozenie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().mnozenie(getSygnal2())


def dzielenie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().dzielenie(getSygnal2())


def wyswietl_otrzymane_parametry():
    if sygnal2 != "WYBIERZ2":
        messagebox.showinfo("Otrzymane parametry:", wynik2sygnalow.pokazWynikiParametrow())
    elif konwersja != "KONWERSJA":
        global syg_konwersja
        messagebox.showinfo("Otrzymane miary: ",
                            syg_konwersja.pokaz_wyniki_miar(getSygnal1().probkowanie(200), getSygnal1().kwantyzacja(200, 8)))
    else:
        messagebox.showinfo("Otrzymane parametry:", getSygnal1().pokazWynikiParametrow())


def wykonaj_konwersje():
    global konwersja
    global sygnal1
    global syg_konwersja
    konwersja = chosen_action_zad2.get()
    if konwersja == "PROBKOWANIE":
        syg_konwersja = getSygnal1().probkowanie(200)
    elif konwersja == "KWANTYZACJA":
        syg_konwersja = getSygnal1().kwantyzacja(200, 8)
    elif konwersja == "EKSTR. 0 RZEDU":
        syg_konwersja = getSygnal1().ekstrapolacja_zerowego_rzeduNaj(300)
    elif konwersja == "INTERP. 1 RZEDU":
        syg_konwersja = getSygnal1().interpolacja_pierwszego_rzeduNaj(300)
    elif konwersja == "REKONSTR. SINC":
        syg_konwersja = getSygnal1().rekonstrukcja_w_oparciu_o_fun_sinc(300)


# TU SIE DZIEJE WSZYSTKO PO KOLEI PO KLIKNIECIU PRZYCISKU URUCHOMO
def zatwierdz_all():
    print("amplituda", amp1)
    print("czas pocz", czas_pocz1)
    print("czas trwa", czas_trwania1)
    print("okres", okres1)
    global sygnal1
    sygnal1 = chosen_signal.get()
    global sygnal2
    sygnal2 = chosen_signal2.get()
    global akcja1
    akcja1 = chosen_action.get()
    global akcja2
    akcja2 = chosen_action2.get()
    global ilosc_przedzialow1
    ilosc_przedzialow1 = int(hist_box.get())

    if akcja1 == "DODAWANIE":
        dodawanie()
    elif akcja1 == "ODEJMOWANIE":
        odejmowanie()
    elif akcja1 == "MNOZENIE":
        mnozenie()
    elif akcja1 == "DZIELENIE":
        dzielenie()

    wykonaj_konwersje()  # sprawdza czy moze wykonac, jesli tak to wykonuje
    wyswietl_otrzymane_parametry()
    wykonaj_akcje2()


root = Tk()
var_zad2 = IntVar()
root.config(background="grey")
root.geometry('530x310')
root.title("Gen. sygnału i szumu")
root.resizable(width=True, height=True)

chosen_signal = Combobox(root, width=25, state="readonly")
chosen_signal['values'] = (
    "WYBIERZ1", "1szum_o_rozk_jednost", "2szum_gauss", "3syg_sinus", "4syg_sinus_wypr_jedn", "5syg_sinus_wypr_dwu",
    "6syg_prostokat", "7syg_prostokat_sym", "8syg_trojkat", "9skok_jednost", "10impuls_jedn", "11szum_impuls",
    "12WCZYTAJ_Z_ZAPIS1.TXT", "13WCZYTAJ_Z_ZAPIS2.TXT")
chosen_signal.grid(row=0, column=1, padx=5, pady=10)
chosen_signal.current(0)

signal_label = Label(root, text="WYBIERZ SYGNAŁ1: ")
signal_label.grid(row=0, column=0, padx=1, pady=1)

# drugi sygnal
chosen_signal2 = Combobox(root, width=25, state="readonly")
chosen_signal2['values'] = (
    "WYBIERZ2", "1szum_o_rozk_jednost", "2szum_gauss", "3syg_sinus", "4syg_sinus_wypr_jedn", "5syg_sinus_wypr_dwu",
    "6syg_prostokat", "7syg_prostokat_sym", "8syg_trojkat", "9skok_jednost", "10impuls_jedn", "11szum_impuls",
    "12WCZYTAJ_Z_ZAPIS2.TXT")
chosen_signal2.grid(row=1, column=1, padx=5, pady=10)
chosen_signal2.current(0)

signal_label2 = Label(root, text="WYBIERZ SYGNAŁ2: ")
signal_label2.grid(row=1, column=0, padx=1, pady=1)

# checkbox do zad2 ZE JESLI ZAZNACZONE TO MA ENABLE TE KONWERSJE A JAK ODZNACZONE TO DISABLE TE KONWERSJEE


check_zad2 = Checkbutton(root, text="Konwersja", variable=var_zad2)
check_zad2.grid(row=2, column=0)

# wybrana akcja do zadania2
chosen_action_zad2 = Combobox(root, width=25, state="readonly")
chosen_action_zad2['values'] = ("KONWERSJA", "PROBKOWANIE",
                                "KWANTYZACJA", "EKSTR. 0 RZEDU", "INTERP. 1 RZEDU", "REKONSTR. SINC")
chosen_action_zad2.grid(row=2, column=3, padx=5, pady=10)
chosen_action_zad2.current(0)

# do zadania 2
action_label = Label(root, text="ZAD2: ")
action_label.grid(row=2, column=2, padx=1, pady=1)

# przycisk do ustalania parametrow
parametry_button = Button(root, text=" Parametry ", command=podaj_parametry)
parametry_button.grid(row=2, column=1, padx=5, pady=10)

# wybrana akcja
chosen_action = Combobox(root, width=25, state="readonly")
chosen_action['values'] = ("AKCJA1", "DODAWANIE",
                           "ODEJMOWANIE", "DZIELENIE", "MNOZENIE")
chosen_action.grid(row=3, column=1, padx=5, pady=10)
chosen_action.current(0)

action_label = Label(root, text="DZIAŁANIE: ")
action_label.grid(row=3, column=0, padx=1, pady=1)

chosen_action2 = Combobox(root, width=25, state="readonly")
chosen_action2['values'] = (
    "AKCJA2", "RYSUJ WYKRES", "RYSUJ HISTOGRAM", "ZAPISZ DO PLIKU ZAPIS1.TXT", "ZAPISZ DO PLIKU ZAPIS2.TXT")
chosen_action2.grid(row=4, column=1, padx=5, pady=10)
chosen_action2.current(0)

action_label = Label(root, text="OPERACJA: ")
action_label.grid(row=4, column=0, padx=1, pady=1)

# zatwierdz
uruchom_button = Button(root, text=" URUCHOM ", command=zatwierdz_all)
uruchom_button.grid(row=6, column=1, padx=5, pady=10)

hist_box = Combobox(root, width=25, state="readonly")
hist_box['values'] = (
    "0", "5", "10", "15", "20")
hist_box.grid(row=5, column=1, padx=5, pady=10)
hist_box.current(0)

ilosc_przedz_label = Label(root, text="ILOŚĆ PRZEDZ.: ")
ilosc_przedz_label.grid(row=5, column=0, padx=1, pady=1)


def running_in_background():
    if chosen_signal2.get() == "WYBIERZ2":
        chosen_action.set("AKCJA1")
        chosen_action.configure(state="disabled")
    else:
        chosen_action.configure(state="normal")

    if chosen_action2.get() != "RYSUJ HISTOGRAM":
        hist_box.configure(state="disabled")
        hist_box.set("0")
    else:
        hist_box.configure(state="normal")
    if var_zad2.get() == 0:
        chosen_action_zad2.set("KONWERSJA")
        chosen_action_zad2.configure(state="disabled")
    else:
        chosen_action_zad2.configure(state="enable")

    root.after(500, running_in_background)


root.after(500, running_in_background)
root.mainloop()
