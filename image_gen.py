from PIL import Image, ImageDraw, ImageFont
import string
import textwrap

def create_color_dict():
    color_dict = {}
    color_file = open('wiki_colorlist.txt', 'r')
    
    for color in color_file.readlines():
        col_tuple = color.split(' #')
        col = col_tuple[0].translate(str.maketrans('', '', string.punctuation)).lower()
        color_dict[col_tuple[0].lower()] = '#' + col_tuple[1][0:-1]
    
    return color_dict

def scale_font(ideal_width, line):
    font_size = 40
    font = ImageFont.truetype('Jost-VariableFont_ital,wght.ttf', size=font_size)
    while (abs(font.getsize(line)[0] - ideal_width) > 25) and font_size < 92:
        font_size += 1
        font = ImageFont.truetype('Jost-VariableFont_ital,wght.ttf', size=font_size)
    return font

def create_color_image(color_filename, template_filename, margin=False, font_size=False, font_filename=False):
    image = Image.open('empty.png')
    draw = ImageDraw.Draw(image)
    
    if font_size == False:
        font_size = 12

    if font_filename == False:
        font = ImageFont.truetype('arial.ttf', font_size)
    else:
        font = ImageFont.truetype(font_filename, font_size)

    if margin == False:
        margin = 130

    color_file = open(color_filename, 'r')
    text = ""
    colors_list = []
    colors = color_file.readlines()
    for color in colors:
        color_list.append(color[0:-1])
        text += color[0:-1] + ' '

    color_dict = moby_colors.create_color_dict()


    color_file.close()    
text_file = open('colors_red_fern.txt', 'r')
text = ""
color_list = []
colors = text_file.readlines()
for color in colors:
    color_list.append(color[0:-1])
    text += color[0:-1] + ' '

color_dict = create_color_dict()
margin = 130
line_height = 20
text = textwrap.wrap(text, width=64)

words_per_line = []
for line in text:
    words = line.split(' ')
    words_per_line.append(len(words))

ideal_width = font.getsize(text[-2])[0]
print(text[0])
words_typed = 1
line = 0
for color in colors[0:-1]:
    color = color[0:-1]
    col_size = font.getsize(color + ' ')
    draw.text((margin, line_height), color, fill=color_dict[color], font=font)
    margin += col_size[0]
    if words_typed == words_per_line[line]:
        words_typed = 0
        line_height += font.getsize(text[line])[1]
        margin = 130
        line += 1
        if line != 0 and line != len(text):
            font = scale_font(ideal_width, text[line])
    words_typed += 1

image.save('test.png')
