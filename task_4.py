from tkinter import *

font_for_buttons = ("Candara", 16)
font_for_text = ("Arial", 15, "bold")
clr = "lightgreen"


def main_window():
    """Main window"""

    def clean():
        """Delete text"""

        nonlocal lbl_txt, txt

        txt.destroy()
        txt = Entry(master=wnd, width=30, font=font_for_text)
        txt.place(anchor="n", x=200, y=90)
        txt.bind("<KeyPress>", printing)

        lbl_txt.configure(text="")

    def printing(evt):
        """Event handling about cursor position off the painting area"""

        nonlocal lbl_txt, txt

        some_txt = txt.get()
        lbl_txt.configure(text=some_txt)

    wnd = Tk()

    wnd.title("Print text")
    wnd.geometry("400x300+100+50")
    wnd.resizable(False, False)

    asking = " Please enter some text "

    lbl = Label(wnd, text=asking, font=font_for_buttons, height=2,
                width=30, relief=GROOVE, background=clr)
    lbl.place(anchor="n", x=200, y=10)

    txt = Entry(master=wnd, width=30, font=font_for_text)
    txt.place(anchor="n", x=200, y=90)

    lbl_txt = Label(wnd, text="", font=font_for_buttons, height=2,
                    width=30, relief=GROOVE, background=clr)
    lbl_txt.place(anchor="n", x=200, y=140)

    btn_1 = Button(wnd, text="Clean", command=clean, background=clr,
                   height=1, width=10, font=font_for_buttons)
    btn_1.place(anchor="n", x=100, y=230)

    btn_2 = Button(wnd, text="CLOSE", font=font_for_buttons, height=1,
                   width=10, command=wnd.destroy, background=clr)
    btn_2.place(anchor="n", x=300, y=230)

    txt.bind("<KeyRelease>", printing)

    wnd.mainloop()


main_window()
