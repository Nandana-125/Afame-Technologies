from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('sales_prediction_model.pkl')

@app.route('/')
def index():
    return render_template('sales_pred.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    tv_expense = float(data['tvExpense'])
    radio_expense = float(data['radioExpense'])
    newspaper_expense = float(data['newspaperExpense'])

    prediction = model.predict(np.array([[tv_expense, radio_expense, newspaper_expense]]))
    sales = prediction[0]
    
    return jsonify({'sales': sales})

if __name__ == '__main__':
    app.run(debug=True)
