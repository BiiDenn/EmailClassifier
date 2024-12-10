# Email Classification

This project aims to classify emails as **Spam** or **Ham** by leveraging data preprocessing techniques and a deep learning model. It includes data processing, CNN model training, and a basic web interface for users to check their email content.

## Purpose
To solve the problem of email classification, helping users identify spam or non-spam (ham) emails and enhancing email communication efficiency.

## Key Features
1. **Data Preprocessing**:
   - Remove unnecessary columns from the `spam.csv` dataset.
   - Rename columns for better clarity.
   - Eliminate duplicate values and special characters.
   - Retain characters in the ASCII range and convert text to lowercase.
   - Remove excessive white spaces to standardize the data.
2. **Data Splitting and Conversion**:
   - Split the dataset into 80% training and 20% testing subsets.
   - Convert the processed data into formats suitable for the CNN model.
3. **CNN Model Training**:
   - Train and predict using a deep learning Convolutional Neural Network (CNN) model.
   - Evaluate prediction results with performance metrics.
4. **User Interface Development**:
   - Build a basic web application using Flask, HTML, CSS, and JavaScript.
   - Allow users to input email content for immediate classification.

## Technologies Used
- **Programming Languages**: Python, HTML, CSS, JavaScript.
- **Framework**: Flask.
- **Python Libraries**: pandas, numpy, scikit-learn, TensorFlow/Keras.
- **Deep Learning Tool**: Convolutional Neural Network (CNN).

## Future Improvements
- **Data Balancing**:
  - The dataset is imbalanced with 4516 ham emails and 653 spam emails. Methods like **oversampling** or **undersampling** should be applied to balance the data before training.
- **Enhancing Model Performance**:
  - Apply additional deep learning algorithms to improve classification accuracy.
  - Optimize model parameters to enhance training and prediction efficiency.

## Usage
### Installation
1. Clone the repository:
```bash
   git clone https://github.com/<username>/email-classification.git
   cd email-classification
```
2. Install the required libraries:
```bash
  pip install -r requirements.txt
```
3. Run the Flask application:
```bash
python app.py
```
4. Open browser and navigate to:
```bash
http://localhost:5000
```

   
