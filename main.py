
#!/usr/bin/python
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
#dir(selenium)
import time
import cv2
import requests
from bs4 import BeautifulSoup

import glob
import os
import sys



EXTS = 'jpg', 'jpeg', 'JPG', 'JPEG', 'gif', 'GIF', 'png', 'PNG'

def avhash(im):
    if not isinstance(im, Image.Image):
        im = Image.open(im)
    im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    return reduce(lambda x, (y, z): x | (z << y),
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),
                  0)

def hamming(h1, h2):
    h, d = 0, h1 ^ h2
    while d:
        h += 1
        d &= d - 1
    return h

def cal(img):
    seq = []
    h = avhash(img)
    return hex(h)

def locked():
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print "Usage: %s image.jpg [dir]" % sys.argv[0]
    else:
        im, wd = sys.argv[1], '.' if len(sys.argv) < 3 else sys.argv[2]
        h = avhash(im)

        os.chdir(wd)
        images = []
        for ext in EXTS:
            images.extend(glob.glob('*.%s' % ext))

        seq = []
        prog = int(len(images) > 50 and sys.stdout.isatty())
        for f in images:
            seq.append((f, hamming(avhash(f), h)))
            if prog:
                perc = 100. * prog / len(images)
                x = int(2 * perc / 5)
                print '\rCalculating... [' + '#' * x + ' ' * (40 - x) + ']',
                print '%.2f%%' % perc, '(%d/%d)' % (prog, len(images)),
                sys.stdout.flush()
                prog += 1

        if prog: print
        for f, ham in sorted(seq, key=lambda i: i[1]):
            print "%d\t%s" % (ham, f)


def cmp():
  img=cv2.imread("/Users/zrain/Desktop/scshot/pic1.png")
  h, w = img.shape[:2]
  print h, w
def webscreen1():
  url = 'http://edu.exmail.qq.com/domain/mail2.sysu.edu.cn'
  driver = webdriver.Chrome()
  #driver.maximize_window()
  #driver.set_window_size(800, 720)

  driver.get(url)
  time.sleep(3)
  print(driver.title)
  driver.get_screenshot_as_file("/Users/zrain/Desktop/scshot/pic6.png")
  #driver.find_element_by_id("kw").send_keys("selenium")
  #driver.find_element_by_id("su").click()
  time.sleep(0)
  driver.close()


def webscreen2():
  url = 'http://www.baidu.com'
  driver = webdriver.Chrome()
  #driver.maximize_window()
  #driver.set_window_size(800, 720)
  driver.get(url)
  print(driver.title)
  driver.get_screenshot_as_file("/Users/zrain/Desktop/scshot/pic2.png")
  #driver.find_element_by_id("kw").send_keys("selenium")
  #driver.find_element_by_id("su").click()
  time.sleep(3)
  driver.close()


  """
  driver = webdriver.Chrome()
  driver.set_page_load_timeout(300)
  driver.set_window_size(1280,800)
  driver.get(url)
  imgelement = driver.find_element_by_id('s_fm')
  location = imgelement.location
  size = imgelement.size
  savepath = r'/Users/zrain/Desktop/XXXX.png'
  driver.get_screenshot_as_file(savepath)
  im = Image.open(savepath)
  left = location['x']
  top = location['y']
  right = left + size['width']
  bottom = location['y'] + size['height']
  im = im.crop((left,top,right,bottom))
  im.save(savepath)
  print "ddd left",left
  """


if __name__=='__main__':
    # webscreen1()

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.Chrome()

    driver= webdriver.PhantomJS()
    driver.set_window_size(1366, 768)
    f = open("ans.txt")
    line = f.readline()
    cont=0
    while line:
        cont+=1
        if cont>2:
            break
        url=line.split('"')[1]
        print url

        driver.get(url)
        data = driver.title
        print(data)
        time.sleep(3)
        filename=""
        # print(driver.title)
        for idx in url:
            if idx.isalnum():
                filename+=idx
            else:
                filename+='_'

        filename="/Users/zrain/Desktop/scshot/url/"+filename+".png"
        print(filename)
        driver.get_screenshot_as_file(filename)
        # driver.find_element_by_id("kw").send_keys("selenium")
        # driver.find_element_by_id("su").click()
        time.sleep(3)
        line = f.readline()
    driver.close()
    f.close()