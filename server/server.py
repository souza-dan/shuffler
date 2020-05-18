from flask import Flask, render_template, request, jsonify

import random

app = Flask(__name__, template_folder="./")

# apis
@app.route('/api/v1/hello')
def api_modules():
    return ('hello world')


@app.route('/api/v1/shuffle', methods=['POST'])
def api_generate_title():
    csv = request.form.get('list')
    separator = request.form.get('separator')
    if not separator:
        separator = ","
    if csv:
        csv_list = ([x for x in request.form.get('list').split(",")])
        random.shuffle(csv_list)
        return jsonify(separator.join(csv_list))
    return jsonify(["no values"])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
