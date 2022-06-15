# Inspired by : https://youtu.be/Xf8dhNl4d9c
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import pyglet as pg
import cv2
import os

# font
pg.font.add_file('fonts//Poppins-Bold.ttf')
pg.font.add_file('fonts//Poppins-Regular.ttf')

# styles
bg_color = "#186178"
btn_color = "#029522"
font_title = "Poppins Bold"
font_common = "Poppins Regular"
fg_color = "#FFFFFF"

# main display
root = Tk()
root.geometry("500x500")
root.configure(bg=bg_color)
root.title("JENERET Certificate Generator")

titleApp = Label(root, text="JENERET", font=(font_title, 18), fg=fg_color, bg=bg_color)
titleApp.grid(column=0, row=0)
titleApp.place(relx=0.5, rely=0.1, anchor=CENTER)

descApp = Label(root, text="Certificate Generator", font=(font_common, 15), fg=fg_color, bg=bg_color)
descApp.grid(column=0, row=0)
descApp.place(relx=0.5, rely=0.17, anchor=CENTER)

# input file
def inputcert():
    try:
        template_cert = fd.askopenfilename(initialdir="/", 
                                        title="Choose template", 
                                        filetypes=[("PNG", "*.png"),
                                        ("All Files", "*.*")])
        Label(root, text=template_cert, font=(font_common, 7), bg=bg_color, fg=fg_color, width=50).place(relx=.05, rely=.3)
    except FileNotFoundError:
        print("File not found :(")
    else:
        return template_cert

# input nama
listName = []
def inputname():
    # try:
    inputNama = fd.askopenfilename(initialdir="/",
                                title="List Nama...", 
                                filetypes=[("Text Document", "*.txt"),
                                ("All Files", "*.*")])
    # Label(root, text=inputNama, font=(font_common, 7), bg=bg_color, fg=fg_color, width=100).pack(side=RIGHT)
    Label(root, text=inputNama, font=(font_common, 7), bg=bg_color, fg=fg_color, width=50).place(relx=.05, rely=.5)
    return inputNama
    # except:
        # mb.showerror("JENERET | Error","Something error")

def cleanup_data():  
    with open(inputname()) as f:
        for line in f:
            listName.append(line)

# generate!
def generate_cert():
    # cleanup_data()
    for name in enumerate(listName):
        certificate_template_image = cv2.imread()
        cv2.putText(certificate_template_image, name.strip(), (470,514), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.imwrite(f"generated-cert/{name.strip()}.png", certificate_template_image)
        # print(f"Processing {index+1} / {len(listName)}")

# keluar
def exit():
    konfirmasi = mb.askyesno("JENERET | Exit?", "Want to exit?")
    if konfirmasi:
        root.destroy()

# template serti
labelTemplate = Label(root, text="Insert certificate template", font=(font_title, 10), bg=bg_color, fg=fg_color)
labelTemplate.place(relx=.05, rely=.25)
btnList = Button(root, text="Choose file...", font=(font_title, 10), command=inputcert, width=15)
btnList.grid(column=0, row=1)
btnList.place(relx=.6, rely=.3)

# list nama
labelName = Label(root, text="Insert names", font=(font_title, 10), bg=bg_color, fg=fg_color)
labelName.place(relx=.05, rely=.43)
btnNama = Button(root, text="Choose File...", font=(font_title, 10), command=inputname, width=15)
btnNama.grid(column=0, row=1)
btnNama.place(relx=.6, rely=.5)

# directory penyimpanan fix
# btnDir = Button(root, text="Cari direktori..", font=(font_title, 10), command=savecert, width=15)
# btnDir.grid(column=0, row=1)
# btnDir.place(relx=.6, rely=.5)

# generate!
btnGenerate = Button(root, text="Generate!", font=(font_title, 10), command=cleanup_data, bg="#029522", fg=fg_color, width=15)
btnGenerate.grid(column=0, row=1)
btnGenerate.place(relx=.5, rely=.7, anchor=CENTER)

# exit
btnExit = Button(root, text="Exit", font=(font_title, 10), command=exit, bg="#FF0000", fg=fg_color, width=15)
btnExit.grid(column=0, row=1)
btnExit.place(relx=.5, rely=.8, anchor=CENTER)

if __name__ == '__main__':
    root.mainloop()