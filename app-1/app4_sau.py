from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "Home Page"
    return render_template("home.html")

@app.route('/about/')
def about():
    #return "Website content goes here!"   
    return render_template("about.html") 

@app.route('/image/')
def image():
    return render_template("image.html")    

if __name__ == "__main__":
    app.run(debug=True)
