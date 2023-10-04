from tkinter import *
from time import strftime

font_for_buttons = ("Candara", 16)
font_for_text = ("Arial", 15, "bold")

global txt, age, wnd


def main_window():
    """Main window"""

    global txt, age, wnd

    wnd = Tk()

    wnd.title("Find out your birth year!")
    wnd.geometry("400x300+100+50")
    wnd.resizable(False, False)

    asking = " Please enter your age "

    lbl = Label(wnd, text=asking, font=font_for_buttons,
                relief=GROOVE, background="grey80")
    lbl.pack(side="top", padx=0, pady=10)

    txt = Entry(master=wnd, width=10, font=font_for_text)
    txt.pack(side="top", padx=0, pady=10)
    age = ""

    btn_1 = Button(wnd, text="FIND OUT!", command=find_out,
                   background="lightyellow", height=1, width=10,
                   font=font_for_buttons)
    btn_1.pack(side="left", padx=40, pady=10)

    btn_2 = Button(wnd, text="CLOSE", font=font_for_buttons,
                   height=1, width=10, command=wnd.destroy,
                   background="lightyellow")
    btn_2.pack(side="right", padx=40, pady=10)

    wnd.mainloop()


def find_out():
    """Find the year of birth by age"""

    global age, txt, wnd

    age = txt.get()
    now = int(strftime("%Y"))

    try:
        age = int(age)
        birth_year = now - age
        wnd.destroy()

        msg = Tk()
        msg.title("Your birth year")
        msg.geometry("350x180+90+40")
        msg.resizable(False, False)

        lbl_age = Label(master=msg, relief=GROOVE, width=28, height=2,
                        text=f"You were probably born in {birth_year}!",
                        font=font_for_text, background="grey80")
        lbl_age.pack(side="top", padx=0, pady=10)

        btn = Button(master=msg, text="OK", width=10, height=1,
                     font=font_for_buttons, command=msg.destroy,
                     background="lightyellow")
        btn.pack(side="top", padx=0, pady=20)

        msg.mainloop()

    except ValueError:
        error_window()


def error_window():
    """Error window"""

    def try_again():
        """Back to main window"""
        err.destroy()
        main_window()

    global wnd

    wnd.destroy()
    err = Tk()
    err.title("Error")
    err.geometry("350x180+90+40")
    err.resizable(False, False)

    lbl_err = Label(master=err, text="Please enter integer number!",
                    relief=GROOVE, width=28, height=2,
                    font=font_for_text, background="grey80")
    lbl_err.pack(side="top", padx=0, pady=10)

    btn_try = Button(master=err, text="Try again", width=10, height=1,
                     font=font_for_buttons, command=try_again,
                     background="lightyellow")
    btn_try.pack(side="left", padx=40, pady=20)

    btn_exit = Button(master=err, text="CLOSE", width=10, height=1,
                      font=font_for_buttons, command=err.destroy,
                      background="lightyellow")
    btn_exit.pack(side="right", padx=40, pady=20)
    err.mainloop()


main_window()
