from PIL import Image, ImageDraw
from numbers_mass import two
import itertools

def generate_number(point_list, image_name):
    '''
    :param point_list: матрица 8 х 8 где:
                       0 - соотв белыому цвету
                       1 - черному
           image_name - имя сохраняемого изображения, без указания формата
    :return: none
    '''
    im = Image.new('RGBA', (64*8, 64*8), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)
    # draw.line((100,200, 150,300), fill=128, width=3)
    for x, point_x in enumerate(point_list):
        for y, point_y in enumerate(point_x):
            if point_y == 1:
                draw.rectangle((y*64,x*64, y*64 + 64, x*64 + 64), fill=(0, 0, 0) )


    im.save(f'{image_name}.png', 'png')
    im.show()

def read_image(image_path):
    '''
    :param image_path - путь до изображения 512х512
           каждый квадрат изображения 64х64 - черного цвета 
    :return: pixel map 0 - white color 1 - black color
    '''
    im = Image.open(image_path)
    pixels = list(im.getdata())
    result_mas = []
    width, height = im.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    sub_mas = []
    for i, lines in enumerate(pixels):
        if (not i % 63 and i != 0) or i == len(pixels) - 1:
            for j, elem in enumerate(lines):
                if not j % 63 and j != 0:
                    if elem == (0, 0, 0, 255):
                        color = 1
                    else:
                        color = 0
                    if len(sub_mas) <= 7:
                        sub_mas.append(color)
                    else:
                        result_mas.append(sub_mas[:])
                        sub_mas = [color,]
    #вывод карты пикселей
    for i in result_mas:
        print(i)
    return result_mas

if __name__ == "__main__":

    generate_number(two, '1')
    read_image('1.jpg')