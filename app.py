from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import os
import smtplib

from email.message import EmailMessage

from itsdangerous import (
    URLSafeTimedSerializer,
    SignatureExpired,
    BadSignature
)

import mysql.connector

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from config import DB_CONFIG, SECRET_KEY

from utils.recommendation import (
    get_career_recommendations,
    get_recommendation_explanation,
    CAREER_DATA
)

from utils.skill_gap import get_missing_skills

from utils.learning_roadmap import get_learning_roadmap

from utils.learning_resources import get_learning_resources

from ml.career_model import predict_career


# =========================================================
# FLASK APPLICATION
# =========================================================

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "NextStep_Career_2026_9xK7!pQ2#Lm8@Rz"
)


# =========================================================
# PASSWORD RESET HELPERS
# =========================================================

RESET_TOKEN_SALT = "nextstep-password-reset"


def generate_reset_token(email):

    serializer = URLSafeTimedSerializer(
        app.secret_key
    )

    return serializer.dumps(
        email,
        salt=RESET_TOKEN_SALT
    )


def verify_reset_token(token, max_age=1800):

    serializer = URLSafeTimedSerializer(
        app.secret_key
    )

    try:

        email = serializer.loads(
            token,
            salt=RESET_TOKEN_SALT,
            max_age=max_age
        )

        return email

    except SignatureExpired:

        return None

    except BadSignature:

        return None


def send_reset_email(
    recipient_email,
    reset_url
):

    mail_username = os.getenv(
        "MAIL_USERNAME"
    )

    mail_password = os.getenv(
        "MAIL_PASSWORD"
    )

    mail_server = os.getenv(
        "MAIL_SERVER",
        "smtp.gmail.com"
    )

    mail_port = int(
        os.getenv(
            "MAIL_PORT",
            "587"
        )
    )

    if not mail_username or not mail_password:

        raise RuntimeError(
            "Email settings are not configured. "
            "Please set MAIL_USERNAME and MAIL_PASSWORD."
        )

    message = EmailMessage()

    message["Subject"] = (
        "NextStep - Password Reset"
    )

    message["From"] = mail_username

    message["To"] = recipient_email

    message.set_content(
        f"""
Hello,

We received a request to reset your NextStep password.

Please click the link below to create a new password:

{reset_url}

This password reset link is valid for 30 minutes.

If you did not request a password reset, you can safely ignore this email.

Regards,
NextStep Team
"""
    )

    with smtplib.SMTP(
        mail_server,
        mail_port
    ) as server:

        server.starttls()

        server.login(
            mail_username,
            mail_password
        )

        server.send_message(
            message
        )


# =========================================================
# CAREER ARCADE DATA
# =========================================================

