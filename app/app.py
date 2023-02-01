from flask import Flask, render_template, request, redirect, url_for

import requests
import os
import random

nasa_planet_url=r'https://api.nasa.gov/planetary/apod'
nasa_rovers_url=r'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'




app = Flask(__name__)

@app.route('/')
def index():

    query={'api_key': os.getenv('API_KEY')  }

    headers = {"Accept": "application/json"}

    response = requests.request(
    "GET",
    nasa_planet_url,
    headers=headers,
    params=query,
    verify=False
    )
    return render_template('index.html', landing_image=response.json()['url'])

@app.route('/mars')
def mars():

    query={'sol': 1000, 'api_key': os.getenv('API_KEY')  }

    headers = {"Accept": "application/json"}

    response = requests.request(
    "GET",
    nasa_rovers_url,
    headers=headers,
    params=query,
    verify=False
    )


    return render_template('mars.html', mars_img_list=[entry['img_src'] for entry in response.json()['photos']])