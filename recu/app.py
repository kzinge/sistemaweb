from flask import Flask, render_template, redirect, request, session, make_response, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supermegadificil'
mensagens = {}
print(mensagens)


@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if  request.method == 'POST':
        user = request.form['name']

        if 'username' in mensagens:
                session['username'] = user
                response = make_response(redirect(url_for('dash')))
                response.set_cookie('username', user, max_age=60 * 60 * 24)
                return response
                
        else:
            session['username'] = user
            response = make_response(redirect(url_for('dash')))
            response.set_cookie('username', user, max_age= 60*60*24)
            mensagens[user] = []
            print(mensagens)
            return response
        
    else:
        return render_template('login.html')


@app.route('/dash')
def dash():
    if 'username' not in session:
        return redirect(url_for('login'))

    user = request.cookies.get('username', session.get('username'))
    msg_user = mensagens[session['username']]

    if user not in mensagens:
        return redirect(url_for('login'))

    query_user = request.args.get('user', user)
    if query_user in mensagens:
        msg_user = mensagens[query_user]
    else:
        msg_user = []

    return render_template('dash.html', msgs = msg_user)


@app.route('/novamsg', methods=['GET', 'POST'])
def newmsg():

    if 'username' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        new_msg = request.form['mensagem']
        mensagens[session['username']].append(new_msg)
    
        return redirect('dash')
    
    else:
        return render_template('newmsg.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)

    response = make_response(redirect(url_for('index')))
    response.set_cookie('username', '', max_age= 0)

    return response


