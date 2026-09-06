def get_skill_gap(user_skills, required_skills):

    user_skills = [
        skill.strip().lower()
        for skill in user_skills.split(",")
        if skill.strip()
    ]

    missing_skills = []

    for skill in required_skills:

        if skill.lower() not in user_skills:
            missing_skills.append(skill)

    return missing_skills