from PIL import Image

print 'Combine image'

X = -50
Y = -50
count = 0
new_im = Image.new('RGB', (550, 750))
while X < 501:
    X += 50
    Y = -50
    while Y < 701:
        Y += 50
        count += 1
        input_path = '../data/13/raw_' + str(X) + '_' + str(Y) + '_' + str(count) + '.jpg'
        img = Image.open(input_path)
        img_crop = img.crop((40, 40, 90, 90))
        print input_path
        new_im.paste(img_crop, (X,Y))
new_im.save('../data/13/full.jpg')
