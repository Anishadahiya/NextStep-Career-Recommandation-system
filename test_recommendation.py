from utils.recommendation import get_career_recommendations


skills = "python, sql, excel, pandas"

interest = "data, analytics"


results = get_career_recommendations(
    skills,
    interest
)


for result in results:

    print(
        result["career"],
        "->",
        result["score"],
        "%"
    )