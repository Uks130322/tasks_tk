from tkinter import *

wnd = Tk()
wnd.title("Changing picture")
wnd.geometry("400x550+100+30")
wnd.resizable(False, False)

img_1 = PhotoImage(file=r"pictures\\jellyfish_1.png")
img_2 = PhotoImage(file=r"pictures\\jellyfish_2.png")

cnv = Canvas(wnd, bd=2, relief=GROOVE, width=380, height=475)
cnv.pack(side="top", padx=0, pady=0)

btn = Button(wnd, text="CLOSE", font=("Candara", 16),
             command=wnd.destroy, background="lightblue")
btn.pack(side="top", padx=0, pady=5)

Pct = cnv.create_image(3, 0, anchor=NW, image=img_1)


def ms_enter(evt):
    """Event handling about cursor position on the painting area"""

    cnv.itemconfig(Pct, image=img_2)


def ms_leave(evt):
    """Event handling about cursor position off the painting area"""

    cnv.itemconfig(Pct, image=img_1)


cnv.bind("<Enter>", ms_enter)
cnv.bind("<Leave>", ms_leave)

wnd.mainloop()
