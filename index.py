from flask import Flask
from flask import render_template

app = Flask(__name__)
weekl=[]
for i in range(1,8):
    weekl.append(f'Week {i}')
@app.route('/')
def index():
    return render_template('README.html',weekl=weekl)


@app.route('/notes/<i>')
def notes():
    return render_template('Week {i}')

if __name__ == '__main__':
    app.run(debug=True)