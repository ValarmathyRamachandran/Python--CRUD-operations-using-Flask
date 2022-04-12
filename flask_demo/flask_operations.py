from json import dumps

from flask import Flask, request, json, Response, jsonify
from mongoengine import connect, Document, StringField, IntField, EmailField

connect(host='mongodb://127.0.0.1:27017/Company')

app = Flask(__name__)


class Employee(Document):
    name = StringField()
    age = IntField()
    email = EmailField()

    def to_json(self):
        return {"name": self.name,
                "age": self.age,
                "email": self.email}


@app.route('/read', methods=['GET'])
def get_records():

    users = Employee.objects()

    if not users:
        return jsonify({'error': 'data not found'})
    else:
        all_employee = [user.to_json() for user in users]
        return {"info": all_employee}


@app.route('/create', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    user = Employee(name=record['name'], age=record['age'], email=record['email'])
    user.save()
    return jsonify(user.to_json())


@app.route('/update', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    users = Employee.objects(name=record['name'])
    if not users:
        return jsonify({'error': 'data not found'})
    else:
        users.update(name=record['name'], age=record['age'], email=record['email'])
        all_employee = [user.to_json() for user in users]
        return {"info": all_employee}


@app.route('/delete', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = Employee.objects(name=record['name'])
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())


if __name__ == "__main__":
    app.run(debug=True)
