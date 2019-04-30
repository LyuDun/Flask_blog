#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.template_filter('md')
def md_2_html(PATH):
    import mistune
    markdown = mistune.Markdown()
    with open(PATH,'r') as f:
        text = f.read()
        return markdown(text)

import views


