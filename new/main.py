import PIL.Image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

ASCII = ["Ñ","@","#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",":","+","=","-",".","_", " ", " ", " "]
ASCII = ASCII[::-1]

def resize(img, width2=200):
    width, height = img.size
    ratio = height/width
    height2 = int(width2 * ratio)
    new_img=img.resize((width2, height2))
    return new_img

def toGray(img):
    gray_img=img.convert("L")
    return gray_img

def convertASCII(img):
    pxl=img.getdata()
    symbols="".join(ASCII[x//25] for x in pxl)
    return symbols

def select_file():
    filepath = filedialog.askopenfilename()
    img=PIL.Image.open(filepath)

    new_img_data = convertASCII(toGray(resize(img)))
    pxl_counter = len(new_img_data)
    ascii_img= "\n".join(new_img_data[i:(i+200)] for i in range(0, pxl_counter, 200))

    ascii_img = '\n'.join(line.center(400) for line in ascii_img.split('\n'))

    text_widget.delete('1.0', END)
    text_widget.insert(END, ascii_img)

root = Tk()
root.configure(background='black')
root.state('zoomed')

text_widget = Text(root, wrap=WORD, width=400, height=150, bg='black', fg='white', font=("Courier", 4))
text_widget.pack(pady=10)

button = Button(root, text="Wybierz plik", command=select_file, bg='black', fg='white',width=80, height=30)
button.pack(pady=5)

root.mainloop()
