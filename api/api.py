import time
from flask import Flask

import numpy as np
import matplotlib.pyplot as plt
import re
from twython import Twython
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from IPython.display import Image as im

app = Flask(__name__)

@app.route('/endpoint')
def get_data():
		print(request.args())
    return {'time': time.time()}