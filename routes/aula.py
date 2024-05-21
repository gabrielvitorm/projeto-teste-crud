from flask import Blueprint, render_template, request, url_for, redirect
import os

#Estou usando o Blueprint para separar as rotas das aulas e dos eventos
aula_route = Blueprint('aula', __name__)
DATA_FILE = 'database/aulas.txt'

# 1 - Essa primeira rota serve para listar as aulas que estão no "banco de dados" em txt, é necessário abrir uma lista no começo da função, pois vai ser atribuido um dicionário a esse txt. Também é necessário declarar uma Variável para receber o arquivo txt que nesse caso é a variável "DATA_FILE"
@aula_route.route('/')
def home_page():
    aulas = []
    with open(DATA_FILE, 'r') as file:
        aulas = [line.strip().split('|') for line in file.readlines()] # Essa é uma usabilidade da biblioteca os para ler as informações da linha.
    return render_template('aula/home_aula.html', aulas=aulas) #É necessário atribuir a variável para usar no HTML com o Jinja

# 1 - Essa segunda rota serve para criar uma aula através de um formulário Html
@aula_route.route('/new', methods=['GET', 'POST'])
def nova_aula():
    if request.method == 'POST': #Metodo POST serve para receber os dados do formulário
        aula = request.form['title'] + '|' + request.form['description'] + '|' + request.form['hours'] + '\n' #essas tags são definidas no formulário com o id e a variável aula vai receber essas informações
        with open(DATA_FILE, 'a') as file:
            file.write(aula)
        return redirect(url_for('aula.home_page'))
    return render_template('aula/criar_aula.html')