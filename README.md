# 🤖 AI Resume Screening & Job Recommendation System

An intelligent, NLP-powered recruitment platform designed to automate resume parsing, match candidate profiles against job descriptions, calculate semantic match scores, and provide actionable candidate suitability recommendations.

---

## 📌 Problem Statement

In modern recruitment, hiring teams and talent acquisition professionals receive hundreds—sometimes thousands—of applications for a single job opening. Manually screening every resume is **time-consuming, repetitive, prone to human error, and subject to implicit bias**.

This project addresses these challenges by delivering an automated end-to-end AI workflow that:
- Accepts candidate resumes in PDF / DOCX formats.
- Extracts and cleans unstructured resume text.
- Parses core candidate metadata, technical skills, experience, and education.
- Compares candidate profiles against detailed Job Descriptions (JDs) using advanced Natural Language Processing (NLP) and vector embeddings.
- Computes a multi-dimensional **Matching Score** (0–100%).
- Generates intelligent **Suitability Recommendations** and automated candidate gap analysis.

---

## 🔄 System Architecture & Workflow

```
┌─────────────────┐       ┌──────────────────┐       ┌────────────────────────┐
│ Candidate Resume│ ────► │ Text Extraction  │ ────► │ Text Preprocessing &   │
│   (PDF / DOCX)  │       │ (pdfplumber/PyPDF│       │ Cleaning (NLTK/SpaCy)  │
└─────────────────┘       └──────────────────┘       └───────────┬────────────┘
                                                                 │
                                                                 ▼
┌─────────────────┐       ┌──────────────────┐       ┌────────────────────────┐
│ Final Report &  │ ◄──── │ Match Engine &   │ ◄──── │ Feature Extraction     │
│ Candidate Score │       │ Scoring Matrix   │       │ (TF-IDF / Embeddings)  │
└─────────────────┘       └──────────────────┘       └────────────────────────┘
```

### Detailed Pipeline Workflow
1. **Resume Ingestion:** Upload PDF / Word documents via web portal or REST API.
2. **Text Extraction:** Extract raw text using PyPDF2 / pdfplumber with OCR support (Tesseract) for scanned documents.
3. **Text Cleaning & Preprocessing:** Tokenization, stop-word removal, lemmatization, and lowercasing.
4. **Information & Skill Extraction:** Named Entity Recognition (NER) and pattern matching to extract skills, certifications, work experience duration, and education.
5. **Semantic Similarity & Matching:** Calculate Cosine Similarity based on TF-IDF matrices and Sentence-Transformers (BERT/RoBERTa embeddings).
6. **Scoring & Evaluation Engine:**
   - **Skill Match Score** (Weight: 40%)
   - **Semantic Similarity Score** (Weight: 40%)
   - **Experience & Education Weightage** (Weight: 20%)
7. **Recommendation & Dashboard Output:** Classified into *Strong Match*, *Moderate Match*, or *Low Match* with highlighted missing skills and candidate feedback.

---

## ✨ Key Features

- **📄 Multi-Format Resume Parsing:** Seamless support for PDF and DOCX documents.
- **🎯 Intelligent Skill Extraction:** Detects hard skills, soft skills, tools, frameworks, and domain expertise.
- **🧠 Hybrid Matching Algorithm:** Combines TF-IDF keyword matching with Sentence-BERT semantic contextual embeddings.
- **📊 Detailed Score Breakdown:** Returns overall score alongside granular skill match percentages and missing skill gap reports.
- **💡 AI Candidate Recommendations:** Provides explicit recommendations (e.g., *Highly Recommended for Interview*, *Needs Upskilling in X*, *Unsuitable*).
- **🚀 Interactive Dashboard:** Simple Web UI built with Streamlit / FastAPI for instant resume screening and visual feedback.

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.9+
- **NLP & Machine Learning:** SpaCy, NLTK, Scikit-Learn, Hugging Face `sentence-transformers`, Transformers (BERT)
- **Document Processing:** `pdfplumber`, `PyPDF2`, `python-docx`, `pdf2image`
- **Web Framework / UI:** Streamlit / FastAPI / Flask
- **Data Manipulation & Viz:** Pandas, NumPy, Plotly, Matplotlib

---

## 📁 Project Structure

```
Folder Structure
Resume_Screening_Project/
│
├── app.py
├── requirements.txt
├── job_description.txt
│
├── templates/
│      ├── index.html
│      └── result.html
│
├── static/
│      └── style.css
│
├── uploads/
│
└── resume.pdf 
```

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
Ensure you have **Python 3.9+** and `git` installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/ai-resume-screening.git
cd ai-resume-screening
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

---

## 💻 Usage Instructions

### Running the Web Interface (Streamlit)
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to access the interactive web interface.

### Running via Python Script
```python
from src.extractor import extract_text_from_pdf
from src.matcher import calculate_match_score

# 1. Load Resume & Job Description
resume_text = extract_text_from_pdf("data/raw_resumes/sample_resume.pdf")
jd_text = open("data/job_descriptions/software_engineer.txt").read()

# 2. Compute Match
result = calculate_match_score(resume_text, jd_text)

# 3. Print Output
print(f"Overall Match Score: {result['score']}%")
print(f"Recommendation: {result['recommendation']}")
print(f"Missing Key Skills: {', '.join(result['missing_skills'])}")
```

---

## 📈 Sample Output Matrix

| Candidate Name | Target Role | Match Score | Recommendation | Top Missing Skills |
| :--- | :--- | :---: | :---: | :--- |
| Jane Doe | Data Scientist | **88%** | 🟢 Highly Recommended | PySpark, Docker |
| John Smith | Full Stack Dev | **62%** | 🟡 Moderate Fit | GraphQL, AWS |
| Alex Brown | Marketing Lead | **24%** | 🔴 Unsuitable | Python, SQL, ML |

---

## 🔮 Future Enhancements

- [ ] Support for multi-lingual resume parsing.
- [ ] Integration with Automated Applicant Tracking Systems (ATS APIs like Lever, Greenhouse).
- [ ] Automated OCR tuning for low-quality scanned image PDFs.
- [ ] LLM-powered candidate interview question generator based on resume gaps.

---
