import json
from flask import (Flask, jsonify)

app = Flask(__name__)


@app.route('/invoices')
def get_invoices():
    return jsonify({})


app.run()
