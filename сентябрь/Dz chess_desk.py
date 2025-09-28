from PIL import Image, ImageDraw

class Chess:
    def __init__(self, length_desk, length_cell, first_color, second_color):
        self.length_desk = length_desk
        self.length_cell = length_cell
        self.first_color = first_color
        self.second_color = second_color
        self.idraw = None
        self.img = None
        self.range = self.length_desk // self.length_cell

    def create_desk(self):
        # И так выбрасывает ошибку, что цифр не хватает
        # if not len(self.first_color) == 3 and (len(self.second_color) == 3):
        #     raise ValueError ("Неверное значение")
        self.img = Image.new('RGB', (self.length_desk, self.length_desk), color=self.second_color)
        self.idraw = ImageDraw.Draw(self.img)

    def chess_desk(self):
        for i in range(self.range):
            for j in range(self.range):
                x1 = i * self.length_cell
                y1 = j * self.length_cell
                x2 = (i + 1) * self.length_cell
                y2 = (j + 1) * self.length_cell
                if (i + j) % 2 == 0:
                    color = self.first_color
                else:
                    color = self.second_color
                self.idraw.rectangle((x1, y1, x2, y2), fill=color)
        self.img.save('chess_desk_2.png')

desk = Chess(640,80, (255, 165, 0), (0, 255, 0))
desk.create_desk()
desk.chess_desk()