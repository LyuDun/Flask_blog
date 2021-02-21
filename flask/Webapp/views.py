from Webapp import app
from flask import render_template, send_from_directory, request
import os
import operator
from pathlib import Path

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.template_filter('md')
def md_2_html(PATH):
    import mistune
    markdown = mistune.Markdown()
    with open(PATH, 'r') as f:
        text = f.read()
        return markdown(text)


@app.route('/')
@app.route('/index/')
def index():
    _markdown_path = Path(Path.cwd(), "Webapp/markdown_article")
    articles = {}


    for dir_, _, files in os.walk(_markdown_path):
        for fileName in files:
            relDir = os.path.relpath(dir_, _markdown_path)
            relFile = os.path.join(relDir, fileName)
            if str(relFile).startswith('.'):
                url = str(relFile).split('.')[1]
                articles[url] = fileName.split('.', 1)[0]
            else:
                url = str(relFile).split('.')[0]
                articles[url] = fileName.split('.', 1)[0]
    return render_template('index.html', articles=articles)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/article/<path:article_category>')
def show_article(article_category):
    base_dir = os.path.dirname(__file__)
    article_dir = os.path.join(base_dir, 'markdown_article', article_category)
    str = article_dir + '.md'
    return render_template('article.html', article_html=str)


# @app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