QUIZ_QUESTIONS = [

    {
        "question": "Which language is widely used for Data Science?",
        "options": [
            "Python",
            "HTML",
            "CSS",
            "Figma"
        ],
        "answer": "Python"
    },

    {
        "question": "Which language is mainly used to query relational databases?",
        "options": [
            "SQL",
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "answer": "SQL"
    },

    {
        "question": "Which tool is commonly used for machine learning in Python?",
        "options": [
            "Scikit-learn",
            "Photoshop",
            "Figma",
            "Bootstrap"
        ],
        "answer": "Scikit-learn"
    },

    {
        "question": "Which technology is used to structure web pages?",
        "options": [
            "HTML",
            "Python",
            "SQL",
            "Power BI"
        ],
        "answer": "HTML"
    },

    {
        "question": "Which career focuses heavily on protecting systems and networks?",
        "options": [
            "Cybersecurity Analyst",
            "UI/UX Designer",
            "Data Scientist",
            "Web Developer"
        ],
        "answer": "Cybersecurity Analyst"
    },

    {
        "question": "Which technology is commonly associated with UI design?",
        "options": [
            "Figma",
            "MySQL",
            "NumPy",
            "TensorFlow"
        ],
        "answer": "Figma"
    },

    {
        "question": "Which library is commonly used for tabular data analysis in Python?",
        "options": [
            "Pandas",
            "Flask",
            "Figma",
            "MySQL"
        ],
        "answer": "Pandas"
    },

    {
        "question": "Which technology is used to style web pages?",
        "options": [
            "CSS",
            "SQL",
            "Python",
            "TensorFlow"
        ],
        "answer": "CSS"
    }
]


# =========================================================
# CAREER MATCH QUESTIONS
# =========================================================

CAREER_MATCH_QUESTIONS = [

    {
        "skill": "Python",
        "career": "Data Scientist"
    },

    {
        "skill": "Figma",
        "career": "UI/UX Designer"
    },

    {
        "skill": "Linux",
        "career": "Cybersecurity Analyst"
    },

    {
        "skill": "HTML",
        "career": "Web Developer"
    },

    {
        "skill": "TensorFlow",
        "career": "AI / Machine Learning Engineer"
    },

    {
        "skill": "SQL",
        "career": "Database Administrator"
    }
]


CAREER_OPTIONS = [
    "Data Scientist",
    "UI/UX Designer",
    "Cybersecurity Analyst",
    "Web Developer",
    "AI / Machine Learning Engineer",
    "Database Administrator"
]


# =========================================================
# BADGES
# =========================================================

BADGES = [

    {
        "id": "first_game",
        "name": "First Explorer",
        "icon": "🚀",
        "description": "Complete your first game."
    },

    {
        "id": "quiz_master",
        "name": "Quiz Starter",
        "icon": "🧠",
        "description": "Score at least 70% in a quiz."
    },

    {
        "id": "career_matcher",
        "name": "Career Matcher",
        "icon": "🧩",
        "description": "Complete Career Match."
    },

    {
        "id": "speed_runner",
        "name": "Speed Runner",
        "icon": "⚡",
        "description": "Complete Career Sprint."
    },

    {
        "id": "xp_100",
        "name": "XP Hunter",
        "icon": "⭐",
        "description": "Earn 100 XP."
    },

    {
        "id": "xp_250",
        "name": "Rising Star",
        "icon": "🌟",
        "description": "Earn 250 XP."
    }
]


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_db_connection():

    return mysql.connector.connect(
        **DB_CONFIG
    )


# =========================================================
# ARCADE HELPER FUNCTIONS
# =========================================================

def initialize_game_stats():

    if "game_stats" not in session:

        session["game_stats"] = {
            "xp": 0,
            "level": 1,
            "streak": 0,
            "badges": []
        }

    return session["game_stats"]


def calculate_level(xp):

    level = (
        xp // 100
    ) + 1

    xp_in_level = (
        xp % 100
    )

    progress = xp_in_level

    return {
        "level": level,
        "xp_in_level": xp_in_level,
        "xp_needed": 100,
        "progress": progress
    }


def add_xp(amount):

    stats = initialize_game_stats()

    stats["xp"] += amount

    stats["streak"] += 1

    level_info = calculate_level(
        stats["xp"]
    )

    stats["level"] = level_info["level"]

    if (
        stats["xp"] >= 100
        and "xp_100" not in stats["badges"]
    ):

        stats["badges"].append(
            "xp_100"
        )

    if (
        stats["xp"] >= 250
        and "xp_250" not in stats["badges"]
    ):

        stats["badges"].append(
            "xp_250"
        )

    if "first_game" not in stats["badges"]:

        stats["badges"].append(
            "first_game"
        )

    session["game_stats"] = stats

    session.modified = True

    return stats


def get_game_stats():

    stats = initialize_game_stats()

    level_info = calculate_level(
        stats["xp"]
    )

    return {
        "xp": stats["xp"],
        "level": level_info["level"],
        "xp_in_level": level_info["xp_in_level"],
        "xp_needed": level_info["xp_needed"],
        "progress": level_info["progress"],
        "streak": stats["streak"],
        "badges": stats["badges"]
    }


# =========================================================
# HOME
# =========================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route("/learning-resources")
def learning_resources():

    return render_template(
        "learning_resources.html"
    )


# =========================================================
# REGISTER
# =========================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        if (
            not name
            or not email
            or not password
        ):

            flash(
                "Please fill in all fields."
            )

            return redirect(
                url_for("register")
            )

        if len(password) < 8:

            flash(
                "Password must be at least 8 characters long."
            )

            return redirect(
                url_for("register")
            )

        hashed_password = (
            generate_password_hash(
                password
            )
        )

        connection = get_db_connection()

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO users
                (
                    name,
                    email,
                    password
                )
                VALUES
                (
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    name,
                    email,
                    hashed_password
                )
            )

            connection.commit()

            flash(
                "Registration successful! Please login."
            )

            return redirect(
                url_for("login")
            )

        except mysql.connector.Error as error:

            print(
                "Registration error:",
                error
            )

            flash(
                "This email may already be registered."
            )

            return redirect(
                url_for("register")
            )

        finally:

            cursor.close()

            connection.close()

    return render_template(
        "register.html"
    )


