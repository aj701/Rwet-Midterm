# Midterm Assignment
# RWET Spring 2015
# ITP - NYU
# By Andrew J. LeVine
# March 2015

"""
Usage: midterm-final.py <imgfile> [--maxLen=<maxLen>] [--fontSize=<fontSize>] [--ranSamp=<ranSamp>]

"""
# maxLen= max length of output fontSize = size of font used in output  ranSamp = amount of different words randomly sampled from 400 most popular words

import sys
from docopt import docopt
from PIL import Image
import random
import operator, time, string
import nltk
from nltk.corpus import stopwords #made own stop words in the end - might switch back to this
from string import digits
text = open('xfiles.txt') #load any textfile you want
start = time.time()


# Finding frequent without stop words - lots is missing!
freq = {}
for line in text:
    line = line.split()
    for word in line:
        word = word.lower()
        wordadj = word.translate(string.maketrans("",""), string.punctuation) #remove punctuation
        new_words = wordadj.translate(None, string.digits) + " "
        if new_words in freq:
            freq[new_words] += 1
        else:
            freq[new_words] = 1

sorted_words = sorted(freq, key = freq.get, reverse = True)
stopwords = ['the ', 'i ' 'is' 'to ', 'a ', 'and ', 'you ', 'of ', 'in ', 'he ', 'it ', 'on ', 
'that ', 'at ', 'his ', 'what ', 'this ', 'her ', 'out ', 'up ', 'she ', 'him ', 'with ', 'was ', 'as ', 
'for ', 'are ', 'me ', 'they ', 'we ', 'have ', 'but ', 'no ', 'not ', 'looks ', 'from ', 'its ', 'know ', 'be ', 'here ', 'im ', 'your ',
'dont ', 'down ', 'do ', 'there ', 'just ', 'all ', 'my ', 'an ', 
'who ', 'into ', 'about ', 'were ', 'then ', 'one ', 'over ', 'get ', 'by ', 'can ', 'see ', 'if ', 'like ', 'them ', 'going ', 
'well ', 'right ', 'youre ', 'now ', 'been ', 'got ', 'has ', 'so ', 'off ', 
'go ', 'where ', 'some ', 'how ', 'did ', 'want ', 'around ', 'or ', 'through ', 'something ', 'away ', 
'hes ', 'why ', 'us ', 'thats ', 'looking ', 'come ', 'when ', 'other ', 'yeah ', 'would ', 'had ', 'their ', 'could ', 'sees ', 'cant ', 'any ', 
'gets ', 'more ', 'theres ', 'only ', 'these ','which ',
'didnt ', 'face ', 'need ', 'behind ', 'will ', 'our ', 'opens ', 'ive ',
'make ', 'said ', 'before ', 'whats ',
'maybe ', 'open ', 'okay ', 'let ' 'because ', 'anything ', 'doesnt ',
'same ', 'yes ', 'even ', 'never ', 'too ', 'sure ', 'does ', 'theyre ', 'am ', 'thing ', 'put ', 'comes ', 'hey ', 'than ', 'shes ', 'whartonthe ', 'rrrr ', 'twothreeonesevensixonesix ', 'chuckie ', 'undead ', 'quagmire ', 'error ','tx ']

fwords = [w for w in sorted_words if not w in stopwords]
cool = fwords[:400]
# print cool

#imaging

dct = docopt(__doc__)

imgname = dct['<imgfile>'] 

maxLen = dct['--maxLen']

fontSize = dct['--fontSize']

ranSamp = dct['--ranSamp']

try:
    maxLen = float(maxLen)
except:
    maxLen = 14.0 

try:
    fontSize = int(fontSize)
except:
    fontSize = 10

try:
    img = Image.open(imgname)
except IOError:
    exit("File not found: " + imgname)

try:
    ranSamp = int(ranSamp)
except:
    ranSamp = 246


# resizing the image
width, height = img.size

rate = maxLen / max(width, height)

width = int(rate * width) 

height = int(rate * height)

img = img.resize((width, height))


pixel = img.load() #get pixels from loaded image

# words = cool
# insert = random.choice(words), random.choice(words), random.choice(words), ".", " "
insert = random.sample(cool, ranSamp)
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")
insert.append(" ")

# print insert

string = ""

for h in xrange(height):
    for w in xrange(width):
        rgb = pixel[w, h]
        string += insert[int(sum(rgb) / 3.0 / 256.0 * (ranSamp + 10))]
    string += "\n"

#lets template this in some html

template = """<!DOCTYPE HTML>
<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <style type="text/css" media="all">
    pre {
      white-space: pre-wrap;
      font-family: 'Inconsolata', 'Consolas'!important;
      line-height: 1.0;
      font-size: %dpx;
    }
  </style>
</head>
<body>
  <pre>%s</pre>
</body>
</html>
"""

html = template % (fontSize, string)
sys.stdout.write(html)
sys.stdout.flush()
