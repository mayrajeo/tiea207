from flask import Flask
from flask import render_template, request
from yle2 import get_video_list
from yle2 import get_video_url
import os
import csv
import random


app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def hello_world():
    try:
        year = request.form['year']
    except:
        year = '1993'
    tulokset = get_video_list(year)
    if len(tulokset) == 0:
        tulokset = get_video_list('1992')
    mid = random.choice(tulokset)
    url = get_video_url(mid)
    return render_template('base.html',
                           url=url,
                           mid=mid)


if __name__ == '__main__':
    app.run()