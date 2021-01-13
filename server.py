from flask import Flask
server = Flask(__name__)
@server.route("/")
def hello():
    return "Hello Timmy from MyApp!"

if __name__ == "__main__":
   server.run(debug=True, host='0.0.0.0', port=7000)
