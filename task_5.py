from tkinter import *

font_for_buttons = ("Candara", 15)
font_for_text = ("Arial", 15, "bold")
clr = "pink"


def main_window():
    """Main window"""

    global font_for_text

    def smaller():
        """Make text smaller"""

        global font_for_text

        font_for_text = (font_for_text[0], font_for_text[1] - 1, font_for_text[2])
        lbl.configure(font=font_for_text)

    def bigger():
        """Make text smaller"""

        global font_for_text

        font_for_text = (font_for_text[0], font_for_text[1] + 1, font_for_text[2])
        lbl.configure(font=font_for_text)

    wnd = Tk()

    wnd.title("How big is your text")
    wnd.geometry("400x300+100+50")
    wnd.resizable(False, False)

    example = " You can make this text \nsmaller or bigger "

    lbl = Label(wnd, text=example, font=font_for_text, height=3,
                width=30, relief=FLAT)
    lbl.place(anchor="n", x=200, y=10)

    btn_1 = Button(wnd, text="Smaller", command=smaller, background=clr,
                   height=1, width=10, font=font_for_buttons)
    btn_1.place(anchor="n", x=100, y=130)

    btn_2 = Button(wnd, text="Bigger", font=font_for_buttons, height=1,
                   width=10, command=bigger, background=clr)
    btn_2.place(anchor="n", x=300, y=130)

    btn_3 = Button(wnd, text="CLOSE", font=font_for_buttons, height=1,
                   width=10, command=wnd.destroy, background=clr)
    btn_3.place(anchor="n", x=200, y=210)

    wnd.mainloop()


main_window()
