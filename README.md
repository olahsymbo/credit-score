# Credit Worthiness Project

This project involves predicting the chances of a customer defaulting on their loan repayment. We used Gradient Boosting Classifier as the predictive model. Training and Testing dataset are in `data` folder. And finally, a Flask API is implemented to serve the model.

## Getting Started

We used python 3.7, sklearn library, and Flask web app framework

1. Clone the repo
2. Create and activate a virtual environment `virtualenv .virtualenv`, and `source .virtualenv/bin/activate`
3. Install the dependencies `pip install -r requirements.txt`

## Training the model

Use the training data in `data` folder and run:

```
python learners/training.py
```

## Serving the model

Simply run:

```
python api/app.py
```
