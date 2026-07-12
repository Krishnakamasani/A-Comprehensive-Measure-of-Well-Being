# 🌍 A Comprehensive Measure of Well-Being

## Human Development Index (HDI) Prediction System

A Machine Learning web application that predicts the **Human Development Index (HDI)** using **Linear Regression** and **Flask**. The application allows users to enter socio-economic indicators and predicts the corresponding HDI value along with its development category.

---

## 📌 Project Overview

The Human Development Index (HDI) is a statistical measure used to evaluate the overall development of a country based on key indicators such as:

- Life Expectancy at Birth
- Expected Years of Schooling
- Mean Years of Schooling
- Gross National Income (GNI) per Capita

This project builds a Machine Learning model to estimate the HDI from these indicators and provides a user-friendly Flask web interface for predictions.

---

## 🚀 Features

- Data preprocessing and cleaning
- Missing value handling
- Feature selection
- Linear Regression model training
- Model evaluation
- Model serialization using Pickle (`HDI.pkl`)
- Flask backend integration
- Modern and responsive web interface
- Real-time HDI prediction
- HDI category classification:
  - Low HDI
  - Medium HDI
  - High HDI
  - Very High HDI

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Linear Regression

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Web Framework
- Flask

### Frontend
- HTML5
- CSS3

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
A-Comprehensive-Measure-of-Well-Being
│
├── Dataset
│   └── HDI.csv
│
├── Flask
│   ├── app.py
│   ├── HDI.pkl
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   │
│   └── static
│       ├── css
│       │   └── style.css
│       │
│       └── images
│           └── background.jpg
│
├── Training
│   └── HumDevIndex.ipynb
│
├── README.md
└── requirements.txt
```

---

## ⚙️ Machine Learning Workflow

1. Import Required Libraries
2. Load HDI Dataset
3. Explore Dataset
4. Handle Missing Values
5. Select Important Features
6. Split Dataset into Training and Testing Sets
7. Train Linear Regression Model
8. Evaluate Model Performance
9. Save Model using Pickle
10. Build Flask Web Application
11. Deploy Prediction Interface

---

## 📊 Input Features

The prediction model accepts the following inputs:

| Feature | Description |
|---------|-------------|
| Life Expectancy at Birth | Average expected lifespan |
| Expected Years of Schooling | Years of education expected |
| Mean Years of Schooling | Average completed education |
| Gross National Income (GNI) per Capita | Income per person |

---

## 📈 Output

The application predicts:

- Human Development Index (HDI)
- HDI Category

Example:

```
Very High HDI : 0.84
```

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/Krishnakamasani/A-Comprehensive-Measure-of-Well-Being.git
```

### Navigate to Project

```bash
cd A-Comprehensive-Measure-of-Well-Being
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
cd Flask
python app.py
```

### Open Browser

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

### Home Page

> The application provides an attractive user interface for entering HDI-related features.

### Prediction Result

> After submitting the input values, the application predicts the Human Development Index and displays its development category.

---

## 🌐 GitHub Repository

**Repository:**

https://github.com/Krishnakamasani/A-Comprehensive-Measure-of-Well-Being

---

## 🖼️ Background Image

The web interface uses a background image located at:

```text
Flask/static/images/background.jpg

Ensure this file is included in the repository so the application displays the intended UI.


## 📚 Future Improvements

- Support multiple Machine Learning algorithms
- Add data visualization dashboard
- Deploy on Render or Railway
- Mobile responsive design improvements
- Input validation with better error handling
- Database integration for storing predictions


# ✅ Conclusion

This project successfully developed a **Human Development Index (HDI) Prediction System** using **Machine Learning** and **Flask**. A Linear Regression model was trained after preprocessing the dataset, handling missing values, and selecting the most relevant features.

The trained model was integrated into a Flask web application that allows users to enter values such as **Life Expectancy at Birth**, **Expected Years of Schooling**, **Mean Years of Schooling**, and **Gross National Income (GNI) per Capita** to predict the Human Development Index. The application displays both the predicted HDI value and its corresponding development category through a clean and interactive user interface.

This project demonstrates the complete machine learning workflow, including data preprocessing, feature engineering, model training, model serialization using Pickle, backend development with Flask, and frontend integration using HTML and CSS. It provided valuable hands-on experience in building an end-to-end machine learning application and strengthened practical knowledge of Python, Scikit-learn, Flask, Git, and GitHub.
