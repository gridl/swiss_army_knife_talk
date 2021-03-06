from flask import Flask, g, request, make_response
import time

app = Flask(__name__)

@app.route('/')
def index():
    language = request.headers.get('Accept-Language', '')
    if 'en' in language:
        body = "Welcome to PolyConf! Yay!"
    else:
        body = "Witajcie na Polyconfie!"

    resp = u"""
    <html>
    <body>
    <h1>{body}</h1>
    </body>
    </html>
    """.format(body=body)
    return make_response(resp)

app.run(port=8080)
