# 📚 Book Recommendation System Using Content-Based Filtering

## 📖 Overview

The **Book Recommendation System** is a machine learning project that recommends books based on their textual content. It uses **Natural Language Processing (NLP)** techniques such as **TF-IDF Vectorization** and **Cosine Similarity** to identify books that are similar to a selected book.

The system also supports **partial title search** and **spelling correction** using Python's `difflib` library, making it easier for users to search for books even if they do not remember the exact title.

---

## 🚀 Features

* Search books by title.
* Supports partial title matching.
* Handles spelling mistakes using `difflib`.
* Recommends similar books using content-based filtering.
* Displays:

  * Title
  * Author
  * Category
  * Description
  * Average Rating
  * Similarity Score
* Clean and easy-to-understand recommendation output.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* difflib

---

## 📂 Dataset

Dataset used:

**Books Dataset** (Kaggle)

Contains information such as:

* Book Title
* Subtitle
* Authors
* Categories
* Description
* Average Rating

---

## 📌 Project Workflow

### 1. Load Dataset

The dataset is loaded using Pandas.

```python
df = pd.read_csv("data.csv")
```

---

### 2. Data Preprocessing

* Handle missing values.
* Merge important text columns into one column named **content**.
* Convert text to lowercase.
* Remove unnecessary white spaces.

Merged columns:

* Title
* Subtitle
* Authors
* Categories
* Description

---

### 3. TF-IDF Vectorization

The combined text is converted into numerical vectors using **TF-IDF Vectorizer**.

```python
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["content"])
```

---

### 4. Cosine Similarity

The cosine similarity matrix is generated to measure similarity between every pair of books.

```python
similarity = cosine_similarity(tfidf_matrix)
```

---

### 5. Recommendation Process

When the user enters a book name:

1. Search the title in the dataset.
2. If the title is not found, use **difflib** to find the closest matching title.
3. Select the matched book.
4. Retrieve similarity scores from the cosine similarity matrix.
5. Sort books by similarity.
6. Return the top recommended books.

---

## 📊 Machine Learning Technique

This project uses **Content-Based Filtering**.

Unlike collaborative filtering, recommendations are generated using the information available about the books rather than user ratings or user behavior.

---

## 📐 Similarity Measure

The project uses **Cosine Similarity**.

Cosine Similarity measures the angle between two TF-IDF vectors.

* Value close to **1** → Highly Similar
* Value close to **0** → Not Similar

---

## 🔍 Libraries Used

```text
pandas
numpy
matplotlib
scikit-learn
difflib
```

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

* Data Cleaning
* Feature Engineering
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Cosine Similarity
* Content-Based Recommendation System
* Fuzzy String Matching
* Python Data Analysis
* Machine Learning Pipeline
