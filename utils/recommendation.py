# utils/recommendation.py

CAREER_PROFILES = {

    "Data Analyst": {
        "skills": {
            "python_score": 7,
            "sql_score": 8,
            "web_score": 3,
            "data_score": 9,
            "ai_score": 4,
            "communication_score": 7,
            "statistics_interest": 8,
            "design_interest": 3,
            "security_interest": 2,
            "cloud_interest": 3,
            "programming_interest": 6,
            "problem_solving": 7
        },
        "matched_skills": [
            "Python",
            "SQL",
            "Data Analysis",
            "Statistics",
            "Communication"
        ],
        "interests": [
            "Statistics",
            "Data Analysis",
            "Programming"
        ]
    },

    "Data Scientist": {
        "skills": {
            "python_score": 8,
            "sql_score": 6,
            "web_score": 2,
            "data_score": 9,
            "ai_score": 8,
            "communication_score": 6,
            "statistics_interest": 9,
            "design_interest": 2,
            "security_interest": 2,
            "cloud_interest": 4,
            "programming_interest": 7,
            "problem_solving": 8
        },
        "matched_skills": [
            "Python",
            "Statistics",
            "Machine Learning",
            "Data Analysis",
            "Problem Solving"
        ],
        "interests": [
            "Statistics",
            "Data Analysis",
            "Artificial Intelligence",
            "Programming",
            "Problem Solving"
        ]
    },

    "AI/ML Engineer": {
        "skills": {
            "python_score": 9,
            "sql_score": 4,
            "web_score": 2,
            "data_score": 7,
            "ai_score": 10,
            "communication_score": 5,
            "statistics_interest": 8,
            "design_interest": 1,
            "security_interest": 2,
            "cloud_interest": 5,
            "programming_interest": 9,
            "problem_solving": 9
        },
        "matched_skills": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "Statistics",
            "Programming"
        ],
        "interests": [
            "Artificial Intelligence",
            "Statistics",
            "Programming",
            "Problem Solving"
        ]
    },

    "Web Developer": {
        "skills": {
            "python_score": 4,
            "sql_score": 4,
            "web_score": 10,
            "data_score": 3,
            "ai_score": 2,
            "communication_score": 6,
            "statistics_interest": 2,
            "design_interest": 7,
            "security_interest": 3,
            "cloud_interest": 4,
            "programming_interest": 8,
            "problem_solving": 8
        },
        "matched_skills": [
            "HTML/CSS",
            "JavaScript",
            "Web Development",
            "Programming",
            "Problem Solving"
        ],
        "interests": [
            "Web Development",
            "Design",
            "Programming",
            "Problem Solving"
        ]
    },

    "Software Developer": {
        "skills": {
            "python_score": 6,
            "sql_score": 5,
            "web_score": 5,
            "data_score": 3,
            "ai_score": 3,
            "communication_score": 6,
            "statistics_interest": 3,
            "design_interest": 3,
            "security_interest": 3,
            "cloud_interest": 4,
            "programming_interest": 10,
            "problem_solving": 10
        },
        "matched_skills": [
            "Programming",
            "Software Development",
            "Database",
            "Python",
            "Problem Solving"
        ],
        "interests": [
            "Programming",
            "Problem Solving",
            "Web Development"
        ]
    },

    "Cybersecurity Analyst": {
        "skills": {
            "python_score": 6,
            "sql_score": 3,
            "web_score": 3,
            "data_score": 3,
            "ai_score": 2,
            "communication_score": 6,
            "statistics_interest": 3,
            "design_interest": 1,
            "security_interest": 10,
            "cloud_interest": 6,
            "programming_interest": 6,
            "problem_solving": 8
        },
        "matched_skills": [
            "Cybersecurity",
            "Networking",
            "Security Analysis",
            "Python",
            "Problem Solving"
        ],
        "interests": [
            "Security",
            "Cybersecurity",
            "Programming",
            "Problem Solving",
            "Cloud Computing"
        ]
    },

    "Cloud Engineer": {
        "skills": {
            "python_score": 5,
            "sql_score": 3,
            "web_score": 3,
            "data_score": 2,
            "ai_score": 2,
            "communication_score": 6,
            "statistics_interest": 2,
            "design_interest": 1,
            "security_interest": 6,
            "cloud_interest": 10,
            "programming_interest": 8,
            "problem_solving": 8
        },
        "matched_skills": [
            "Cloud Computing",
            "Linux",
            "Networking",
            "Security",
            "Programming"
        ],
        "interests": [
            "Cloud Computing",
            "Security",
            "Programming",
            "Problem Solving"
        ]
    },

    "UI/UX Designer": {
        "skills": {
            "python_score": 1,
            "sql_score": 1,
            "web_score": 5,
            "data_score": 2,
            "ai_score": 1,
            "communication_score": 8,
            "statistics_interest": 2,
            "design_interest": 10,
            "security_interest": 1,
            "cloud_interest": 1,
            "programming_interest": 3,
            "problem_solving": 7
        },
        "matched_skills": [
            "UI Design",
            "UX Design",
            "Communication",
            "Creativity",
            "Problem Solving"
        ],
        "interests": [
            "Design",
            "Communication",
            "Problem Solving",
            "Web Development"
        ]
    }
}


