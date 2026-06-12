# Phishing Email Detection Model

A Machine Learning-based web application that detects phishing emails using Natural Language Processing (NLP) and Scikit-learn.
* live demo: https://phishing-email-detector-qnfh.onrender.com/
## Features

* Detects phishing and legitimate emails
* Uses TF-IDF for text feature extraction
* Trained using Multinomial Naive Bayes
* Web interface built with Flask
* Displays email classification results instantly

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* Joblib
* HTML/CSS

## Dataset

The model was trained on a dataset containing phishing and legitimate emails with over 82,000 records.

## Model Performance

* Accuracy: 96.24%


## Usage

1. Paste email content into the text area.
2. Click "Analyze Email".
3. View the prediction:

   * Phishing
   * Safe

## Future Improvements

* URL feature extraction
* Risk scoring
* Email header analysis
* Advanced phishing detection models
