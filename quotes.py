from flask import Flask ,render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:@Post@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://nzcipglequwrnh:c1d9f876805a0c4b064fb234a6cf1e6bdcfd2bbb8d8ba2bf9f2f3bc15b1c67e6@ec2-52-22-216-69.compute-1.amazonaws.com:5432/d4vd1uf2vnciqv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author =db.Column(db.String(30))
    quote = db.Column(db.String(2000))



@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
     return render_template('quotes.html')

@app.route('/process', methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()

    return redirect(url_for('index'))