def calculate_score(user_scores, career_profile):
    """
    Calculate percentage match between user scores
    and a career profile.
    """

    total_difference = 0
    maximum_difference = 0

    for skill, target_score in career_profile["skills"].items():

        user_score = user_scores.get(skill, 0)

        total_difference += abs(
            user_score - target_score
        )

        maximum_difference += 9

    if maximum_difference == 0:
        return 0

    score = 100 - (
        (total_difference / maximum_difference) * 100
    )

    return round(
        max(0, min(100, score)),
        2
    )


def get_matched_interests(
    user_scores,
    career_profile
):
    """
    Find interests that match the career.
    """

    interest_mapping = {

        "statistics_interest": "Statistics",

        "design_interest": "Design",

        "security_interest": "Security",

        "cloud_interest": "Cloud Computing",

        "programming_interest": "Programming",

        "problem_solving": "Problem Solving",

        "ai_score": "Artificial Intelligence",

        "data_score": "Data Analysis",

        "web_score": "Web Development"
    }

    matched = []

    for field, interest_name in interest_mapping.items():

        user_score = user_scores.get(
            field,
            0
        )

        if (
            user_score >= 7
            and interest_name in career_profile["interests"]
        ):
            matched.append(
                interest_name
            )

    return matched


def get_recommendations(
    user_scores,
    limit=3
):
    """
    Generate career recommendations.
    """

    recommendations = []

    for career_name, profile in CAREER_PROFILES.items():

        score = calculate_score(
            user_scores,
            profile
        )

        matched_interests = get_matched_interests(
            user_scores,
            profile
        )

        recommendations.append({

            "career": career_name,

            "score": score,

            "matched_skills": profile[
                "matched_skills"
            ],

            "matched_interests": matched_interests,

            "explanation": (
                f"Your assessment profile has a "
                f"{score}% match with the skills "
                f"and interests commonly associated "
                f"with {career_name}."
            )
        })

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations[:limit]


# =========================================================
# COMPATIBILITY FUNCTION USED BY APP.PY
# =========================================================

def get_career_recommendations(
    user_scores,
    interests_text=None
):
    """
    Compatibility wrapper used by app.py.
    """

    return get_recommendations(
        user_scores,
        limit=3
    )


def get_recommendation_explanation(
    career,
    matched_skills,
    matched_interests
):
    """
    Create a user-friendly explanation.
    """

    explanation = (
        f"{career} is recommended based on "
        "your assessment profile."
    )

    if matched_skills:

        explanation += (
            " Your matching skills include "
            + ", ".join(matched_skills)
            + "."
        )

    if matched_interests:

        explanation += (
            " Your matching interests include "
            + ", ".join(matched_interests)
            + "."
        )

    return explanation


# =========================================================
# CAREER DATA FOR OTHER PAGES
# =========================================================

CAREER_DATA = []

for career_name, profile in CAREER_PROFILES.items():

    CAREER_DATA.append({

        "career": career_name,

        "skills": profile[
            "matched_skills"
        ],

        "learning_roadmap": []

    })