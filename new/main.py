from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from tkinter import Label, Button, filedialog

class App:
    def __init__(self):
        self.photo = None
        self.root = tk.Tk()
        self.root.title("ASCII Image Generator")

        self.label = Label(self.root)
        self.label.pack()

        button = Button(self.root, text="Wybierz", command=self.open_file_dialog)
        button.pack()

        self.root.mainloop()

    def generate_ascii_image(self, file_path):
        if file_path:
            image = Image.open(file_path)

            ascii = ["Ñ","@","#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",":","+","=","-",".","_"]

            resized_image = image.resize((100, 100))  # Nowe wymiary mniejsze niż 400x400 pikseli

            canvas = Image.new("RGB", (400, 400))

            # Utwórz obiekt do rysowania na kanwie
            draw = ImageDraw.Draw(canvas)

            # Przejdź przez piksele obrazu wynikowego
            for x in range(400):
                for y in range(400):
                    # Pobierz kolor piksela z przeskalowanego obrazu
                    pixel_color = resized_image.getpixel((x // 4, y // 4))

                    # Ustaw kolor piksela na kanwie
                    draw.point((x, y), pixel_color)

            image_hsb = canvas.convert("HSV")
            hue, saturation, brightness = image_hsb.split()
            canvas2 = Image.new("L", canvas.size)
            canvas2.paste(brightness, (0, 0))

            width, height = canvas2.size
            aspect_ratio = height / width
            new_width = 400  # Nowa szerokość pliku ASCII
            new_height = 400  # Nowa wysokość pliku ASCII

            pixels = canvas2.getdata()

            new_pixels = [ascii[pixel // 25] for pixel in pixels]
            new_pixels = ''.join(new_pixels)

            new_pixels_count = len(new_pixels)
            ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]

            # Dopasuj do kwadratowych wymiarów dodając odstępy
            ascii_image_square = []
            for line in ascii_image:
                padding = " " * (new_width - len(line))
                line_with_padding = line + padding
                ascii_image_square.append(line_with_padding)

            ascii_image = "\n".join(ascii_image_square)

            self.show_ascii_image(ascii_image, new_width, new_height)

    def show_ascii_image(self, ascii_image, width, height):
        if self.photo:
            self.photo.image = None

        text_image = Image.new("RGB", (width * 10, height * 10), "black")
        draw_text = ImageDraw.Draw(text_image)
        font = ImageFont.load_default()
        draw_text.text((0, 0), ascii_image, font=font, fill="white")

        text_image_resized = text_image.resize((width, height))
        self.photo = ImageTk.PhotoImage(text_image_resized)

        self.label.config(image=self.photo)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        self.generate_ascii_image(file_path)

app = App()
