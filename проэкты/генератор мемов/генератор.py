from PIL import Image, ImageDraw, ImageFont

print('БиП Боп, Генератор мемов запущен!')
text1 = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: " ))
print(text1)
top_text = ''
bottom_text = ''
if text1 == 1:
    bottom_text = input('Введи нижний текст:')
    print(bottom_text)
elif  text1 == 2:
    top_text = input('Введи верхний текст:')
    bottom_text = input('Введи нижний текст:')
else:
    print('Введён не правильный режим. Перезапустите программу')
    quit()

print(top_text, bottom_text)

memes = ["Грустный_кот.png","Кот в очках.png","Кот в ресторане.png"]

for i in range(len(memes)):
   print( i, memes[i])

print("выбери картинку для мема")
imge = Image.open(memes[int(input("Введите номер картинки: "))])

font1 = ImageFont.truetype('arial.ttf', size=70)

draw = ImageDraw.Draw(imge)

width, height = imge.size

text = draw.textbbox((0,0),top_text,font1)

text2 = draw.textbbox((0,0),bottom_text,font1)

draw.text(((width - text[2]) / 2, 10), top_text, font=font1, fill='black')

draw.text(((width - text2[2]) / 2,(height - text2[3] -10)), bottom_text, font=font1, fill='black')

imge.save('nev_mem.jpg')




