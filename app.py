from integral import calculate_integrals
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/integral/<lower>/<upper>', methods=['GET'])
def integral_service(lower, upper):
    result = calculate_integrals(float(lower), float(upper))
    return jsonify(result)

