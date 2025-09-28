from PIL import Image, ImageDraw

length_desk = 640
length_cell = 80
black_color = (0, 0, 0)
white_color = (255, 255, 255)

# class Image:
#     def _init_(self, rgb):
#         self.rgb = rgb
#         self.length_cell = length_cell
#         self.basic_color = white_color

img = Image.new('RGB', (length_desk, length_desk), color=(0,0,0))
idraw = ImageDraw.Draw(img)

for i in range(8):
    for j in range(8):
        x1 = i * length_cell
        y1 = j * length_cell
        x2 = (i + 1) * length_cell
        y2 = (j + 1) * length_cell
        if (i + j) % 2 == 0:
            color = black_color
        else:
            color = white_color
        idraw.rectangle((x1, y1, x2, y2), fill=color)



# idraw.rectangle((80, 80, 160, 160), fill=black_color)

img.save('chess_desk.png')