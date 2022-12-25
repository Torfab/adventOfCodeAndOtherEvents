import os.path
import random
import re

import matplotlib.pyplot as plt
import multidict as multidict
import numpy as np
from PIL import Image

from wordcloud import ImageColorGenerator, WordCloud


def color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(%d, 100%%, 35%%)" % (random.randint(85,155)%120)


def getFrequencyDictForText(sentence, pruneNotUsefulWords=True, tooManyOccurance=7):
  if(not sentence):
    print("absurd")
    return
  fullTermsDict = multidict.MultiDict()
  tmpDict = {}
  # making dict for counting frequencies
  sentence=re.sub('[^A-Za-z]+', ' ', sentence)
  for text in sentence.split(" "):
    text=text.lower()
    if(pruneNotUsefulWords):
      if re.match("ll$|the$|a$|of$|in$|print$|def$|for$|dict$|def$|idx$|range$|return$|element$|splitted$|len$|result$|if$|rows$|solve$|append$|and$|split$|int$|else$|import$|utilities$|from$|continue$|sort$|break$|pop$|or$|while$|elif$|float$", text):
        continue
    val = tmpDict.get(text, 0)
    tmpDict[text] = min(val + 1, tooManyOccurance)
  for key in tmpDict:
    fullTermsDict.add(key, tmpDict[key])
  return fullTermsDict

def generate(dictOfText, arrayOfImages, recolor=False, imageRecolor=False):
  # print(dictOfText)
  for element in arrayOfImages:

    mask=np.array(Image.open(element))

    wc = WordCloud(background_color="white", max_words=2000, mask=mask)
    wc.generate_from_frequencies(dictOfText)   

    if(recolor):
      if (imageRecolor):
        image_colors = ImageColorGenerator(mask, (0,0,0))
        wc.recolor(color_func=image_colors, random_state=3)
      else:
        wc.recolor(color_func=color_func, random_state=3)
    wc.to_file("result"+element.split(".")[0]+".png")
    print("generated from "+element)
  print("completed")

def getTextFromFiles(path, custom=False):
  realText=''
  if(not custom):
    for day in range(1,25):
      file=path+"day"+str(day)+".py"
      text = open(os.path.dirname(__file__)+"/"+file, "r")
      data=text.read()
      text.close()
      realText = realText+data
  else:
    text = open(os.path.dirname(__file__)+"/"+path, "r")
    data=text.read()
    text.close()
    realText = realText+data     
  return realText


# generate(getFrequencyDictForText(getTextFromFiles("../")),["santa.jpg", "elephants.jpg", "tree.png"])
# getFrequencyDictForText(getTextFromFiles("allChallenges.txt", True), True, 20)
# generate(getFrequencyDictForText(getTextFromFiles("allChallenges.txt", True), True, 20),["santa.jpg", "elephants.jpg", "tree.png"])
generate(getFrequencyDictForText(getTextFromFiles("natale.txt", True), True, 30),["snowFlake.jpg"], True, False)
