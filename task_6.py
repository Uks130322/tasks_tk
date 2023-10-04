from tkinter import *

font_for_buttons = ("Candara", 15)
font_for_text = ("Candara", 13, "italic")
clr = "grey80"


def main_window():
    """Main window"""

    def change(evt):

        t = lst.get(lst.curselection())

        for k in range(len(names)):

            if t == names[k]:
                lbl.configure(image=imgs[k])
                break

    path = r"C:\\Users\\User\\Documents\\Python\\content\126\\"

    names = ["macrophages", "neutrophils", "dendritic cells",
             "monocytes", "mast cells", "basophils", "eosinophils",
             "natural killers cells"]

    files = ["126_1.png", "126_2.png", "126_3.png", "126_4.png",
             "126_5.png", "126_6.png", "126_7.png", "126_8.png"]

    wnd = Tk()
    wnd.title("Innate immune system cells")
    wnd.geometry("750x500+100+50")
    wnd.resizable(False, False)
    imgs = [PhotoImage(file=path + f) for f in files]

    index = 0

    lbl = Label(wnd, image=imgs[index])
    lbl.configure(relief=GROOVE)
    lbl.place(x=260, y=10, width=480, height=480)

    frm_list = Frame(wnd, bd=3, relief=GROOVE, height=260, width=210)
    frm_list.place(anchor="nw", x=20, y=40)

    lbl_cells = Label(frm_list, text="Cell name:", font=font_for_buttons)
    lbl_cells.place(anchor="nw", x=10, y=10)

    lst = Listbox(frm_list, selectmode=SINGLE, font=font_for_text)
    lst.configure(bg=clr, selectbackground="gray")
    lst.configure(activestyle="none", height=len(names) + 1)
    lst.place(x=10, y=40)

    for cell in names:
        lst.insert(END, cell)

    lst.select_set(0)
    lst.bind("<<ListboxSelect>>", change)

    btn = Button(wnd, text="Exit", font=font_for_buttons, height=1,
                 width=10, command=wnd.destroy, background=clr)
    btn.place(anchor="n", x=120, y=420)

    wnd.mainloop()


main_window()
