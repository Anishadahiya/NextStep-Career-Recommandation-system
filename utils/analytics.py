import pandas as pd


DATASET_PATH = "datasets/careers.csv"


def get_career_analytics():

    df = pd.read_csv(DATASET_PATH)

    career_count = len(df)

    all_skills = []

    for skills in df["skills"]:

        skill_list = skills.split(",")

        for skill in skill_list:

            all_skills.append(
                skill.strip().title()
            )

    skill_frequency = {}

    for skill in all_skills:

        if skill in skill_frequency:

            skill_frequency[skill] += 1

        else:

            skill_frequency[skill] = 1

    sorted_skills = dict(
        sorted(
            skill_frequency.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    return {

        "total_careers": career_count,

        "top_skills": sorted_skills
    }