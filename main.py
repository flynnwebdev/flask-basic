from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  return '<h3>Hello world!</h3>'

@app.route('/spam')
def spam():
  person = {'name': 'John', 'age': 21}
  return person

# Second segment of the URI is a RESTful parameter called 'foo'
# Flask does this:
#   1. Creates a variable called 'foo'
#   2. Set the 'foo' variable to the value in the URI in the same position as the parameter
#   3. Calls the handler function, passing in 'foo'
@app.route('/hello/<string:foo>')
def hello(foo):
  # foo = request.args.get('name')
  return {'message': f'Hello, {foo}!'}

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
  return {'result': num1 + num2}

@app.errorhandler(404)
def not_found(error):
  return {'error': str(error)}, 404

if __name__ == '__main__':
  app.run(debug=True)
