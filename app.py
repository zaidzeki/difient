#!/usr/bin/env python3

import requests
from flask import Flask, request, send_file
from PIL import Image


app = Flask(__name__)

@app.route('/')
def index():
    return '''\
        <form action="/image" target="__blank" method='POST'>
            <textarea name="prompt"></textarea>
            <button>Get Image</button>
        </form>
'''

@app.route('/image', methods=['GET', 'POST'])
def image():
    prompt = request.form.get('prompt')
    url = f"https://image.pollinations.ai/prompt/{prompt}?width=1080&height=720&nologo=false&quality=high&crispness=high"
    resp = requests.get(url)
    nonce = random.randint(100000)
    with open(f'{nonce}.png') as fp: fp.write(resp.content)
    Image.open(f'{nonce}.png').save('{nonce}.jpg', optimize=True)
    return send_file(f'{nonce}.jpg')
    return prompt


if __name__ == "__main__":
    app.run()
