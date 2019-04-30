from app import app
from flask import render_template
import configparser
import pymysql

cp = configparser.ConfigParser()
cp.read('mysql.cfg')
USER = cp.get('mysql','user')
PASSWORD = cp.get('mysql','password')
conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASSWORD, db='test',charset='utf8')
cur = conn.cursor()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/article/<int:id>/')
def show_article(id):
    sql = "select  article_path from article_name_table where id=%d"%(id) 
    try:
        cur.execute(sql)
        article_path = cur.fetchone() 
        return render_template('article.html',article_html=article_path[0])
    except:
        pass
