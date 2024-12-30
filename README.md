# *Random Forest* + *XGBoost Stacking* Deployment for Streamlit

This project showcases the deployment of a Stacking model that combines **Random Forest** and **XGBoost** for predicting income levels based on demographic and economic features. The deployment is built using Streamlit.

* 🎯 **Objective**: Deploy a robust ML model for predicting $\rightarrow$ whether an individual earns more than 50K USD annually based on input features like *age, marital status, education, etc.*.
* The project demonstrates the entire pipeline: [project repo](https://github.com/mauricios11/income_classif_eda), from the entire EDA, then impute missing values, then balance the target column, and finally training a stacking model to deploying it on Streamlit.

* To use the app enter to the next link: "[Income Prediction APP ](https://mauricios11-random-forest-deployment.streamlit.app/)"

## Description:

* **Stacking Model**: Combines the fusion of the power fo two models: *Random Forest* and *XGBoost* to improve overall performance.

* **Streamlit Frontend**: Just a simple web interface for users to input data and receive predictions.

* **Probability Outputs**: Displays both the predicted class *(income >50K or <=50K)* and the associated probabilities.

🛠️ Tools and Technologies: *Python, Streamlit, Scikit-learn, XGBoost, Joblib, Git LFS (Large File Storage)*

📁 Project Structure:

```
project-folder/
|
|-- app/
|   |-- model/                  # trained stacking model (tracked with Git LFS)
|   |   |-- stacking_optimized_0.pkl
|   |-- app.py                  # main streamlit script
|   |-- utils.py                # helper functions (model predictions)
|   |-- requirements.txt        # dependencies
```

### To Run Locally

Clone the repository:

`git clone https://github.com/mauricios11/random_forest_deployment.git`

Navigate to the project folder. Then install dependencies:

`pip install -r app/requirements.txt`

Run the Streamlit app:

`streamlit run app/app.py`

Open the app in your browser at http://localhost:#### 🌐


