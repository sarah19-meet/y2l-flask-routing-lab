from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def home():
    return render_template("shop.html")

@app.route('/list')
def list1():
    colors=["red","grey","yellow"]
    return render_template("hello_Vars.html", colors=colors)



if __name__ == '__main__':
   app.run(debug = True)
