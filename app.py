from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Halo, ini aplikasi Flask pertama saya!"

if __name__ == "__main__":
    app.run(debug=True)