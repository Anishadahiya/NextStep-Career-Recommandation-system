# ml/career_model.py

from sklearn.tree import DecisionTreeClassifier


# ==========================================
# TRAINING DATA
# ==========================================

X = [
    [9, 9, 8, 9, 5, 8],   # Data Analyst
    [8, 9, 7, 9, 9, 7],   # Data Scientist
    [9, 6, 8, 6, 10, 7],  # AI Engineer
    [9, 5, 10, 4, 6, 8],  # Web Developer
    [6, 6, 4, 5, 8, 6],   # Cybersecurity
    [5, 10, 3, 6, 4, 5],  # Database Administrator
    [3, 2, 8, 2, 2, 9]    # UI/UX Designer
]


y = [
    "Data Analyst",
    "Data Scientist",
    "AI / Machine Learning Engineer",
    "Web Developer",
    "Cybersecurity Analyst",
    "Database Administrator",
    "UI/UX Designer"
]


# ==========================================
# CREATE MODEL
# ==========================================

model = DecisionTreeClassifier(
    random_state=42
)


# ==========================================
# TRAIN MODEL
# ==========================================

model.fit(X, y)


# ==========================================
# PREDICT CAREER
# ==========================================

def predict_career(
    python_score,
    sql_score,
    web_score,
    data_score,
    ai_score,
    communication_score
):

    user_data = [[
        python_score,
        sql_score,
        web_score,
        data_score,
        ai_score,
        communication_score
    ]]

    prediction = model.predict(
        user_data
    )

    return prediction[0]


# ==========================================
# GET CONFIDENCE
# ==========================================

def get_prediction_confidence(
    python_score,
    sql_score,
    web_score,
    data_score,
    ai_score,
    communication_score
):

    user_data = [[
        python_score,
        sql_score,
        web_score,
        data_score,
        ai_score,
        communication_score
    ]]

    probabilities = model.predict_proba(
        user_data
    )[0]

    confidence = max(
        probabilities
    ) * 100

    return round(
        confidence,
        2
    )


# ==========================================
# TEST MODEL
# ==========================================

if __name__ == "__main__":

    career = predict_career(
        9,
        9,
        4,
        9,
        5,
        8
    )

    confidence = get_prediction_confidence(
        9,
        9,
        4,
        9,
        5,
        8
    )

    print(
        "Predicted Career:",
        career
    )

    print(
        "Confidence:",
        str(confidence) + "%"
    )