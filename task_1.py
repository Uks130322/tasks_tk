from tkinter import *

wnd = Tk()

wnd.title("Important information")
wnd.geometry("400x500+100+50")
wnd.resizable(False, False)

txt = " Please look at this picture before close "
img = PhotoImage(file=r"pictures\\hedgehog.png")

lbl = Label(wnd, text=txt, font=("Candara", 16))
lbl.pack(side="top", padx=0, pady=10)
lbl.configure(background="pink", relief=SOLID)

pic_lbl = Label(image=img)
pic_lbl.pack(side="top", padx=0, pady=3)

btn = Button(wnd, text="CLOSE", font=("Candara", 16),
             command=wnd.destroy, background="lightyellow")
btn.pack(side="top", padx=0, pady=3)


wnd.mainloop()
