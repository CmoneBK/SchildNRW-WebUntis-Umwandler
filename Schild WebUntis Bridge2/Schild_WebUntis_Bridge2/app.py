import webbrowser
import threading
import os
from flask import Flask, render_template, request
from pythonS11_3 import run

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        use_abschlussdatum = request.form.get('use_abschlussdatum') == 'on'
        create_second_file = request.form.get('create_second_file') == 'on'
        print(f'use_abschlussdatum: {use_abschlussdatum}')  # Debug print
        print(f'create_second_file: {create_second_file}')  # Debug print
        run(use_abschlussdatum, create_second_file)
        return 'Done!'
    return render_template('index.html')

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    if os.environ.get('FLASK_SERVER_STARTED') != '1':
        # Set the environment variable to prevent the browser from opening again
        os.environ['FLASK_SERVER_STARTED'] = '1'
        
        # Delay the browser opening to ensure the server is up and running
        browser_thread = threading.Timer(1, open_browser)
        browser_thread.start()
    
    app.run(debug=True)