# =========================================================
# LOGIN
# =========================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        try:

            cursor.execute(
                """
                SELECT *
                FROM users
                WHERE email = %s
                """,
                (
                    email,
                )
            )

            user = cursor.fetchone()

        finally:

            cursor.close()

            connection.close()

        if (
            user
            and check_password_hash(
                user["password"],
                password
            )
        ):

            session["user_id"] = (
                user["id"]
            )

            session["user_name"] = (
                user["name"]
            )

            initialize_game_stats()

            flash(
                "Login successful!"
            )

            return redirect(
                url_for("assessment")
            )

        flash(
            "Invalid email or password."
        )

    return render_template(
        "login.html"
    )


# =========================================================
# FORGOT PASSWORD
# =========================================================

@app.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        if not email:

            flash(
                "Please enter your email address."
            )

            return redirect(
                url_for("forgot_password")
            )

        connection = get_db_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        try:

            cursor.execute(
                """
                SELECT id, email
                FROM users
                WHERE email = %s
                """,
                (
                    email,
                )
            )

            user = cursor.fetchone()

        finally:

            cursor.close()

            connection.close()

        if user:

            token = generate_reset_token(
                user["email"]
            )

            reset_url = url_for(
                "reset_password",
                token=token,
                _external=True
            )

            try:

                send_reset_email(
                    user["email"],
                    reset_url
                )

                print(
                    "Password reset email sent to:",
                    user["email"]
                )

            except Exception as error:

                print(
                    "Password reset email error:",
                    error
                )

                flash(
                    "Unable to send the reset email. "
                    "Please check the email configuration."
                )

                return redirect(
                    url_for("forgot_password")
                )

        flash(
            "If this email is registered, "
            "a password reset link has been sent."
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "forgot_password.html"
    )


# =========================================================
# RESET PASSWORD
# =========================================================

