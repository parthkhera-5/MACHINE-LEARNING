# **🚕 NYC Taxi Trip Duration Prediction**

**📄 Project Description**

This project aims to predict the duration of taxi trips in New York City using machine learning regression techniques. By leveraging historical trip data — including pickup/drop-off locations, timestamps, passenger counts, and vendor information — we build models to estimate trip durations accurately. This can help optimize taxi operations and improve passenger experience.

**✨ Features**

**Data Loading & Preprocessing:**

Efficient handling of large datasets, including cleaning, missing value imputation, and type conversions.

**Exploratory Data Analysis (EDA):**

Investigation of trip patterns, spatial and temporal trends, and distribution of trip durations.

**Feature Engineering:**

Creation of new features such as haversine distance, speed, time-based features (hour of day, day of week, month).

**Outlier Detection & Handling:**

Identification and mitigation of extreme values impacting model training.

**Machine Learning Model Training:**

Implementation and comparison of multiple regression algorithms:

Linear Regression

K-Nearest Neighbors (KNN)

Random Forest Regressor

XGBoost Regressor

Gradient Boosting Regressor

**Hyperparameter Tuning:**

Applied GridSearchCV to optimize hyperparameters for Linear Regression, KNN, and Random Forest models, improving accuracy and robustness.

**Model Evaluation:**

Performance assessed using RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error).

**🛠️ Technologies Used**

 | Technology                   | Purpose                                           |
| ---------------------------- | ------------------------------------------------- |
| **Python 3**                 | Core programming language                         |
| **Pandas**                   | Data manipulation and cleaning                    |
| **NumPy**                    | Numerical operations                              |
| **Matplotlib** & **Seaborn** | Data visualization                                |
| **Scikit-learn**             | Model building, hyperparameter tuning, evaluation |
| **Gradient Boost Regressor** | Gradient boosting model (optional)                |
| **XGBoost**                  | Optimized gradient boosting framework             |

**📊 Results and Conclusion**

Hyperparameter tuning with GridSearchCV significantly improved Linear Regression, KNN, and Random Forest performance.

Gradient boosting models (XGBoost and Gradient Boosting Regressor) delivered strong results with minimal tuning.

Feature engineering, especially spatial and temporal features, was critical to model success.

Final models achieved competitive RMSE and MAE scores, demonstrating reliable trip duration prediction.
