from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('C:\\Users\\risha\\PycharmProjects\\PythonProject\\sciKit\\Projects\\Project4\\index.html')

if __name__ == '__main__':
    app.run(debug=True)
