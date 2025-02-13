from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, 你好!"
if __name__ == '__main__':
    app.run(port=5050)
