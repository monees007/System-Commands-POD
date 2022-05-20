from flask import Flask
from flask import render_template

app = Flask(__name__)
weekl=[]
for i in range(1,9):
    weekl.append(f'Week {i}')
@app.route('/')
def index():
    return render_template('README.html',weekl=weekl,leng=len(weekl))


@app.route('/notes/<i>')
def notes(i):
    return render_template(f'Week{str(int(i)+1)}.html',weekl=weekl,leng=len(weekl))

if __name__ == '__main__':
    app.run(debug=True)