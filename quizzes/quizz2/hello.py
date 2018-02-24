from flask import Flask, jsonify, request, json
app = Flask(__name__)

num = 1
userList = {}

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/users', methods=['POST'])
def add_user():
    global num
    users = {
        "id": num,
        "name": request.form["name"]
    }
    userList[str(num)] = request.form["name"]
    num = num+ + 1
    return jsonify(users), 201


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    if id in userList:
        users = {
        "id": id,
        "name": userList[id]
        }
        return jsonify(users)
    else:
        return "User doesn't exist.", 204
    
           
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    del userList[id]
    return "", 204


if __name__ == '__main__':
    app.run(debug=True)
