# Machine Predictive Maintainance

### 📌 Overview
This project is a *Machine Predictive Maintenance System* built using *Streamlit* and *Machine Learning* to predict whether a machine will suffer failure based on various input parameters like temperature, torque, rotational speed, and tool wear.




## 📂 Project Structure

📂 machine-predictive-maintainance/

│── 📜 app.py                # Streamlit web app for predictions

│── 📜 model.joblib           # Pre-trained machine learning model

│── 📜 requirements.txt       # Dependencies for deployment

│── 📜 README.md              # Project documentation (this file)

│── 📂 data/                  # (Optional) Dataset files




## 📌 Features

✅ Predicts machine failure based on input parameters
✅ Displays failure reasons & preventive measures
✅ Interactive Streamlit UI for easy usage
✅ Data visualization for insights into input parameters



## ⚙ Installation & Setup

#### 1️⃣ Clone the Repository
    git clone https://github.com/VyshnaviVunnamatla/machine-predictive-maintainance.git
    cd machine-predictive-maintainance

#### 2️⃣ Install Dependencies

Make sure you have Python installed, then run:
        
    pip install -r requirements.txt

#### 3️⃣ Run the Streamlit App

    streamlit run app.py

## 📊 Input Parameters for Prediction

<table align="center">
  <tr>
    <th>Parameter</th>
    <th>Description</th>
    <th>Example Value</th>
  </tr>
  <tr>
    <td>Machine Type</td>
    <td>Type of machine (Low/Medium/High)</td>
    <td>Low</td>
  </tr>
  <tr>
    <td>Air Temperature (K)</td>
    <td>Temperature of air in Kelvin</td>
    <td>300</td>
  </tr>
  <tr>
    <td>Process Temperature (K)</td>
    <td>Temperature of the process in Kelvin</td>
    <td>350</td>
  </tr>
  <tr>
    <td>Rotational Speed (rpm)</td>
    <td>Speed of rotation in rpm</td>
    <td>1500</td>
  </tr>
  <tr>
    <td>Torque (Nm)</td>
    <td>Torque applied in Nm</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Tool Wear (min)</td>
    <td>Tool wear in minutes</td>
    <td>120</td>
  </tr>
</table>




## 🎯 Model Details

1. The trained model is a Random Forest Classifier stored as **model.joblib** .

2. It predicts whether the machine will fail or not based on the given input values.




## 🚀 Deployment on Streamlit Cloud

To deploy the app on Streamlit Community Cloud, follow these steps:

1. Push your code to a public GitHub repository.

2. Go to *Streamlit cloud* - https://share.streamlit.io/.

3. Click "New App", select your repo, and set app.py as the main file.

4. Click Deploy! 🎉




## 🤝 Contributing

Feel free to fork the repo, open issues, or submit pull requests to improve this project!




## 📜 License

This project is licensed under the MIT License.
