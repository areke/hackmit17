
import urllib, urllib2, json, string, time, base64, os, cv2
CAPTCHA_DIRECTORY = 'static/captcha_images/'
LABELED_DIRECTORY = 'static/labeled_images/'
def download():
    url = 'https://captcha.delorean.codes/u/areke/challenge'
    data = {}
    request = urllib2.Request(url)
    response = urllib2.urlopen(request).read()
    data = json.loads(response)
    images = data['images']
    for image in images:
        name = image['name']
        jpg_base64 = image['jpg_base64']
        img_data = base64.b64decode(jpg_base64)
        filename = CAPTCHA_DIRECTORY + name + '.jpg'
        with open(filename, 'wb') as f:
            f.write(img_data)

images = os.listdir(CAPTCHA_DIRECTORY)
while len(images) != 4000:
    download()
    images = os.listdir(CAPTCHA_DIRECTORY)