@app.route(
    "/reset-password/<token>",
    methods=["GET", "POST"]
)
def reset_password(token):

    email = verify_reset_token(
        token,
        max_age=1800
    )

    if not email:

        flash(
            "This password reset link is invalid or has expired."
        )

        return redirect(
            url_for("forgot_password")
        )

    if request.method == "POST":

        password = request.form.get(
            "password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )

        if len(password) < 8:

            flash(
                "Password must be at least 8 characters long."
            )

            return redirect(
                url_for(
                    "reset_password",
                    token=token
                )
            )

        if password != confirm_password:

            flash(
                "Passwords do not match."
            )

            return redirect(
                url_for(
                    "reset_password",
                    token=token
                )
            )

        hashed_password = (
            generate_password_hash(
                password
            )
        )

        connection = get_db_connection()

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                UPDATE users
                SET password = %s
                WHERE email = %s
                """,
                (
                    hashed_password,
                    email
                )
            )

            connection.commit()

            flash(
                "Password reset successfully! "
                "You can now login with your new password."
            )

            return redirect(
                url_for("login")
            )

        except mysql.connector.Error as error:

            connection.rollback()

            print(
                "Password reset database error:",
                error
            )

            flash(
                "Unable to reset password. Please try again."
            )

            return redirect(
                url_for(
                    "reset_password",
                    token=token
                )
            )

        finally:

            cursor.close()

            connection.close()

    return render_template(
        "reset_password.html"
    )


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("home")
    )


# =========================================================
# CAREER ASSESSMENT
# =========================================================

@app.route(
    "/assessment",
    methods=["GET", "POST"]
)
def assessment():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    recommendations = None

    if request.method == "GET":

        return render_template(
            "assessment.html",
            recommendations=None
        )

    try:

        python_score = int(
            request.form.get(
                "python_score",
                0
            )
        )

        sql_score = int(
            request.form.get(
                "sql_score",
                0
            )
        )

        web_score = int(
            request.form.get(
                "web_score",
                0
            )
        )

        data_score = int(
            request.form.get(
                "data_score",
                0
            )
        )

        ai_score = int(
            request.form.get(
                "ai_score",
                0
            )
        )

        communication_score = int(
            request.form.get(
                "communication_score",
                0
            )
        )

        statistics_score = int(
            request.form.get(
                "statistics_interest",
                0
            )
        )

        design_score = int(
            request.form.get(
                "design_interest",
                0
            )
        )

        security_score = int(
            request.form.get(
                "security_interest",
                0
            )
        )

        cloud_score = int(
            request.form.get(
                "cloud_interest",
                0
            )
        )

        programming_score = int(
            request.form.get(
                "programming_interest",
                0
            )
        )

        problem_solving_score = int(
            request.form.get(
                "problem_solving",
                0
            )
        )

    except (
        TypeError,
        ValueError
    ):

        flash(
            "Please enter valid scores from 1 to 10."
        )

        return redirect(
            url_for("assessment")
        )

    all_scores = [
        python_score,
        sql_score,
        web_score,
        data_score,
        ai_score,
        communication_score,
        statistics_score,
        design_score,
        security_score,
        cloud_score,
        programming_score,
        problem_solving_score
    ]

    valid_scores = list(
        range(1, 11)
    )

    for score in all_scores:

        if score not in valid_scores:

            flash(
                "Please answer all assessment questions."
            )

            return redirect(
                url_for("assessment")
            )

    # =====================================================
    # BUILD USER SKILLS
    # =====================================================

    user_skills = []

    if python_score >= 6:

        user_skills.append(
            "python"
        )

    if sql_score >= 6:

        user_skills.append(
            "sql"
        )

    if web_score >= 6:

        user_skills.extend(
            [
                "html",
                "css",
                "web development"
            ]
        )

    if data_score >= 6:

        user_skills.extend(
            [
                "data analysis",
                "data",
                "analytics"
            ]
        )

    if ai_score >= 6:

        user_skills.extend(
            [
                "ai",
                "artificial intelligence",
                "machine learning"
            ]
        )

    if statistics_score >= 6:

        user_skills.append(
            "statistics"
        )

    if security_score >= 6:

        user_skills.extend(
            [
                "security",
                "cybersecurity"
            ]
        )

    if cloud_score >= 6:

        user_skills.append(
            "cloud"
        )

    if programming_score >= 6:

        user_skills.append(
            "programming"
        )

    if design_score >= 6:

        user_skills.extend(
            [
                "design",
                "ui",
                "ux"
            ]
        )

    if problem_solving_score >= 6:

        user_skills.append(
            "problem solving"
        )

    user_skills = list(
        dict.fromkeys(
            user_skills
        )
    )

    skills_text = ",".join(
        user_skills
    )

    # =====================================================
    # BUILD USER INTERESTS
    # =====================================================

    user_interests = []

    if data_score >= 6:

        user_interests.extend(
            [
                "data",
                "analytics"
            ]
        )

    if ai_score >= 6:

        user_interests.extend(
            [
                "ai",
                "artificial intelligence",
                "machine learning"
            ]
        )

    if web_score >= 6:

        user_interests.extend(
            [
                "web",
                "web development"
            ]
        )

    if design_score >= 6:

        user_interests.extend(
            [
                "design",
                "ui",
                "ux"
            ]
        )

    if security_score >= 6:

        user_interests.extend(
            [
                "security",
                "cybersecurity"
            ]
        )

    if cloud_score >= 6:

        user_interests.extend(
            [
                "cloud",
                "technology"
            ]
        )

    if programming_score >= 6:

        user_interests.extend(
            [
                "programming",
                "coding"
            ]
        )

    if statistics_score >= 6:

        user_interests.append(
            "statistics"
        )

    user_interests = list(
        dict.fromkeys(
            user_interests
        )
    )

    interests_text = ",".join(
        user_interests
    )

    # =====================================================
    # BUILD USER SCORE DICTIONARY
    # =====================================================

    user_scores = {
        "python_score": python_score,
        "sql_score": sql_score,
        "web_score": web_score,
        "data_score": data_score,
        "ai_score": ai_score,
        "communication_score": communication_score,
        "statistics_interest": statistics_score,
        "design_interest": design_score,
        "security_interest": security_score,
        "cloud_interest": cloud_score,
        "programming_interest": programming_score,
        "problem_solving": problem_solving_score
    }

    # =====================================================
    # CAREER RECOMMENDATION
    # =====================================================

    recommendations = get_career_recommendations(
        user_scores,
        interests_text
    )

    # =====================================================
    # ML PREDICTION
    # =====================================================

    ml_prediction = predict_career(
        user_scores
    )

    ml_career = ml_prediction["career"]

    ml_confidence = ml_prediction["confidence"]

    # =====================================================
    # PROCESS RECOMMENDATION
    # =====================================================

    if recommendations:

        top_recommendation = recommendations[0]

        top_career = top_recommendation["career"]

        career_info = None

        for career in CAREER_DATA:

            if (
                career["career"].lower()
                == top_career.lower()
            ):

                career_info = career

                break

        required_skills = []

        if career_info:

            required_skills = career_info["skills"]

        matched_skills = top_recommendation.get(
            "matched_skills",
            []
        )

        # -------------------------------------------------
        # SKILL GAP
        # -------------------------------------------------

        missing_skills = get_missing_skills(
            top_career,
            user_scores
        )

        # -------------------------------------------------
        # EXPLANATION
        # -------------------------------------------------

        explanation = get_recommendation_explanation(
            top_career,
            matched_skills,
            top_recommendation.get(
                "matched_interests",
                []
            )
        )

        # -------------------------------------------------
        # LEARNING ROADMAP
        # -------------------------------------------------

        learning_roadmap = get_learning_roadmap(
            top_career,
            missing_skills
        )

        # -------------------------------------------------
        # LEARNING RESOURCES
        # -------------------------------------------------

        learning_resources = get_learning_resources(
            top_career,
            missing_skills
        )

        # -------------------------------------------------
        # ADD RESULTS TO RECOMMENDATION
        # -------------------------------------------------

        recommendations[0]["missing_skills"] = (
            missing_skills
        )

        recommendations[0]["explanation"] = (
            explanation
        )

        recommendations[0]["learning_roadmap"] = (
            learning_roadmap
        )

        recommendations[0]["learning_resources"] = (
            learning_resources
        )

        recommendations[0]["ml_career"] = (
            ml_career
        )

        recommendations[0]["ml_confidence"] = (
            ml_confidence
        )

        # =================================================
        # SAVE ASSESSMENT TO MYSQL
        # =================================================

        connection = get_db_connection()

        cursor = connection.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO assessments
                (
                    user_id,
                    python_score,
                    sql_score,
                    web_score,
                    data_score,
                    ai_score,
                    communication_score,
                    recommended_career
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    session["user_id"],
                    python_score,
                    sql_score,
                    web_score,
                    data_score,
                    ai_score,
                    communication_score,
                    top_career
                )
            )

            connection.commit()

        except mysql.connector.Error as error:

            connection.rollback()

            print(
                "Assessment database error:",
                error
            )

            flash(
                "Assessment generated, but could not be saved."
            )

        finally:

            cursor.close()

            connection.close()

    else:

        flash(
            "No career recommendation could be generated."
        )

    return render_template(
        "assessment.html",
        recommendations=recommendations
    )


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    connection = get_db_connection()

    cursor = connection.cursor(
        dictionary=True
    )

    try:

        cursor.execute(
            """
            SELECT *
            FROM assessments
            WHERE user_id = %s
            ORDER BY created_at DESC
            """,
            (
                session["user_id"],
            )
        )

        assessments = cursor.fetchall()

    finally:

        cursor.close()

        connection.close()

    return render_template(
        "dashboard.html",
        assessments=assessments
    )


# =========================================================
# CAREER DETAILS
# =========================================================

@app.route(
    "/career-details/<path:career_name>"
)
def career_details(
    career_name
):

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    recommendation = None

    for career in CAREER_DATA:

        if (
            career["career"].lower()
            == career_name.lower()
        ):

            recommendation = {
                "career": career["career"],
                "matched_skills": career["skills"],
                "learning_roadmap": career["learning_roadmap"],
                "explanation": (
                    f"{career['career']} is associated "
                    "with the skills and interests "
                    "shown on this page."
                )
            }

            break

    return render_template(
        "career_details.html",
        recommendation=recommendation
    )


# =========================================================
# CAREER ARCADE
# =========================================================

@app.route("/arcade")
def arcade():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    game_stats = get_game_stats()

    return render_template(
        "arcade.html",
        game_stats=game_stats,
        all_badges=BADGES
    )


# =========================================================
# SKILL QUIZ
# =========================================================

@app.route(
    "/arcade/skill-quiz",
    methods=["GET", "POST"]
)
def skill_quiz():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "GET":

        return render_template(
            "skill_quiz.html",
            questions=QUIZ_QUESTIONS
        )

    score = 0

    for index, question in enumerate(
        QUIZ_QUESTIONS
    ):

        user_answer = request.form.get(
            f"question_{index}",
            ""
        ).strip().lower()

        correct_answer = (
            question["answer"]
            .strip()
            .lower()
        )

        if user_answer == correct_answer:

            score += 1

    total = len(
        QUIZ_QUESTIONS
    )

    percentage = round(
        (score / total) * 100
    )

    earned_xp = score * 10

    if percentage >= 80:

        earned_xp += 30

    elif percentage >= 60:

        earned_xp += 15

    add_xp(
        earned_xp
    )

    stats = initialize_game_stats()

    if (
        percentage >= 70
        and "quiz_master"
        not in stats["badges"]
    ):

        stats["badges"].append(
            "quiz_master"
        )

    session["game_stats"] = stats

    return render_template(
        "quiz_result.html",
        score=score,
        total=total,
        percentage=percentage,
        earned_xp=earned_xp
    )


# =========================================================
# CAREER SPRINT
# =========================================================

@app.route(
    "/arcade/career-sprint"
)
def career_sprint():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    questions = QUIZ_QUESTIONS[:5]

    return render_template(
        "career_sprint.html",
        questions=questions
    )


@app.route(
    "/arcade/career-sprint/result",
    methods=["POST"]
)
def career_sprint_result():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    score = 0

    questions = QUIZ_QUESTIONS[:5]

    for index, question in enumerate(
        questions
    ):

        answer = request.form.get(
            f"question_{index}",
            ""
        ).strip().lower()

        correct_answer = (
            question["answer"]
            .strip()
            .lower()
        )

        if answer == correct_answer:

            score += 1

    total = len(
        questions
    )

    percentage = round(
        (score / total) * 100
    )

    earned_xp = score * 15

    add_xp(
        earned_xp
    )

    stats = initialize_game_stats()

    if (
        "speed_runner"
        not in stats["badges"]
    ):

        stats["badges"].append(
            "speed_runner"
        )

    session["game_stats"] = stats

    return render_template(
        "sprint_result.html",
        score=score,
        total=total,
        percentage=percentage,
        earned_xp=earned_xp
    )


# =========================================================
# CAREER MATCH
# =========================================================

@app.route(
    "/arcade/career-match",
    methods=["GET", "POST"]
)
def career_match():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    if request.method == "GET":

        return render_template(
            "career_match.html",
            questions=CAREER_MATCH_QUESTIONS
        )

    score = 0

    total = len(
        CAREER_MATCH_QUESTIONS
    )

    for index, item in enumerate(
        CAREER_MATCH_QUESTIONS
    ):

        answer = request.form.get(
            f"match_{index}",
            ""
        )

        if answer == item["career"]:

            score += 1

    percentage = round(
        (score / total) * 100
    )

    earned_xp = score * 15

    add_xp(
        earned_xp
    )

    stats = initialize_game_stats()

    if (
        "career_matcher"
        not in stats["badges"]
    ):

        stats["badges"].append(
            "career_matcher"
        )

    session["game_stats"] = stats

    return render_template(
        "match_result.html",
        score=score,
        total=total,
        percentage=percentage,
        earned_xp=earned_xp
    )


# =========================================================
# APPLICATION START
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )