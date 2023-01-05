import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=TO-_3tck2tg&ab_channel=ImagineDragonsVEVO')
img_file = open('Imagine_Dragon.png', 'wb')
img.save(img_file)
img_file.close()