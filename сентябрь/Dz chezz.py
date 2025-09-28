from PIL import Image, ImageDraw

length_desk = 640
length_cell = 80
# black_color = (0, 0, 0)
# white_color = (255, 255, 255)

# class Image:
#     def _init_(self, rgb):
#         self.rgb = rgb
#         self.length_cell = length_cell
#         self.basic_color = white_color

img = Image.new('RGB', (length_desk, length_desk), color=(0,0,0))
idraw = ImageDraw.Draw(img)

for i in range(8):
    for j in range(8):
        x1 = i * 80
        y1 = j * 80
        x2 = i + 80
        y2 = j + 80
        if (i + j) % 2 == 0:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        idraw.rectangle((x1, y1, x2, y2), fill=color)


# idraw.rectangle((1, 1, length_cell, length_cell), fill = black_color)
# idraw.rectangle((80, 80, 160, 160), fill=black_color)
# idraw.rectangle((160, 160, 240, 240), fill=black_color)
# idraw.rectangle((240, 240, 320, 320), fill=black_color)
# idraw.rectangle((320, 320, 400, 400), fill=black_color)
# idraw.rectangle((400, 400, 480, 480), fill=black_color)
# idraw.rectangle((480, 480, 560, 560), fill=black_color)
# idraw.rectangle((560, 560, 640, 640), fill=black_color)

img.save('probnic.png')