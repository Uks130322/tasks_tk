from tkinter import *
from random import randrange

font_for_buttons = ("Candara", 15, "bold")
font_for_text = ("Candara", 14)
font_for_scale = ("Candara", 12)
clr = "grey80"


def main_window():
    """Main window"""

    global wnd

    rand_color = []
    user_color = []

    def random_color() -> str:
        """Choose random color"""

        nonlocal rand_color

        result = "#"

        for i in range(3):
            color = randrange(255)
            rand_color += [color]
            result += f"{color:02x}"

        return result

    def get_color(*args) -> str:
        """Get current color"""

        nonlocal user_color
        user_color = [int(scl_red.get()), int(scl_green.get()),
                      int(scl_blue.get())]

        get_red = f"{scl_red.get():02x}"
        get_green = f"{scl_green.get():02x}"
        get_blue = f"{scl_blue.get():02x}"
        your_color = "#" + get_red + get_green + get_blue

        frm_your.configure(background=your_color)

        return your_color

    def check():
        """Compare random color and user's color"""

        differ = 0

        for index in range(3):
            differ += abs(rand_color[index] - user_color[index])

        if differ <= 10:
            txt = "You are pro"
        elif differ <= 22:
            txt = "You a normal"
        else:
            txt = "You are not so good"

        result_window(txt)

    wnd = Tk()

    wnd.title("Color check")
    wnd.geometry("500x550+100+50")
    wnd.resizable(False, False)

    lbl = Label(wnd, text="Please try to make the same color:",
                relief=FLAT, width=40, height=2, font=font_for_buttons)
    lbl.place(anchor="n", x=250, y=0)

    lbl_my = Label(wnd, text="my color:", relief=FLAT, width=15,
                   height=1, font=font_for_text)
    lbl_my.place(anchor="n", x=125, y=60)

    lbl_your = Label(wnd, text="your color:", relief=FLAT, width=15,
                     height=1, font=font_for_text)
    lbl_your.place(anchor="n", x=375, y=60)

    frm_choose = Frame(wnd, bd=2, relief=FLAT, width=440,
                       height=220)
    frm_choose.place(anchor="n", x=250, y=230)

    lbl_red = Label(frm_choose, text="red", relief=FLAT, width=7,
                    height=1, font=font_for_text)
    lbl_red.place(anchor="n", x=30, y=20)

    lbl_green = Label(frm_choose, text="green", relief=FLAT, width=7,
                      height=1, font=font_for_text)
    lbl_green.place(anchor="n", x=30, y=90)

    lbl_blue = Label(frm_choose, text="blue", relief=FLAT, width=7,
                     height=1, font=font_for_text)
    lbl_blue.place(anchor="n", x=30, y=160)

    scl_red = Scale(frm_choose, orient=HORIZONTAL, from_=0, to=255,
                    tickinterval=50, resolution=1, width=20, length=350,
                    font=font_for_scale)
    scl_red.place(anchor="n", x=250, y=0)
    scl_red.config(command=get_color)

    scl_green = Scale(frm_choose, orient=HORIZONTAL, from_=0, to=255,
                      tickinterval=50, resolution=1, width=20, length=350,
                      font=font_for_scale)
    scl_green.place(anchor="n", x=250, y=70)
    scl_green.config(command=get_color)

    scl_blue = Scale(frm_choose, orient=HORIZONTAL, from_=0, to=255,
                     tickinterval=50, resolution=1, width=20, length=350,
                     font=font_for_scale)
    scl_blue.place(anchor="n", x=250, y=140)
    scl_blue.config(command=get_color)

    frm_my = Frame(wnd, bd=2, relief=GROOVE, background=random_color(),
                   width=120, height=120)
    frm_my.place(anchor="n", x=125, y=100)

    frm_your = Frame(wnd, bd=2, relief=GROOVE, background="black",
                     width=120, height=120)
    frm_your.place(anchor="n", x=375, y=100)

    btn_check = Button(wnd, text="Check", font=font_for_buttons,
                       height=1, width=10, command=check)
    btn_check.place(anchor="n", x=125, y=480)

    btn_exit = Button(wnd, text="Exit", font=font_for_buttons,
                      height=1, width=10, command=wnd.destroy)
    btn_exit.place(anchor="n", x=375, y=480)

    wnd.mainloop()


def result_window(txt: str):
    """Window with result"""

    def try_again():
        """Function to try again"""

        res_wnd.destroy()
        main_window()

    wnd.destroy()

    res_wnd = Tk()

    res_wnd.title("Result")
    res_wnd.geometry("300x210+100+50")
    res_wnd.resizable(False, False)

    lbl = Label(res_wnd, text=txt, relief=GROOVE, width=20, height=2,
                font=font_for_text)
    lbl.place(anchor="n", x=150, y=20)

    btn_again = Button(res_wnd, text="Try again", font=font_for_buttons,
                       height=1, width=10, command=try_again)
    btn_again.place(anchor="n", x=75, y=120)

    btn_exit = Button(res_wnd, text="Exit", font=font_for_buttons,
                      height=1, width=10, command=res_wnd.destroy)
    btn_exit.place(anchor="n", x=225, y=120)

    res_wnd.mainloop()


main_window()
