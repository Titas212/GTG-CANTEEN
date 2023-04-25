from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<html><body><h1 style='color:blue'>GTG Online</h1></body></html>"

@app.route("/products")
def products():
    return "<html><body><h1 style='color:green'>Coming soon...</h1></body></html>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')