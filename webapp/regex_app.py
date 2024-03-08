from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    regex_results = None
    email_validation_result = None
    if request.method == 'POST':
        if 'input_string' in request.form and 'pattern' in request.form:
            input_string = request.form['input_string']
            pattern = request.form['pattern']
            try:
                regex = re.compile(pattern)
                regex_results = regex.findall(input_string)
            except re.error as e:
                regex_results = [f"Regex Error: {str(e)}"]
        elif 'email' in request.form:
            email = request.form['email']
            if re.match(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', email, re.I):
                email_validation_result = f"The email address {email} is valid."
            else:
                email_validation_result = f"The email address {email} is invalid."

    return render_template('home.html', regex_results=regex_results, email_validation_result=email_validation_result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
