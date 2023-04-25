from flask import Flask, render_template, request
import numpy as np
import pickle
import sklearn

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))


@app.route("/")
def about():
    return render_template('home.html')




if __name__ == "__main__":
    app.run(debug=False)
