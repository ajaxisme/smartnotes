from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addTranscript', methods=['POST'])
def addTranscript():
   text = request.form['transcript']
   text = text.encode('ascii', 'ignore')
   with open('api/sample', 'w') as f:
       f.write(text)
   return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
