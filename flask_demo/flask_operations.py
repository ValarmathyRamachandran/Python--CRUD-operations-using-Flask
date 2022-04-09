from flask import Flask, request, json, Response, jsonify
from mongoengine import connect, Document, StringField, IntField, EmailField

connect(host='mongodb://127.0.0.1:27017/Company')

app = Flask(__name__)


class Employee(Document):
    name = StringField()
    age = IntField()
    email = EmailField()


@app.route('/create', methods=['POST'])
def create_new_employee():
    body = json.loads(request.data)
    print(body)
    name = body.get('name')
    age = body.get('age')
    email = body.get('email')
    employee = Employee(name=name, age=age, email=email)
    print('new employee added')
    employee.save()
    return {'message': 'success'}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
