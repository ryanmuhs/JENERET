# Inspired by : https://youtu.be/Xf8dhNl4d9c
# Original code : https://github.com/GunarakulanGunaretnam/automatic-certificate-generator
from tkinter import *
from tkinter import colorchooser
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import pyglet as pg
import cv2

# font
pg.font.add_file('fonts/Poppins-Bold.ttf')
pg.font.add_file('fonts/Poppins-Regular.ttf')

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
titleApp.place(relx=0.5, rely=0.07, anchor=CENTER)

descApp = Label(root, text="Certificate Generator", font=(font_common, 15), fg=fg_color, bg=bg_color)
descApp.grid(column=0, row=0)
descApp.place(relx=0.5, rely=0.15, anchor=CENTER)

# input file
def inputcert():
    try:
        templateCert = fd.askopenfilename(initialdir="/", 
                                        title="Choose template", 
                                        filetypes=[("PNG", "*.png"),
                                        ("All Files", "*.*")])
        entryTemplate.delete(1, END)
        entryTemplate.insert(0, templateCert)
    except FileNotFoundError:
        mb.showerror("JENERET | Error", "File not found :(")
    else:
        return templateCert

# input nama
listName = []
def inputname():
    try:
        inputNama = fd.askopenfilename(initialdir="/",
                                    title="List Nama...", 
                                    filetypes=[("Text Document", "*.txt"),
                                    ("All Files", "*.*")])
        entryName.delete(1, END)
        entryName.insert(0, inputNama)
        print(inputNama)
        return inputNama
    except:
        mb.showerror("JENERET | Error","Something error, I can feel it")

def pick():
    pickCol = colorchooser.askcolor()[0]
    return pickCol

def inputdir():
    inputDir = fd.askdirectory(initialdir="C:",
                            title="Input directory..")
    entryDir.delete(1, END)
    entryDir.insert(0, inputDir)


templatecert = StringVar()
inputNama = StringVar()
pickCol = StringVar()
# append nama
def appendList():
    inputNama = inputname()
    try:
        with open(inputNama, "r+") as f:
            for line in f:
                listName.append(line.strip())
    except FileNotFoundError:
        mb.showerror("JENERET", "File not yet selected")

# generate!
def generateCert():
    # templateCert = inputcert()
    # # inputDir = inputdir()
    # pickCol = pick()

    global templatecert
    global pickCol
    print(pickCol)
    try:
        for name in (listName):
            final_cert = cv2.imread()
            cv2.putText(final_cert, str(name), (470,514), cv2.FONT_HERSHEY_DUPLEX, 3, pickCol, 5, cv2.LINE_AA)
            cv2.imwrite(f"C:/Users/Lenovo/OneDrive - Telkom University/Tel-U/Matkul/SEM 2/Alpro/TUBES/jadi/generated-cert/{str(name)}.png", final_cert)
            # cv2.imwrite(f"{str(inputDir)}/{str(name)}.png", certificate_template_image)
    except:
        mb.showerror("JENERET | Error", "Something error, I can feel it")
    else:
        mb.showinfo("JENERET | Success","Certificate has been generated!")
        # print(templatecert)

# call
def generate():
    appendList()
    generateCert()

# keluar
def exit():
    confirm = mb.askyesno("JENERET | Exit?", "Want to exit?")
    if confirm:
        root.destroy()

# template serti
labelTemplate = Label(root, text="Insert certificate template (.png)", font=(font_title, 10), bg=bg_color, fg=fg_color, padx=0, pady=0)
labelTemplate.place(relx=.05, rely=.21)
entryTemplate = Entry(root, text="", width=35, font=(font_common, 8))
entryTemplate.place(relx=.05, rely=.29)
btnTemplate = Button(root, text="Choose file...", font=(font_title, 10), command=inputcert, width=15)
btnTemplate.grid(column=0, row=1)
btnTemplate.place(relx=.6, rely=.26)

# list nama
labelName = Label(root, text="Insert names (.txt)", font=(font_title, 10), bg=bg_color, fg=fg_color, padx=0, pady=0)
labelName.place(relx=.05, rely=.39)
entryName = Entry(root, text="", width=35, font=(font_common, 8))
entryName.place(relx=.05, rely=.45)
btnName = Button(root, text="Choose File...", font=(font_title, 10), command=inputname, width=15)
btnName.grid(column=0, row=1)
btnName.place(relx=.6, rely=.42)

labelCol = Label(root, text="Pick a color", font=(font_title, 10), bg=bg_color, fg=fg_color, padx=0, pady=0)
labelCol.place(relx=.05, rely=.55)
btnCol = Button(root, text="Pick...", font=(font_title, 10), command=pick, width=15)
btnCol.grid(column=0, row=1)
btnCol.place(relx=.6, rely=.55)

# insert directory
labelDir = Label(root, text="Insert Directory", font=(font_title, 10), bg=bg_color, fg=fg_color, padx=0, pady=0)
labelDir.place(relx=.05, rely=.65)
entryDir = Entry(root, text="", width=35, font=(font_common, 8))
entryDir.place(relx=.05, rely=.73)
btnDir = Button(root, text="Browse...", font=(font_title, 10), command=inputdir, width=15)
btnDir.grid(column=0, row=1)
btnDir.place(relx=.6, rely=.7)

# generate!
btnGenerate = Button(root, text="Generate!", font=(font_title, 10), command= generate, bg="#029522", fg=fg_color, width=15)
btnGenerate.grid(column=0, row=1)
btnGenerate.place(relx=.3, rely=.9, anchor=CENTER)

# exit
btnExit = Button(root, text="Exit", font=(font_title, 10), command=exit, bg="#FF0000", fg=fg_color, width=15)
btnExit.grid(column=1, row=1)
btnExit.place(relx=.7, rely=.9, anchor=CENTER)

if __name__ == '__main__':
    root.mainloop()