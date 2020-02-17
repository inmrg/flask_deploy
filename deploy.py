from flask import Flask, render_template

vport = 5002  #define el puerto de salida
vdebug = False #define si esta modo depuracion para desarrollo

app = Flask(__name__)



@app.route('/')
def home():
    return '<h1> deploy to heroku!!</h1>'



if __name__ == "__main__":
    app.run(port=vport, debug=vdebug)