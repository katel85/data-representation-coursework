from flask import Flask
app = Flask(__name__, static_url_path='', static_folder = 'staticpages')

@app.route('/user/<username>', methods=['GET'])
def getuser(username):
    return 'Hi there whats happening' + username

@app.route('/user', methods=['POST'])
def postuser():
    return 'Hi there is this message posting on postman'

if __name__ == "__main__":
    app.run(debug=True)
