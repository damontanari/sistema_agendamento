from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from main import app

agendamentos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        data = request.form['data']
        servicos = request.form.getlist('servicos')
        data_agendamento = datetime.strptime(data, '%Y-%m-%d')

        if data_agendamento < datetime.now():
            flash('A data de agendamento não pode ser anterior ao dia atual.', 'error')
            return redirect(url_for('agendar'))

        agendamentos.append({'data': data_agendamento, 'servicos': servicos})
        flash('Agendamento realizado com sucesso!', 'success')
        return redirect(url_for('agendar'))

    return render_template('agendamento.html')

@app.route('/historico')
def historico():
    hoje = datetime.now()
    semana_atual = hoje + timedelta(days=7)
    agendamentos_semana = [agendamento for agendamento in agendamentos if hoje <= agendamento['data'] < semana_atual]

    return render_template('historico.html', agendamentos_semana=agendamentos_semana)
