from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Captain'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

if __name__=='__main__':
    app.run()
