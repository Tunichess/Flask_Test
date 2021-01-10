from flask import Flask,request,jsonify,url_for,redirect, session,render_template, g 
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'

bootstrap=Bootstrap(app)



# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['POST','GET'], defaults={'nbr': '0','color':'Default'})
@app.route('/<int:nbr>/<string:color>', methods=['POST','GET'])

def form(nbr,color):
    if request.method=="GET":
        return render_template('form.html')
    else:
        nbr = request.form['nbr']
        if  nbr=="" :
            nbr=0
        color = request.form['color']     
        nbr2=int(nbr) % 7
        nbr3=7-nbr2
        listnbr=[*range((int(nbr)-nbr2))]
        listnbr2=[*range(int(nbr2))]
        listnbr=[*range((int(nbr)-nbr2))]
        listnbr3=[*range(int(nbr3))]
        ct=int(nbr) // 7
        print(ct)
        tops=520-(ct*45)
        print(tops)
        return render_template('form.html', nbr=nbr, color=color, listnbr=listnbr, listnbr2=listnbr2, listnbr3=listnbr3 ,tops=tops)


if __name__ == "__main__":
    app.run()