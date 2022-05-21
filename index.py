from flask import Flask,render_template
import os
# ,mmm.md.html
app = Flask(__name__)
weekl=[]
for filename in os.listdir('templates'):
    f = os.path.join(filename[:-8])
    # checking if it is a file
    if os.path.isfile(os.path.join('templates', filename)) and filename!='base.html':
        weekl.append(f)

@app.route('/')
def index():
    return render_template('README.md.html',weekl=weekl,leng=len(weekl))


@app.route('/notes/<i>')
def notes(i):
    return render_template(weekl[int(i)]+'.md.html',weekl=weekl,leng=len(weekl))

if __name__ == '__main__':
    app.run(debug=False)
