from app import app
from flask import render_template, send_from_directory, request
import os
import operator


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
    lists = os.walk('/root/myproject/Flask_blog/flask/app/markdwon_article')
    articles = {}
    base_url = 'http://www.cqcqhelloworld.top/article/'
    for path, dir_list, file_list in lists:
        for file_name in file_list:
            str = dir_list
            str = os.path.join(path, file_name)
            url = base_url + \
                str.split('/', 8)[7]+'/'+str.split('/', 8)[8].split('-', 1)[0]
            articles[url] = file_name.split('-', 1)[1].split('.', 1)[0]
    return render_template('index.html', articles=articles)


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/article/<path:article_category>/<int:id>/')
def show_article(article_category, id):
    base_dir = os.path.dirname(__file__)
    article_dir = os.path.join(base_dir, 'markdwon_article', article_category)
    for file in os.listdir(article_dir):
        if (operator.eq(file.split('-', 1)[0], str(id))):
            return render_template('article.html',
                                   article_html=os.path.join(article_dir, file))


# @app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
