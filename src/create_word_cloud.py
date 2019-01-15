import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud

# import MeCab as mc
dirpath = os.path.dirname(__file__)

class CreatWordCloud:
    def __init__(self, background_color: str, width: int=500, height: int=900):
        self.stopwords = [u'てる', u'いる', u'なる', u'れる', u'する', u'ある', u'こと', u'これ', u'さん', u'して', \
                     u'くれる', u'やる', u'くださる', u'そう', u'せる', u'した',  u'思う',  \
                     u'それ', u'ここ', u'ちゃん', u'くん', u'', u'て',u'に',u'を',u'は',u'の', u'が', u'と', u'た', u'し', u'で', \
                     u'ない', u'も', u'な', u'い', u'か', u'ので', u'よう', u'']
        self.font_path = "/Library/Fonts/STIXGeneralBolIta.otf"
        self.background_color = background_color
        self.width = width
        self.height = height

    def __call__(self, month: str, sex: str, word_lsit: list):
        return self.create_wordcloud(month, sex, " ".join(word_lsit))

    def create_wordcloud(self, month, sex, text: str):
        if sex == "man":
            image = "images/man.png"
        else:
            image = "images/woman.png"
        image_mask = np.array(Image.open(os.path.join(dirpath, image)))
        wordcloud = WordCloud(background_color=self.background_color, font_path=self.font_path, contour_width=3, \
                          mask=image_mask, stopwords=set(self.stopwords), contour_color='steelblue')
        wordcloud.generate(text)
        wordcloud.to_file(os.path.join(dirpath, "output/{0}_{1}_WordCloud.png".fromat(month, sex)))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.figure()
        plt.imshow(image_mask, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis("off")
        plt.show()

if __name__ == "__main__":
    CWC = CreatWordCloud(background_color="white", width=500, height=900)
    CWC(month="1", sex="man", word_lsit="Wōdejebato is an undersea volcanic mountain with a flat top (a guyot), and probably a shield volcano, in the northern Marshall Islands of the Pacific. Formed of basaltic rocks, it is connected through a 74-kilometre (46 mi) submarine ridge to the smaller Bikini Atoll to its southeast. Named for a sea god of Bikini, Wōdejebato rises 4,420 metres (14,500 ft) above the ocean floor, to within 1,335 metres (4,380 ft) of the surface. It was probably formed by a hotspot in present-day French Polynesia before being shifted by plate tectonics. A volcanic episode in the Late Cretaceous led to the formation of an island and a carbonate platform that disappeared below the sea. A second volcanic episode between 85 and 78.4 million years ago created an island that was eventually eroded, generating an atoll or atoll-like structure that covered the former island with carbonates. The second carbonate platform drowned about 68 million years ago. In addition to the task-specific dataset, the full set of Wikipedia pages (segmented at the sentence level) will be distributed on the data tab or on our website ".split())
