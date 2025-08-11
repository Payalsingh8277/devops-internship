from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "task 1 :  Automate Code Deployment Using CI/CD Pipeline."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    