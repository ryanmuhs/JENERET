# Inspired by : https://youtu.be/Xf8dhNl4d9c
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import pyglet as pg
import cv2

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

judulApp = Label(root, text="JENERET", font=(font_title, 18), fg=fg_color, bg=bg_color)
judulApp.grid(column=0, row=0)
judulApp.place(relx=0.5, rely=0.1, anchor=CENTER)

descApp = Label(root, text="Certificate Generator", font=(font_common, 15), fg=fg_color, bg=bg_color)
descApp.grid(column=0, row=0)
descApp.place(relx=0.5, rely=0.17, anchor=CENTER)

# input file
def inputcert():
    try:
        template_cert = fd.askopenfilename(initialdir="\\coba-2", 
                                        title="Pilih soal", 
                                        filetypes=[("PNG", "*.png"),
                                        ("All Files", "*.*")])
        Label(root, text=template_cert, font=(font_common, 7), bg=bg_color, fg=fg_color).place(relx=.12, rely=.3)
    except FileNotFoundError:
        print("Filenya ga ada :D")
    else:
        return template_cert

# input nama
def inputname():
    try:
        inputNama = fd.askopenfilename(initialdir="\\",
                                    title="Pilih soal", 
                                    filetypes=[("Text Document", "*.txt"),
                                    ("All Files", "*.*")])
        Label(root, text=inputNama, font=2, bg=bg_color, fg=fg_color).pack(side=RIGHT)
    except:
        mb.showerror("JENERET | Error","Filenya ga ada :D")

# simpen serti
def savecert():
    try:
        dirpath = fd.askdirectory(initialdir="/",title="Simpan di..")
        labelDirpath = Label(root, text=dirpath, font=(font_common, 10), fg=fg_color)
        labelDirpath.grid(column=1, row=1)
        labelDirpath.place(relx=.3, rely=.8)
    except FileExistsError:
        mb.showerror("JENERET | Error", "File tidak ada!")

# bagian penting
listNama = []

# clean strip
def cleanup_data():
    with open(inputname()) as f:
        for line in f:
            listNama.append(line.strip())

# generate!
def generate_cert():

    for index, name in enumerate(listNama):
        certificate_template_image = cv2.imread()
        cv2.putText(certificate_template_image, name.strip(), (470,514), cv2.FONT_HERSHEY_DUPLEX, 2.5, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.imwrite(f"{savecert}/{name.strip()}.png", certificate_template_image)
        print(f"Processing {index+1} / {len(listNama)}")

# keluar
def keluar():
    konfirmasi = mb.askyesno("Mau keluar?", "Mau keluar?")
    if konfirmasi:
        root.destroy()

# template serti
btnFile = Button(root, text="Pilih file...", font=(font_title, 10), command=inputcert, width=15)
btnFile.grid(column=0, row=1)
btnFile.place(relx=.6, rely=.3)

# list nama
btnNama = Button(root, text="List Nama...", font=(font_title, 10), command=inputname, width=15)
btnNama.grid(column=0, row=1)
btnNama.place(relx=.6, rely=.4)

# directory penyimpanan fix
btnDir = Button(root, text="Cari direktori..", font=(font_title, 10), command=savecert, width=15)
btnDir.grid(column=0, row=1)
btnDir.place(relx=.6, rely=.5)

# generate!
btnConfirm = Button(root, text="Generate!", font=(font_title, 10), command=generate_cert, bg="#029522", fg=fg_color, width=15)
btnConfirm.grid(column=0, row=1)
btnConfirm.place(relx=.5, rely=.7, anchor=CENTER)

# exit
btnExit = Button(root, text="Keluar", font=(font_title, 10), command=keluar, bg="#FF0000", fg=fg_color, width=15)
btnExit.grid(column=0, row=1)
btnExit.place(relx=.5, rely=.8, anchor=CENTER)

if __name__ == '__main__':
    root.mainloop()