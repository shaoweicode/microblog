from app import app
from flask import render_template,flash,redirect
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'shaowei'}
    post = [
        {'author':{'nickname':'john'},
        'body':'beautiful day in portland!'
        },
        
        {'author':{'nickname':'Susan'},
        'body':'movie is cool'
        }
    ]
    return render_template('index.html',title='Home',user=user,post = post)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for openid"'+form.openid.data +'"remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])