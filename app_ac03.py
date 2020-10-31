from flask import Flask, request, jsonify, render_template , redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import json
import os

app_ac03 = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cliente.db"
app_ac03.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbimpacta:impacta#2020@dbimpacta.postgresql.dbaas.com.br/dbimpacta'
db = SQLAlchemy(app_ac03)


class Cadastro(db.Model):
    __tablename__ = "tbAlunos_alexsandro_RA_1901705"
    ra = db.Column(db.Integer, primary_key = True, unique=True)
    nome_do_aluno = db.Column(db.String(50), nullable=True)
    email_do_aluno = db.Column(db.String(50), nullable=True)
    logradouro = db.Column(db.String(50), nullable=True)
    numero = db.Column(db.String(5), nullable=True)
    bairro = db.Column(db.String(25), nullable=True)
    estado = db.Column(db.String(20), nullable=True)
    complemento = db.Column(db.String(25), nullable=True)
    cep = db.Column(db.String(10), nullable=True)

    def __init__(self, ra, nome_do_aluno, email_do_aluno, logradouro, numero, bairro, estado, complemento,cep):
        self.ra = ra
        self.nome_do_aluno = nome_do_aluno
        self.email_do_aluno = email_do_aluno
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.estado = estado
        self.complemento = complemento
        self.cep = cep

@app_ac03.route("/")
@app_ac03.route("/index")
def index():
    cadastro = Cadastro.query.all()
    return render_template("index.html", cadastro=cadastro)

@app_ac03.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        aluno = Cadastro(request.form['ra'], 
        request.form['nome'], 
        request.form['email'], 
        request.form['logradouro'], 
        request.form['numero'], 
        request.form['bairro']  , 
        request.form['estado'], 
        request.form['complemento'],
        request.form['cep'])
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app_ac03.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    aluno = Cadastro.query.get(id)
    if request.method == 'POST':
        aluno.ra = request.form['ra']
        aluno.nome_do_aluno = request.form['nome']
        aluno.email_do_aluno = request.form['email']
        aluno.logradouro = request.form['logradouro']
        aluno.numero = request.form['numero']
        aluno.bairro = request.form['bairro']
        aluno.estado = request.form['estado']
        aluno.complemento = request.form['complemento']
        aluno.cep = request.form['cep']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', aluno=aluno)

@app_ac03.route("/delete/<int:id>")
def delete(id):
    aluno = Cadastro.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    #db.create_all()
    #db.drop_all()
    port = int(os.environ.get("PORT",5000))
    app_ac03.run(debug=True, host='0.0.0.0', port=port)

'''
select * from maap_system
delete from maap_system

from app_ac03 import db
db.create_all()
db.drop_all() 
http://localhost:5000/
heroku
pip install pipenv
pipenv install requests
pipenv install "dependency"
pipenv check
heroku login
cltr c devolve o prompt
heroku create
git push heroku master
git push heroku HEAD:master
heroku ps:scale web=1
heroku open
heroku apps
heroku apps:destroy "nome do app sem aspas"
heroku apps:destroy arcene-40228
heroku buildpacks:clear
heroku buildpacks:add --index heroku/python
heroku logs --tail
heroku logs  > herokulogs
heroku apps:rename NEWNAME
heroku apps:rename crud-cadastro-alunos --app boiling-tundra-56022 
'''