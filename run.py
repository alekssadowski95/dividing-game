from flaskpackage import app as flask_app

if __name__ == '__main__':
    flask_app.run(host="localhost", port=5000, debug=True)