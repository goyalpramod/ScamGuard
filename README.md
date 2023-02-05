Team Name - PASS </br>
Problem Statement - Fraud App Detection


# ScamGuard

ScamGuard is a web application that helps users determine whether a given Android app is a scam or not. It takes in an APK file, app description, app logo, and app name as inputs and analyzes them to give a verdict on the app's authenticity.

## How it works

ScamGuard uses multiple techniques to analyze the input app and provide a verdict.

- **APK Scan**: ScamGuard scans the permissions of the APK file and uses an Artificial Neural Network (ANN) model to determine if it is malware or not.
- **Description Analysis**: The app description is run through a Long Short-Term Memory (LSTM) model to determine if the app may be fraudulent.
- **App Logo and Name Analysis**: The app logo and name are compared against a database of similar logos and names to calculate a similarity score. If the score is above a certain threshold, the app is declared as a copy app.
- **VirusTotal check**: An additional check is run on the apk via the VirusTotal API to check whether any malware may be present or not, It runs through multiple virus checks from various platforms present in VirusTotal

## Conclusion

ScamGuard is a valuable tool for Android users who want to ensure that the apps they download are safe and legitimate. By combining multiple techniques for analysis, ScamGuard provides a comprehensive analysis of an app and helps users make informed decisions about whether to install it or not.
![Screenshot (222)](https://user-images.githubusercontent.com/77145616/216807165-e111746f-0274-4b83-83f7-5805478a2dd9.png)
![Screenshot (224)](https://user-images.githubusercontent.com/77145616/216807202-63691e34-0b5e-4017-bcc3-e0cdb0a7c0e5.png)
![Screenshot (225)](https://user-images.githubusercontent.com/77145616/216807204-2608d6a7-acf6-48e3-8c04-eb57a671d566.png)
![Screenshot (226)](https://user-images.githubusercontent.com/77145616/216807205-4c66e6db-5284-4053-9d08-ed621eea9723.png)
