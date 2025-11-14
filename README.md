# Stock Price Movement Prediction with Machine Learning

This academic project applies Machine Learning techniques to predict whether a stock's price will go up or down the next day, using historical data and supervised models. The approach is practical, featuring a functional API, Dockerized environment, and a trained model ready to make predictions based on user-provided inputs.

#  Problem Description
Traders in the stock markets face the constant challenge of making buy or sell decisions in short timeframes, which requires a quick and accurate analysis of asset dynamics. As a tool for refining predictions, an asset highly correlated with the asset being predicted is always used.

The need lies in having an automated, predictive tool that synthesizes this information and suggests a trading direction (up or down). While the ideal solution involves real-time data ingestion (a recurring challenge due to download failures), the immediate problem is validating and deploying a model capable of demonstrating this predictive capability using a fixed dataset for these two correlated assets.

##  Project Objective

The main objective is to develop and deploy a Machine Learning model hosted on an API to generate short-term trading predictions.

The specific objectives are:

Create a decision support tool: Design a model that predicts the direction (buy/sell) of a primary asset, using a correlated asset as the key variable (example: predicted EC with CL=F influence).

Validate the architecture: Demonstrate the feasibility of the solution by building a functional model on a fixed dataset, which can be scaled in the future to ingest real-time data from any pair of correlated assets.

Facilitate deployment: Package the model and the API in a Docker container to provide an easily clonable and executable tool that allows other developers or traders to generate predictions locally and quickly.

## Project Structure

### File / Folder	Description

	1. stock_pred_ec_oil.ipynb	Main notebook with data exploration, model training, and evaluation.
    2  stock_pred_final.py   script file
	3. app.py	Script exposing the model as a REST API using FastAPI.
	4. test_api.py	Unit tests to validate API functionality.
	5. requirements.txt	List of dependencies required to run the project.
	6. Dockerfile	Configuration for containerizing the application.
	7. DATA/	Folder containing the data used to train the model.
	8. best_model.pkl	Trained and serialized model ready to be loaded by the API.
	9. README.md	Project documentation.

## Technologies Used

    -Python 3.10+
    -Scikit-learn
    -Pandas / NumPy
    -FastAPI
    -Docker
    -Pytest

## Example Usage

Once the API is running, you can send a POST request with the following input features:
  
```bash
json

      {
  "Close": 10.0,  
  "Volume": 500000,
  "SMA_100": 12.0,
  "RSI_14": 56.0,
  "WTI_Close": 46.32
       }
```

The response will be:

```bash
json
       {
  "prediction": 1,
  "confidence": 0.6,
  "meaning": "1 = DOWN tomorrow"
        }
```

## Input Explanation

    1. Close: Closing price of the stock on the last trading day.
    2. Volume: Number of shares traded at the close of the last trading day.
    3. SMA_100: 100-period Simple Moving Average at the close of the last trading day.
    4. RSI_14: Relative Strength Index (14-period) at the close of the last trading day.
    5. WTI_Close: Closing price of WTI crude oil on the last trading day.

## Results

The model achieved an accuracy of 53.1% on the test set, using a classifier [specify: RandomForest, XGBoost, etc.]. It was evaluated using metrics such as accuracy, F1-score, and confusion matrix.

## How to run the prediction model
Follow this steps to clone the repository, built the Docker and get a prediction from the API.

### To clone the repository
```bash
git clone https://github.com/Rasosa31/stock_prediction_model.git
cd stock_prediction_model
```

## 🐍 Activate the Conda Environment (Optional, if not using Docker for the test)

Note: If you are only using Docker (the recommended path), you can skip this section. This is for local testing or development.

1. Create the Environment: Choose a unique name (e.g., stock_env).

```Bash
conda create -n stock_env python=3.8
```
(If you prefer another name, replace stock_env.)

2. Activate the Environment:

```Bash
conda activate stock_env
```
3. Install Dependencies:

```Bash
pip install -r requirements.txt
```

## 🐳 The Docker Path (The Easiest Way to Run)

Use two separate terminals. Ensure both terminals are navigated to the root of the project directory (stock_prediction_model).

In the First Terminal (Build & Run):

1. Build the Docker Container: The period (.) is mandatory, as it references the current directory.

```Bash
docker build -t ec-wti-api .
```
2. Run the Docker Container: This starts the API on port 5000 inside the container and exposes it to port 5001 on your local machine.

```Bash
docker run -p 5001:5000 ec-wti-api
```
     Keep this terminal open and running!

## In the Second Terminal (Test the API):

Test the API: This script sends a prediction request to the local address localhost:5001.

```Bash
python test_api.py
```

You should see a prediction displayed like this: json { "prediction": 0, "confidence": 0.72, "meaning": "0 = SUBE mañana" }


## Additional notes

Make sure you have Docker installed: Install Docker
The test_api.py file must be in the repository root or the specified folder.

If port 5001 is in use, you can change it using the `Docker run` command.


## Additional Notes

    NaN values handled via dropna()
    Only 5 inputs required — API computes additional features
    Accuracy: 53.1% (+2.5% improvement with WTI feature)
    Model serialized with joblib (preferred over pickle)

# Credits

This project was developed as part of the Machine Learning Zoomcamp course by DataTalksClub (https://github.com/DataTalksClub/machine-learning-zoomcamp/), for educational and practical exploration in data science and machine learning.