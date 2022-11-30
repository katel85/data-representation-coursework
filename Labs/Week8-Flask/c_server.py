from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Hi there Mam"

@app.route('/datainquery', methods=['GET'])
def inquery():
    #making this into a dictionary 
    queryargs={
        "firstname": request.args["firstname"],
        "age": request.args["age"]
    }
    print(queryargs)
    #firstname = request.args["firstname"]
    #return "Your name is " + firstname
    return jsonify(queryargs)

@app.route('/dataasjson', methods=['POST'])
def asjson():
    #making this into a dictionary 
    book={
        
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]

    }

    # put into a database
    print(book)
    return jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)