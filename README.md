# 🚀 NLP Model Training & Inference Project

> ⚠️ **Project Status**: In Progress  
> This project is not yet complete. Some manual steps are required to run or train the model.

---

## 📁 Project Overview

This is a simple NLP project using a custom-trained model built with TensorFlow and served via Flask. You can either use the pre-trained model or train a new one using the provided dataset and notebook.

---

## 📥 Requirements

To run this project, you need to download the **pre-trained model** and **tokenizer** manually.

### 🔗 Downloads

- **Model & Tokenizer**  
  [📁 Google Drive Folder](https://drive.google.com/drive/folders/1-Wha_doXW39ijTUQHWuXKkshOLLY4y9v?usp=drive_link)

- **Dataset (700,000+ Rows)**  
  The same folder includes a large dataset used for model training and testing.

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-link>
   cd <your-project-folder>
   

2. **Install required packages:**
   Make sure Python is installed (Python 3.7+ recommended), then run:

pip install -r requirements.txt 
requirements.txt includes:

flask
tensorflow
gunicorn
numpy

3. **Add model and tokenizer files:**

  Download the model and tokenizer from the Drive folder above.

  Place all the model and tokenizer files in the same directory as app.py.

## 🚀 Running the Project

Once everything is ready:

python app.py

This will start the Flask server locally, and the model will be ready to serve predictions.

## 🧠 Training a New Model

If you want to train your own model using the provided dataset:
1.Download the dataset and training notebook (.ipynb) from the same Drive folder.
2.Place the dataset and notebook in your project directory.
3.Open the notebook and follow the instructions to:
  Load and preprocess the data
  Train the model
  Evaluate and save the model/tokenizer
  Upload the trained model to Google Drive if needed

##  📂 Folder Structure

/project-folder
│
├── app.py
├── requirements.txt
├── model/           ← Pre-trained model files (optional)
├── tokenizer/       ← Tokenizer files (optional)
├── dataset.csv      ← Dataset (optional, for training)
└── train_model.ipynb← Jupyter notebook for training (optional)

