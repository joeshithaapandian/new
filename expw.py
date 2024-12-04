from flask import Flask

app = Flask(_name_)

@app.route('/')
def welcome():
    return "Welcome to Google App Engine!"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
