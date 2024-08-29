from flask import Flask, render_template, url_for, redirect, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('task.db')
    cursor = conn.cursor()
    tasks = cursor.execute("SELECT * FROM tb_tarefas").fetchall()
    conn.commit()
    return render_template('index.html', tarefas = tasks)

@app.route('/adicionar', methods=['POST'])
def addtask():
        task = request.form.get('addtask')
        conn = sqlite3.connect('task.db')
        cursor = conn.cursor()
        tasks = cursor.execute("INSERT INTO tb_tarefas (tas_tarefa) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

@app.route('/<int:task_id>/deletar', methods = ['POST'])
def deltask(task_id):
        dell = task_id
        conn = sqlite3.connect('task.db')
        cursor = conn.cursor()
        tasks = cursor.execute("DELETE FROM tb_tarefas WHERE tas_id = ?", (dell,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    