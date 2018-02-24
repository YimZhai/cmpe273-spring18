from flask import Flask, jsonify, request
app = Flask(__name__)

num = 0
users = [{
    "id": 1,
    "name": "Hello"
    }]

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/users')
def get_users():
    return jsonify(users)


@app.route('/users', methods=['POST'])
def add_user():
    users = {
        "id": num,
        "name": request.form["name"]
    }
    count += 1
    users.append(request.get_json())
    return '', jsonify(users)



@app.route('/users/<id>')
def get_detail(id):
    users = {
        "id": id,
        "name": request.form["name"]
    }
    return jsonify(users)
                

@app.route("/users/<id>", methods=["DELETE"])
def user_delete(id):
    return "", 204


if __name__ == '__main__':
    app.run(debug=True)
