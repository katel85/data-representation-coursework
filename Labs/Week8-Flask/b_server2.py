from flask import Flask, url_for, redirect
app = Flask(__name__, static_url_path='', static_folder = 'staticpages')

@app.route('/')
def index():
    return"<a href="+url_for('getuser') + ">getusers</a>"

@app.route('/user', methods=['GET'])
def getuser():
    return 'Hi there whats happening '

'''@app.route('/user/<username>', methods=['GET'])
def getuser(username):
    return 'Hi there whats happening ' + username'''

@app.route('/user/<int:id>', methods=['GET'])
def getuserbyid(id):
    return 'Getting my id' + str(id)

@app.route('/user', methods=['POST'])
def postuser():
    return 'Hi there is this message posting on postman'

@app.route('/invalid',methods=['GET'])
def invalid():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)




