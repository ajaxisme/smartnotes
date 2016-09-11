from flask import Flask, jsonify, request
import termextract

app = Flask(__name__)

@app.route('/suggestions')
def serve():
    text = ''
    with open('sample', 'r') as f:
        text = f.read()

    q = request.args.get('q') 
    data = list(termextract.get_matching_lines(text, q))
    callback = request.args.get('callback')
    return "%s(%s)" % (callback, data)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
