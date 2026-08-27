# ======================================================
# AI Resume Screening Project
# Developed using Flask + Skill Matching
# ======================================================

# Import Flask libraries
from flask import Flask, render_template, request

# Used to save uploaded files
import os

# Library to read PDF files
import PyPDF2


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

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


# ------------------------------------------------------
# Function to Read Job Description
# ------------------------------------------------------

def read_job_description():

    with open(
        "job_description.txt",
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# ------------------------------------------------------
# Function to Calculate Resume Match
# ------------------------------------------------------

def calculate_similarity(resume_text, job_text):

    """
    Calculate resume match based on required skills.
    """

    # Convert resume text to lowercase
    resume_text = resume_text.lower()

    # Convert job description to lowercase
    job_text = job_text.lower()


    # --------------------------------------------------
    # Required Skills
    # --------------------------------------------------

    required_skills = [

        "python",

        "flask",

        "machine learning",

        "sql",

        "git",

        "html",

        "css",

        "rest api",

        "communication skills",

        "problem solving",

        "team work"

    ]


    # --------------------------------------------------
    # Find Matching Skills
    # --------------------------------------------------

    matched_skills = []


    for skill in required_skills:

        if skill in resume_text:

            matched_skills.append(skill)


    # --------------------------------------------------
    # Calculate Score
    # --------------------------------------------------

    total_skills = len(required_skills)

    matched_count = len(matched_skills)


    score = (
        matched_count /
        total_skills
    ) * 100


    return round(score, 2), matched_skills


# ------------------------------------------------------
# Home Page
# ------------------------------------------------------

@app.route("/")

def home():

    return render_template(
        "index.html"
    )


# ------------------------------------------------------
# Prediction Route
# ------------------------------------------------------

@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    # --------------------------------------------------
    # Check Whether User Uploaded File
    # --------------------------------------------------

    if "resume" not in request.files:

        return "No Resume Uploaded"


    file = request.files["resume"]


    if file.filename == "":

        return "Please Select Resume"


    # --------------------------------------------------
    # Save Resume
    # --------------------------------------------------

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)


    # --------------------------------------------------
    # Read Resume
    # --------------------------------------------------

    resume_text = extract_text_from_pdf(
        filepath
    )


    # --------------------------------------------------
    # Read Job Description
    # --------------------------------------------------

    job_text = read_job_description()


    # --------------------------------------------------
    # Calculate Match Score
    # --------------------------------------------------

    score, matched_skills = calculate_similarity(
        resume_text,
        job_text
    )


    # --------------------------------------------------
    # Recommendation Logic
    # --------------------------------------------------

    if score >= 80:

        recommendation = "Excellent Match"

    elif score >= 60:

        recommendation = "Good Match"

    elif score >= 40:

        recommendation = "Average Match"

    else:

        recommendation = "Poor Match"


    # --------------------------------------------------
    # Send Results to HTML
    # --------------------------------------------------

    return render_template(

        "result.html",

        score=score,

        recommendation=recommendation,

        matched_skills=matched_skills

    )


# ------------------------------------------------------
# Run Application
# ------------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )