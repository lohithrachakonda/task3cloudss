from flask import Flask, jsonify
from integral import calculate_integrals

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Integral Calculator! Use the /integral/<lower>/<upper> endpoint to calculate integrals.'

@app.route('/integral/<lower>/<upper>', methods=['GET'])
def integral_service(lower, upper):
    result = calculate_integrals(float(lower), float(upper))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

