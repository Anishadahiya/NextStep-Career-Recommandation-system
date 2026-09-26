# ml/career_model.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier


CAREERS = [
    "Data Analyst",
    "Data Scientist",
    "AI/ML Engineer",
    "Web Developer",
    "Software Developer",
    "Cybersecurity Analyst",
    "Cloud Engineer",
    "UI/UX Designer"
]


# Career profiles used to create a small training dataset.
CAREER_PROFILES = {
    "Data Analyst": [
        7, 9, 3, 10, 5, 8,
        9, 3, 2, 4, 6, 8
    ],

    "Data Scientist": [
        9, 7, 2, 10, 10, 6,
        10, 2, 2, 5, 8, 10
    ],

    "AI/ML Engineer": [
        10, 5, 2, 9, 10, 5,
        10, 2, 3, 6, 10, 10
    ],

    "Web Developer": [
        5, 5, 10, 3, 3, 6,
        3, 9, 4, 6, 9, 8
    ],

    "Software Developer": [
        8, 6, 7, 4, 5, 6,
        5, 4, 4, 5, 10, 10
    ],

    "Cybersecurity Analyst": [
        6, 5, 3, 5, 4, 6,
        6, 2, 10, 8, 7, 9
    ],

    "Cloud Engineer": [
        7, 5, 4, 4, 4, 6,
        5, 2, 8, 10, 8, 9
    ],

    "UI/UX Designer": [
        2, 2, 7, 3, 2, 8,
        3, 10, 1, 2, 4, 7
    ]
}


def create_training_data():
    """
    Create training examples from the career profiles.
    """

    X = []
    y = []

    for career, profile in CAREER_PROFILES.items():

        # Original profile
        X.append(profile)
        y.append(career)

        # Slight variations of the profile
        for _ in range(20):

            variation = []

            for value in profile:
                change = np.random.randint(-2, 3)
                new_value = max(1, min(10, value + change))
                variation.append(new_value)

            X.append(variation)
            y.append(career)

    return np.array(X), np.array(y)


# Create training data
X_train, y_train = create_training_data()


# Create and train the model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


def predict_career(user_scores):
    """
    Predict the most suitable career using the ML model.

    user_scores must contain the 12 assessment fields.
    """

    feature_names = [
        "python_score",
        "sql_score",
        "web_score",
        "data_score",
        "ai_score",
        "communication_score",
        "statistics_interest",
        "design_interest",
        "security_interest",
        "cloud_interest",
        "programming_interest",
        "problem_solving"
    ]

    values = [
        user_scores.get(field, 0)
        for field in feature_names
    ]

    prediction = model.predict([values])[0]

    probabilities = model.predict_proba([values])[0]

    confidence = max(probabilities) * 100

    return {
        "career": prediction,
        "confidence": round(confidence, 2)
    }

def get_prediction_confidence(
    python_score,
    sql_score,
    web_score,
    data_score,
    ai_score,
    communication_score
):
    scores = [
        python_score,
        sql_score,
        web_score,
        data_score,
        ai_score,
        communication_score
    ]

    if not scores:
        return 0

    average_score = sum(scores) / len(scores)

    confidence = (average_score / 10) * 100

    return round(confidence, 2)
    