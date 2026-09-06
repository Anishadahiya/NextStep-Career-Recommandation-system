ROADMAP = {
    "python": [
        "Python fundamentals",
        "Functions and modules",
        "Pandas and NumPy",
        "Data analysis projects"
    ],

    "sql": [
        "SQL basics",
        "SELECT, WHERE and GROUP BY",
        "JOINs and subqueries",
        "SQL data analysis projects"
    ],

    "excel": [
        "Excel formulas",
        "Pivot tables",
        "Charts and dashboards",
        "Advanced Excel"
    ],

    "power bi": [
        "Power BI fundamentals",
        "Data cleaning with Power Query",
        "DAX basics",
        "Build a Power BI dashboard"
    ],

    "statistics": [
        "Descriptive statistics",
        "Probability",
        "Hypothesis testing",
        "Regression basics"
    ],

    "data visualization": [
        "Chart fundamentals",
        "Data storytelling",
        "Matplotlib",
        "Interactive dashboards"
    ],

    "machine learning": [
        "Machine learning fundamentals",
        "Regression",
        "Classification",
        "Build a machine learning project"
    ],

    "javascript": [
        "JavaScript fundamentals",
        "DOM manipulation",
        "APIs",
        "Build a JavaScript project"
    ],

    "html": [
        "HTML fundamentals",
        "Forms",
        "Semantic HTML",
        "Build a webpage"
    ],

    "css": [
        "CSS fundamentals",
        "Flexbox",
        "Grid",
        "Responsive design"
    ]
}


def get_learning_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        skill_name = skill.strip().lower()

        if skill_name in ROADMAP:

            roadmap.append({
                "skill": skill,
                "steps": ROADMAP[skill_name]
            })

    return roadmap