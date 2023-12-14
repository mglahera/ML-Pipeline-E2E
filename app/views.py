from flask import render_template
from app import app
from src.pipeline.process import process_data
from src.pipeline.train import train_model

@app.route('/')
def index():
    data = process_data()
    prediction = train_model(data)
    return render_template('index.html', prediction=prediction)