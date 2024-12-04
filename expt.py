from flask import Flask, request

app = Flask(_name_)

@app.route('/')
def index():
    return '''
        <form action="/convert" method="post">
            Temperature (°C): <input type="text" name="temp_c">
            <input type="submit" value="Convert">
        </form>
    '''

@app.route('/convert', methods=['POST'])
def convert():
    try:
        temp_c = float(request.form['temp_c'])
        temp_f = (temp_c * 9/5) + 32
        return f"{temp_c}°C = {temp_f}°F"
    except ValueError:
        return "Invalid input. Please enter a numeric value."

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
