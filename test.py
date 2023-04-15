import tkinter as tk
# --- functions ---

def text_change():
    global text

    text += 1

    if text > 4:
        text = 1

    print("changed to:", text)

    #btn['text'] = text
    btn.config(text=text)


def text_print():
    print("current:", text)

# --- main ---

text = 0

root = tk.Tk()

btn = tk.Button(text="1,2,3 or 4", command=text_change, width=10, height=3)
btn.grid(row=1, column=1)

btn2 = tk.Button(text="SHOW", command=text_print, width=10, height=3)
btn2.grid(row=2, column=1)

root.mainloop()