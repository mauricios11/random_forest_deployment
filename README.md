# Random Forest + XGBoost Stacking Deployment for Streamlit

This project showcases the deployment of a Stacking model that combines Random Forest and XGBoost for predicting income levels based on demographic and economic features. The deployment is built using Streamlit, offering an interactive and user-friendly interface to make predictions.

* 🎯 **Objective**: The primary goal of this project is to deploy a robust machine learning model for predicting whether an individual earns more than 50K USD annually based on input features like age, marital status, education, and hours worked per week. The project demonstrates the entire pipeline, from training the stacking model to deploying it on Streamlit.

## Description:

* **Stacking Model**: Combines the predictive power of Random Forest and XGBoost to improve overall performance.

* **Streamlit Frontend**: A simple and interactive web interface for users to input data and receive predictions.

* **Probability Outputs**: Displays both the predicted class *(income >50K or <=50K)* and the associated probabilities.

🛠️ Tools and Technologies: *Python, Streamlit, Scikit-learn, XGBoost, Joblib, Git LFS (Large File Storage)*

### 🚧 Challenges Faced

During the project, we encountered a notable challenge: Large Model File Size 📂

* The trained model file (stacking_optimized_0.pkl) exceeded 285 MB, surpassing GitHub's 100 MB file size limit. This caused push operations to fail with errors such as:

```File app/model/stacking_optimized_0.pkl is 285.17 MB; this exceeds GitHub's file size limit of 100.00 MB```

To solve this I configured Git LFS (Large File Storage) to handle the large model file efficiently:

Installed Git LFS with:

```git lfs install

#Configured Git LFS to track the model file:

git lfs track "app/model/stacking_optimized_0.pkl"

#Added and pushed the file successfully
```

📁 Project Structure

```project-folder/
|
|-- app/
|   |-- assets/                 # Static assets (e.g., images, stylesheets)
|   |-- model/                  # Contains the trained stacking model (tracked with Git LFS)
|   |   |-- stacking_optimized_0.pkl
|   |-- app.py                  # Main Streamlit app script
|   |-- utils.py                # Helper functions (e.g., model predictions)
|   |-- requirements.txt        # Python dependencies
|
|-- env/                        # Local environment (not included in GitHub)
|-- README.md                   # Project description and setup guide
```

### To Run Locally

Clone the repository:

`git clone <repository-url>`

Navigate to the project folder. Then install dependencies:

`pip install -r app/requirements.txt`

Run the Streamlit app:

`streamlit run app/app.py`

Open the app in your browser at http://localhost:#### 🌐


