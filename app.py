# ======================================================
# AI Resume Screening Project
# Developed using Flask + Machine Learning
# ======================================================

# Import Flask libraries
from flask import Flask, render_template, request

# Used to save uploaded files
import os

# Library to read PDF files
import PyPDF2

# Machine Learning Libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ------------------------------------------------------
# Create Flask Application
# ------------------------------------------------------

app = Flask(__name__)


# ------------------------------------------------------
# Folder where uploaded resumes will be stored
# ------------------------------------------------------

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ------------------------------------------------------
# Create Upload Folder Automatically
# ------------------------------------------------------

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ------------------------------------------------------
# Function to Read Resume PDF
# ------------------------------------------------------

def extract_text_from_pdf(pdf_path):
    """
    Reads every page from a PDF file
    and returns complete text.
    """

    text = ""

    with open(pdf_path, "rb") as pdf_file:

        reader = PyPDF2.PdfReader(pdf_file)

        # Loop through all pages

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


# ------------------------------------------------------
# Function to Read Job Description
# ------------------------------------------------------

def read_job_description():

    with open("job_description.txt", "r", encoding="utf-8") as file:

        return file.read()


# ------------------------------------------------------
# Function for Prediction
# ------------------------------------------------------

def calculate_similarity(resume_text, job_text):

    """
    Convert text into vectors using TF-IDF
    Calculate Cosine Similarity
    """

    documents = [resume_text, job_text]

    # Convert text into numerical vectors

    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(documents)

    # Calculate Similarity

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])

    # Convert into Percentage

    score = similarity[0][0] * 100

    return round(score, 2)


# ------------------------------------------------------
# Home Page
# ------------------------------------------------------

@app.route("/")

def home():

    return render_template("index.html")


# ------------------------------------------------------
# Prediction Route
# ------------------------------------------------------

@app.route("/predict", methods=["POST"])

def predict():

    # Check whether user uploaded file

    if "resume" not in request.files:

        return "No Resume Uploaded"

    file = request.files["resume"]

    if file.filename == "":

        return "Please Select Resume"

    # Save Resume

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    # Read Resume

    resume_text = extract_text_from_pdf(filepath)

    # Read Job Description

    job_text = read_job_description()

    # Calculate Match Score

    score = calculate_similarity(resume_text, job_text)

    # Recommendation Logic

    if score >= 80:

        recommendation = "Excellent Match"

    elif score >= 60:

        recommendation = "Good Match"

    elif score >= 40:

        recommendation = "Average Match"

    else:

        recommendation = "Poor Match"

    # Send Results to HTML Page

    return render_template(
        "result.html",
        score=score,
        recommendation=recommendation
    )


# ------------------------------------------------------
# Run Application
# ------------------------------------------------------

if __name__ == "__main__":

    app.run(debug=True)
