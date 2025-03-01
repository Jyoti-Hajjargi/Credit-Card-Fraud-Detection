# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GrDe7E9awOZvFQu1HHRVHjLwTbVhJlqS
"""

# Data manipulation and analysis
import pandas as pd
import numpy as np

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Evaluation Metrics
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Ignore warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

from google.colab import files
upload = files.upload()

# Load the dataset
df = pd.read_csv('creditcard.csv')

# Display the first 5 rows to verify
print(df.head())

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Distribution of the target variable
sns.countplot(x='Class', data=df)
plt.title('Distribution of Fraudulent (1) and Non-Fraudulent (0) Transactions')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# Features and target variable
X = df.drop('Class', axis=1)
y = df['Class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Verify the split
print(f'Training set size: {X_train.shape}')
print(f'Test set size: {X_test.shape}')

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data
X_test_scaled = scaler.transform(X_test)

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)

# Fit the KNN model on the training data
knn.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred_knn = knn.predict(X_test_scaled)

# Initialize Logistic Regression model
log_reg = LogisticRegression()

# Fit the Logistic Regression model on the training data
log_reg.fit(X_train_scaled, y_train)

# Make predictions on the test data
y_pred_log_reg = log_reg.predict(X_test_scaled)

# Confusion Matrix for KNN
conf_matrix_knn = confusion_matrix(y_test, y_pred_knn)
print("Confusion Matrix for KNN:")
print(conf_matrix_knn)

# Visualize the confusion matrix
sns.heatmap(conf_matrix_knn, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - KNN')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Confusion Matrix for Logistic Regression
conf_matrix_log_reg = confusion_matrix(y_test, y_pred_log_reg)
print("Confusion Matrix for Logistic Regression:")
print(conf_matrix_log_reg)

# Visualize the confusion matrix
sns.heatmap(conf_matrix_log_reg, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix - Logistic Regression')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report for KNN
class_report_knn = classification_report(y_test, y_pred_knn)
print("Classification Report for KNN:")
print(class_report_knn)

# Classification Report for Logistic Regression
class_report_log_reg = classification_report(y_test, y_pred_log_reg)
print("Classification Report for Logistic Regression:")
print(class_report_log_reg)

# Accuracy Score for KNN
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"Accuracy for KNN: {accuracy_knn:.4f}")

accuracy_log_reg = accuracy_score(y_test, y_pred_log_reg)
print(f"Accuracy for Logistic Regression: {accuracy_log_reg:.4f}")

print(f"KNN Accuracy: {accuracy_knn:.4f}")
print(f"Logistic Regression Accuracy: {accuracy_log_reg:.4f}")