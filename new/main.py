from PIL import Image, ImageDraw
from termcolor import colored
import colorama

image = Image.open(r"C:\Users\admin\Desktop\IB Patryk\SEMESTR 6\PAzIG_projekt\ASCII_camera\new\DoggoInfobox.jpg")

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
new_height = int(aspect_ratio * new_width * 0.55)  # Nowa wysokość pliku ASCII

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

with open("ascii_image.txt", "w", encoding="utf-8") as file:
    file.write(ascii_image)

