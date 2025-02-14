# Breast Cancer Predictor

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## Overview
The **Breast Cancer Predictor** is a web-based application designed to assist medical professionals in predicting whether a tumor is benign (harmless) or malignant (cancerous) based on cell measurements from a cytology lab. The application uses machine learning models to analyze input data and provide predictions along with probabilities for each outcome.

This project is built using Streamlit, a popular framework for creating data-driven web applications, and leverages Plotly for interactive data visualisation. The machine learning model is trained on the _**Breast Cancer Wisconsin (Diagnostic) Dataset**_, which contains features computed from digitized images of fine needle aspirates (FNA) of breast masses.

## Features
### Interactive Sidebar:

Users can input cell nuclei measurements using sliders for various features such as radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension.

The sidebar allows users to adjust the values for mean, standard error, and worst-case measurements.

### Radar Chart Visualisation:

The application generates an interactive radar chart that visualises the scaled values of the input measurements.

The chart displays three traces: Mean, Standard Error, and Worst values for the selected features.

### Prediction Output:

The application predicts whether the tumour is Benign or Malignant based on the input data.

It also provides the probability of the tumour being benign or malignant.

A disclaimer is included to remind users that the tool is meant to assist, not replace, professional medical diagnosis.

### Responsive Layout:

The application is designed with a responsive layout, ensuring a good user experience on both desktop and mobile devices.

## Project Structure
The project is organised into the following components:

* main.py: The main script that runs the Streamlit application. It includes functions for data loading, sidebar creation, scaling input values, generating the radar chart, and making predictions.

* Data/data.csv: The dataset containing breast cancer measurements.

* Model/scaler.pkl: The scaler used to normalise the input data before feeding it into the model.

* Model/model.pkl: The trained machine learning model used for predictions.

* Assets/style.css: Custom CSS styles for the application.

## How It Works
### Data Loading:

The application loads the breast cancer dataset from Data/data.csv.

Unnecessary columns (Unnamed: 32 and id) are dropped, and the diagnosis column is converted to binary values (M for malignant and B for benign).

Rows with missing values are removed.

### Sidebar Input:

The sidebar allows users to input cell nuclei measurements using sliders. The sliders are pre-populated with the mean values from the dataset.

### Data Scaling:

The input values are scaled to a range of 0 to 1 using min-max scaling based on the dataset's minimum and maximum values.

### Radar Chart:

The scaled input values are visualised using a radar chart, which displays the mean, standard error, and worst-case measurements for the selected features.

### Prediction:

The input data is passed through a pre-trained machine learning model to predict whether the tumor is benign or malignant.

The model also outputs the probabilities for each class.

## Installation and Setup
To run the Breast Cancer Predictor application locally, follow these steps:

### Clone the Repository:

(bash)

git clone https://github.com/your-repo/breast-cancer-predictor.git
cd breast-cancer-predictor

### Install Dependencies:
Ensure you have Python 3.7 or higher installed. Then, install the required packages using pip:



(bash)

pip install streamlit pandas plotly numpy scikit-learn

### Run the Application:
Start the Streamlit application by running:


(bash)

streamlit run main.py
Access the Application:
Open your web browser and navigate to http://localhost:8501 to view the application.

## Dependencies
* **Streamlit**: For building and running the web application.

* **Pandas**: For data manipulation and analysis.

* **Plotly**: For creating interactive radar charts.

* **NumPy**: For numerical operations.

* **Scikit-learn**: For loading the pre-trained machine learning model and scaler.

## Future Enhancements
* **Model Retraining**: Allow users to retrain the model with new data.

* **Feature Importance**: Display feature importance scores to help users understand which features contribute most to the prediction.

* **User Authentication**: Add user authentication to restrict access to authorised medical professionals.

* **Export Results**: Allow users to export prediction results and visualisations for further analysis.


Acknowledgments
The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) Dataset, available from Kaggle.

Thanks to the Streamlit and Plotly communities for providing excellent tools for building data-driven applications and most importantly Alejandro AO.

Contact
For any questions or feedback, please contact me at [3foldincrease@gmail.com].

This wiki provides an overview of my Breast Cancer Predictor project, its features, and how to set it up. For more detailed information, refer to the code and documentation in the repository.
