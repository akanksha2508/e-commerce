from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/')
@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/forget/')
def forget():
    return render_template('forget.html')

@app.route('/home/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug = True)
