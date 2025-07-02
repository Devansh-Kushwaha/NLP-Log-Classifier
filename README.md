# Hybrid Log Classification Framework

This project implements a hybrid system for log classification, combining three complementary techniques to address different levels of complexity in log data. The framework offers both flexibility and accuracy when dealing with structured, unstructured, and poorly labeled logs.

---

## Classification Techniques

1. **Regex-Based Classification**  
   - Ideal for simple, repetitive, and structured log formats.  
   - Uses predefined regular expressions to classify logs efficiently.

2. **Sentence Transformers + Logistic Regression**  
   - Suitable for complex log patterns when sufficient labeled data is available.  
   - Generates semantic embeddings using Sentence Transformers and applies Logistic Regression for classification.

3. **Large Language Models (LLMs)**  
   - Best for complex, unstructured logs with limited labeled data.  
   - Acts as a fallback or augmentation when other methods are insufficient.


---

## Project Structure

- **`training/`** – Code for regex-based classification and model training using Sentence Transformers and Logistic Regression.  
- **`models/`** – Saved models including embeddings and classifiers.  
- **`resources/`** – Includes sample CSV files, result outputs, and reference images.  
- **Root Directory** – Contains the FastAPI server code (`server.py`).

---

## Getting Started

### Step 1: Install Dependencies

Make sure Python is installed on your machine. Then run:

```bash
pip install -r requirements.txt
```

### Step 2: Start the FastAPI Server

Launch the server with:

```bash
uvicorn server:app --reload
```

API will be available at:
- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) – Main API endpoint  
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – Swagger documentation  
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) – ReDoc documentation

---

## Usage Instructions

Upload a CSV file to the API containing logs to be classified. The file must include the following columns:

- `source`  
- `log_message`

The output will be a CSV with an added `target_label` column representing the predicted category.

---

## Disclaimer

This project and its content are provided for educational purposes only. Commercial use is prohibited without proper authorization.
