# SMS Spam Detection using Machine Learning

## About the Project
This project classifies SMS messages as **Spam** or **Ham (Not Spam)** using Machine Learning. It uses the Multinomial Naive Bayes algorithm to predict whether a message is spam or a legitimate message. The application is built using Streamlit to provide a simple and interactive interface.

## Features
- Enter an SMS message to check whether it is Spam or Ham.
- Predict the message category with a single click.
- Simple and interactive web interface.
- Machine Learning model trained on an SMS dataset.

## Technologies Used
- **Python**
- **Pandas** – Data handling and preprocessing
- **Scikit-learn** – Model training and evaluation
- **Streamlit** – Web application
- **Joblib** – Saving and loading the trained model

## Machine Learning Model
The project uses the **Multinomial Naive Bayes** classifier for text classification.

The model is trained on labeled SMS messages containing two categories:
- **Ham:** Legitimate messages.
- **Spam:** Unwanted or fraudulent messages.

## Dataset
The dataset contains SMS messages labeled as spam or ham. It is used to train and evaluate the classification model.

## Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/pro-unnati/spam-ham-classifier.git
```

### 2. Navigate to the project directory
```bash
cd spam-ham-classifier
```

### 3. Install the required libraries
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application
```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## How to Use
1. Launch the application.
2. Enter an SMS message in the input field.
3. Click the **Predict** button.
4. View the predicted result: Spam or Ham.

## Project Structure
```text
spam-ham-classifier/
├── app.py
├── spam.csv
├── spam_ham_model.pkl
├── requirements.txt
└── README.md
```

*Note: The file structure above is an example. Adjust it according to the actual files in your repository.*

## Future Improvements
- Improve spam detection for messages containing misleading or unfamiliar phrases.
- Evaluate additional text classification algorithms.
- Enhance model performance using text preprocessing and feature engineering.
- Deploy the application online for public access.

## Author
**Unnati Gupta**

GitHub: [pro-unnati](https://github.com/pro-unnati)

---

If you find this project useful, feel free to explore the repository and share your feedback.
