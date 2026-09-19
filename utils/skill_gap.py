# utils/skill_gap.py

CAREER_REQUIRED_SKILLS = {
    "Data Analyst": {
        "Python": 7,
        "SQL": 8,
        "Data Analysis": 8,
        "Statistics": 8,
        "Communication": 7
    },

    "Data Scientist": {
        "Python": 8,
        "Statistics": 9,
        "Machine Learning": 8,
        "Data Analysis": 9,
        "Problem Solving": 8
    },

    "AI/ML Engineer": {
        "Python": 9,
        "Machine Learning": 9,
        "Artificial Intelligence": 9,
        "Statistics": 8,
        "Programming": 9
    },

    "Web Developer": {
        "HTML/CSS": 8,
        "JavaScript": 8,
        "Web Development": 9,
        "Programming": 8,
        "Problem Solving": 7
    },

    "Software Developer": {
        "Programming": 9,
        "Software Development": 9,
        "Python": 7,
        "Database": 7,
        "Problem Solving": 9
    },

    "Cybersecurity Analyst": {
        "Cybersecurity": 9,
        "Networking": 8,
        "Security Analysis": 8,
        "Python": 6,
        "Problem Solving": 8
    },

    "Cloud Engineer": {
        "Cloud Computing": 9,
        "Networking": 8,
        "Linux": 8,
        "Security": 7,
        "Programming": 8
    },

    "UI/UX Designer": {
        "UI Design": 9,
        "UX Design": 9,
        "Communication": 8,
        "Creativity": 9,
        "Problem Solving": 7
    }
}


def get_user_skill_levels(user_scores):
    """
    Convert assessment scores into general skill levels.
    """

    return {
        "Python": user_scores.get("python_score", 0),
        "SQL": user_scores.get("sql_score", 0),
        "Web Development": user_scores.get("web_score", 0),
        "Data Analysis": user_scores.get("data_score", 0),
        "Artificial Intelligence": user_scores.get("ai_score", 0),
        "Communication": user_scores.get("communication_score", 0),
        "Statistics": user_scores.get("statistics_interest", 0),
        "UI Design": user_scores.get("design_interest", 0),
        "Security": user_scores.get("security_interest", 0),
        "Cloud Computing": user_scores.get("cloud_interest", 0),
        "Programming": user_scores.get("programming_interest", 0),
        "Problem Solving": user_scores.get("problem_solving", 0)
    }


def get_missing_skills(career, user_scores):
    """
    Find skills where the user's current level is below
    the expected level for the recommended career.
    """

    required_skills = CAREER_REQUIRED_SKILLS.get(career, {})
    user_skills = get_user_skill_levels(user_scores)

    missing_skills = []

    for skill, required_level in required_skills.items():

        current_level = user_skills.get(skill, 0)

        if current_level < required_level:
            missing_skills.append({
                "skill": skill,
                "current_level": current_level,
                "required_level": required_level,
                "gap": required_level - current_level
            })

    missing_skills.sort(
        key=lambda item: item["gap"],
        reverse=True
    )

    return missing_skills


def get_skill_gap_summary(career, user_scores):
    """
    Return a simple summary of the user's skill gaps.
    """

    missing_skills = get_missing_skills(
        career,
        user_scores
    )

    if not missing_skills:
        return "Your current profile covers the main skills required for this career."

    skill_names = [
        item["skill"]
        for item in missing_skills[:3]
    ]

    return (
        "Focus on improving: "
        + ", ".join(skill_names)
        + "."
    )