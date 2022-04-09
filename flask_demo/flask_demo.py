from flask import Flask, request

app = Flask(__name__)

my_dict = {
    'name': 'valar',
    'job': 'Software Developer',
    'location': 'chennai'

}


@app.route("/")
def hello_world():
    return 'hello world'


@app.route('/info')
def get_info():
    print[request.args.to_dict()]
    param = request.args.get('param')
    print(my_dict.get(param))
    return {param: my_dict.get(param)}


if __name__ == '__main__':
    app.run(debug=True, port=4000)
