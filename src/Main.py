import requests
import shutil
import time

print 'Get for file 1'

X = -50
Y = -50
count = 0
while X < 501:
    X += 50
    Y = -50
    while Y < 701:
        Y += 50
        count += 1
        time.sleep(0.2)
        s = 'Doing file ' + str(count) + 'at ' + str(X) + ' -- ' + str(Y)
        print s
        optput_path = '../data/13/raw_' + str(X) + '_' + str(Y) + '_' + str(count) + '.jpg'
        url_path = 'http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=' + str(X) + '&Y=' + str(Y) + '&O=26993095&R=00001&F=0001&A=71714&rand=0.7327805407165833'
        # url = 'http://images1.flashphotography.com/Magnifier/MagnifyRender.ashx?X=242&Y=140&O=26993095&R=00003&F=0045&A=71714&rand=0.6425606573905747'
        r = requests.get(url_path, stream=True)
        if r.status_code == 200:
            with open(optput_path, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
