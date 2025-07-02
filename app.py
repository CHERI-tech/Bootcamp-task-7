from flask import Flask,jsonify
import random
from quotes import quotes
from flask import render_template
app=Flask(__name__)

@app.route('/',methods=['GET'])
def get_quote():
     quote=random.choice(quotes)
     return render_template('index.html', quote=quote)

if __name__=='__main__':
     app.run(debug=True)