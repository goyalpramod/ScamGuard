Team Name - PASS </br>
Problem Statement - Fraud App Detection


# ScamGuard

ScamGuard is a web application that helps users determine whether a given Android app is a scam or not. It takes in an APK file, app description, app logo, and app name as inputs and analyzes them to give a verdict on the app's authenticity.

## How it works

ScamGuard uses multiple techniques to analyze the input app and provide a verdict.

- **APK Scan**: ScamGuard scans the permissions of the APK file and uses an Artificial Neural Network (ANN) model to determine if it is malware or not.
- **Description Analysis**: The app description is run through a Long Short-Term Memory (LSTM) model to determine if the app may be fraudulent.
- **App Logo and Name Analysis**: The app logo and name are compared against a database of similar logos and names to calculate a similarity score. If the score is above a certain threshold, the app is declared as a copy app.

## Conclusion

ScamGuard is a valuable tool for Android users who want to ensure that the apps they download are safe and legitimate. By combining multiple techniques for analysis, ScamGuard provides a comprehensive analysis of an app and helps users make informed decisions about whether to install it or not.
