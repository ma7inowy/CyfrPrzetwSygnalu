from tkinter import *
from tkinter.ttk import Combobox

from Main import Main
from SygnalCiagly import SygnalCiagly

sc = SygnalCiagly()
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
# sygnaly = {}
# sygnaly["1szum_o_rozk_jednost"] = sc.szum_o_rozkladzie_jednostajnym(int(amp1), int(czas_pocz1), int(czas_trwania1))
# sygnaly["2szum_gauss"] = sc.szum_gaussowski(amp1, czas_pocz1, czas_trwania1)

parametry_wypelnione = False







def podaj_parametry():
    settings_root = Tk()
    settings_root.title("Parametry")
    settings_root.geometry("350x250")
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

    label3 = Label(settings_root, text="Okres: ")
    label3.grid(row=3, column=0, padx=12, pady=12)
    okres = Entry(settings_root, width=20)
    okres.grid(row=3, column=1, padx=5, pady=5)

    # czas_pocz1 = czas_pocz.get()

    def zatwierdz2():
        global amp1
        amp1 = int(amp.get())
        global czas_pocz1
        czas_pocz1 = int(czas_pocz.get())
        global czas_trwania1
        czas_trwania1 = int(czas_trwania.get())
        global okres1
        okres1 = int(okres.get())
        global sygnal1
        sygnal1 = chosen_signal.get()
        global sygnal2
        sygnal2 = chosen_signal2.get()

    zatwierdz_button2 = Button(settings_root, text=" OKEJ ", command=zatwierdz2)
    zatwierdz_button2.grid(row=4, column=1, padx=12, pady=12)


def getSygnal1():
    if sygnal1 == "1szum_o_rozk_jednost":
        syg = sc.szum_o_rozkladzie_jednostajnym(amp1, czas_pocz1, czas_trwania1)
    if sygnal1 == "2szum_gauss":
        syg = sc.szum_gaussowski(amp1, czas_pocz1, czas_trwania1)
    if sygnal1 == "3syg_sinus":
        syg = sc.sygnal_sinusoidalny(amp1, okres1, czas_pocz1, czas_trwania1)
    if sygnal1 == "4syg_sinus_wypr_jedn":
        syg = sc.sygnal_sinusoidalny_wyprostowany_jednopolowkowo(amp1, okres1, czas_pocz1, czas_trwania1)
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
    return syg


def rysowanie_wykresu():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        wynik2sygnalow.rysuj_sygnal()
    else:
        getSygnal1().rysuj_sygnal()


def rysowanie_histogramu():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        wynik2sygnalow.rysuj_histogram()
    else:
        getSygnal1().rysuj_histogram(15)


def zapis_do_pliku():
    if sygnal2 != "WYBIERZ2":
        global wynik2sygnalow
        main.zapisz_do_pliku(wynik2sygnalow)
    else:
        main.zapisz_do_pliku(getSygnal1())

def wykonaj_akcje2():
    if akcja2 == "RYSUJ WYKRES":
        rysowanie_wykresu()
    if akcja2 == "RYSUJ HISTOGRAM":
        rysowanie_histogramu()
    if akcja2 == "ZAPISZ DO PLIKU":
        zapis_do_pliku()


def dodawanie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().dodawanie(getSygnal2())


def odejmowanie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().odejmowanie(getSygnal2())


def mnozenie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().mnozenie(getSygnal2())


def dzielenie():
    global wynik2sygnalow
    wynik2sygnalow = getSygnal1().dzielenie(getSygnal2())


def zatwierdz_all():
    print("amplituda", amp1)
    print("czas pocz", czas_pocz1)
    print("czas trwa", czas_trwania1)
    print("okres", okres1)
    global akcja1
    akcja1 = chosen_action.get()
    global akcja2
    akcja2 = chosen_action2.get()

    if akcja1 == "DODAWANIE":
        dodawanie()
    if akcja1 == "ODEJMOWANIE":
        odejmowanie()
    if akcja1 == "MNOZENIE":
        mnozenie()
    if akcja1 == "DZIELENIE":
        dzielenie()

    wykonaj_akcje2()


root = Tk()
root.geometry('300x400')
root.title("Sygnaly")
root.resizable(width=False, height=False)

haj = Label(root)  # pole tekstowe
haj.grid(row=0, column=0)  # czyli gird czyli sitaka robiona (row i column to umiejscowienie na siatce)

# ramka



# Napis w ramce


# input


frame2 = Frame(root, borderwidth=4)
frame2.grid(row=0, column=1)
frame2.config(background="green")  # tlo ramki

listbox = Listbox(root)
listbox.grid(row=1, column=1)
listbox.insert(0, "elo")
listbox.insert(1, "elo2")
listbox.insert(2, "elo3")
listbox.insert(3, "elo4")
# listbox.bind('<<ListboxSelect>>', on_select)


# OPTIONS = [
#     "Jan",
#     "Feb",
#     "Mar"
# ]

# variable = StringVar(frame2)
# variable.set(OPTIONS[0])  # default value
# clicked = StringVar()
# menu = OptionMenu(frame2, clicked, "Monday", "Tuesday")
# menu.grid(row=1,column=0)
# menu.pack()

# pierwszy sygnal
chosen_signal = Combobox(frame2, width=30, state="readonly")
chosen_signal['values'] = ("WYBIERZ1", "1szum_o_rozk_jednost", "2szum_gauss", "3syg_sinus", "4syg_sinus_wypr_jedn")
chosen_signal.grid(row=0, column=1, padx=12, pady=12)
chosen_signal.current(0)
# drugi sygnal
chosen_signal2 = Combobox(frame2, width=30, state="readonly")
chosen_signal2['values'] = ("WYBIERZ2", "1szum_o_rozk_jednost", "2szum_gauss", "3syg_sinus", "4syg_sinus_wypr_jedn")
chosen_signal2.grid(row=1, column=1, padx=12, pady=12)
chosen_signal2.current(0)
# przycisk do ustalania parametrow
parametry_button = Button(frame2, text=" Parametry ", command=podaj_parametry)
parametry_button.grid(row=2, column=1, padx=12, pady=12)

# wybrana akcja
chosen_action = Combobox(frame2, width=20, state="readonly")
chosen_action['values'] = ("AKCJA1", "DODAWANIE",
                           "ODEJMOWANIE", "DZIELENIE", "MNOZENIE")
chosen_action.grid(row=3, column=1, padx=12, pady=12)
chosen_action.current(0)

chosen_action2 = Combobox(frame2, width=20, state="readonly")
chosen_action2['values'] = ("AKCJA", "RYSUJ WYKRES", "RYSUJ HISTOGRAM", "ZAPISZ DO PLIKU")
chosen_action2.grid(row=4, column=1, padx=12, pady=12)
chosen_action2.current(0)

# zatwierdz
zatwierdz_button = Button(frame2, text=" ZATWIERDZ ", command=zatwierdz_all)
zatwierdz_button.grid(row=5, column=1, padx=12, pady=12)

root.mainloop()
