from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])

def getRouter():
    return {'R1': '192.168.5.10'}

if __name__ == '__main__':
    app.run()