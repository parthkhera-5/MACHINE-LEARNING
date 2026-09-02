# 🎬 Movie Recommendation System

## 📌 Project Overview
This project is a **Content-Based Movie Recommendation System** that suggests movies similar to a given title based on their content features. Unlike collaborative filtering, this system does not depend on user ratings but instead analyzes movie metadata such as genres, keywords, cast, director, and overview.

---

## 🚀 Features
- Content-based filtering approach
- TF-IDF vectorization for text processing
- Cosine similarity for recommendation
- Fuzzy matching for user input
- Data preprocessing and feature engineering
- 15+ data visualizations (UBM: Univariate, Bivariate, Multivariate)
- Clean, structured, and reproducible code

---

## 🧠 Problem Statement
Users often face difficulty choosing movies due to the large volume of available content. This system helps users by recommending movies based on similarity in content, improving user experience and reducing decision fatigue.

---

## 📂 Dataset Information
- Total Movies: **4803**
- Total Features: **24**

### Important Features Used:
- Genres
- Keywords
- Tagline
- Cast
- Director
- Overview

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Libraries:**
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - difflib
  - wordcloud

---

## ⚙️ Project Workflow

### 1. Data Preprocessing
- Handled missing values
- Converted `release_date` to datetime
- Filled null values with empty strings
- Cleaned and prepared text data

### 2. Feature Engineering
- Selected relevant columns
- Combined features into a single column (`combine`)
- Prepared text for vectorization

### 3. Text Processing
- Lowercasing
- Removing punctuation
- Removing stopwords
- Stemming / normalization

### 4. Vectorization
- Applied **TF-IDF Vectorizer**
- Converted text into numerical vectors

### 5. Similarity Calculation
- Used **Cosine Similarity**
- Created similarity matrix of shape (4803 x 4803)

### 6. Recommendation System
- Takes movie name as input
- Finds closest match using fuzzy matching
- Returns top similar movies

---

## 📊 Data Visualization
Performed structured analysis using UBM rule:

### 🔹 Univariate Analysis
- Genre distribution
- Runtime distribution
- Vote average histogram

### 🔹 Bivariate Analysis
- Budget vs Revenue
- Popularity vs Revenue
- Language vs Ratings

### 🔹 Multivariate Analysis
- Correlation heatmap
- Pair plots
- Stacked bar charts (language vs time)

---

## 🤖 Machine Learning Model

### Model Used:
- **Content-Based Filtering**
- TF-IDF + Cosine Similarity

### Why this model?
- Does not require user data
- Efficient for text similarity
- Easy to implement and scale

---

## 📈 Evaluation Metrics
- Cosine similarity score
- Recommendation relevance (manual evaluation)

### Business Impact:
- Improves user engagement
- Helps users discover relevant movies
- Reduces time spent searching for content

---

## 🔧 Future Improvements
- Implement Collaborative Filtering
- Build Hybrid Recommendation System
- Use NLP embeddings (Word2Vec, BERT)
- Deploy using Streamlit or Flask
- Add user personalization

---

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/movie-recommendation-system.git

# Navigate to project directory
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run Jupyter Notebook
