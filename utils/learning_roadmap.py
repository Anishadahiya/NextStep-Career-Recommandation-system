# utils/learning_roadmap.py

ROADMAPS = {
    "Data Analyst": [
        {
            "skill": "SQL",
            "steps": [
                "Learn SELECT, WHERE, ORDER BY and GROUP BY",
                "Practice JOINs and subqueries",
                "Learn aggregate functions",
                "Practice SQL using real datasets"
            ]
        },
        {
            "skill": "Python",
            "steps": [
                "Learn Python fundamentals",
                "Practice lists, dictionaries and functions",
                "Learn Pandas and NumPy",
                "Work with CSV datasets"
            ]
        },
        {
            "skill": "Data Analysis",
            "steps": [
                "Learn data cleaning",
                "Practice exploratory data analysis",
                "Create charts and visualizations",
                "Build a data analysis project"
            ]
        },
        {
            "skill": "Statistics",
            "steps": [
                "Learn mean, median and standard deviation",
                "Understand probability basics",
                "Learn correlation",
                "Practice statistical analysis"
            ]
        }
    ],

    "Data Scientist": [
        {
            "skill": "Python",
            "steps": [
                "Strengthen Python fundamentals",
                "Learn NumPy and Pandas",
                "Practice data preprocessing",
                "Build data science projects"
            ]
        },
        {
            "skill": "Statistics",
            "steps": [
                "Learn descriptive statistics",
                "Learn probability",
                "Study distributions",
                "Practice statistical testing"
            ]
        },
        {
            "skill": "Machine Learning",
            "steps": [
                "Learn supervised learning",
                "Study regression and classification",
                "Learn model evaluation",
                "Build machine learning projects"
            ]
        },
        {
            "skill": "Data Visualization",
            "steps": [
                "Learn Matplotlib",
                "Learn visualization principles",
                "Create dashboards",
                "Present insights from datasets"
            ]
        }
    ],

    "AI/ML Engineer": [
        {
            "skill": "Python",
            "steps": [
                "Master Python programming",
                "Learn NumPy and Pandas",
                "Practice object-oriented programming",
                "Build Python projects"
            ]
        },
        {
            "skill": "Machine Learning",
            "steps": [
                "Learn regression and classification",
                "Study clustering",
                "Learn model evaluation",
                "Build ML projects with scikit-learn"
            ]
        },
        {
            "skill": "Artificial Intelligence",
            "steps": [
                "Learn AI fundamentals",
                "Study neural networks",
                "Explore deep learning",
                "Build an AI project"
            ]
        },
        {
            "skill": "Statistics",
            "steps": [
                "Learn probability",
                "Study distributions",
                "Learn correlation and covariance",
                "Practice statistical concepts used in ML"
            ]
        }
    ],

    "Web Developer": [
        {
            "skill": "HTML/CSS",
            "steps": [
                "Learn HTML structure",
                "Learn CSS fundamentals",
                "Practice responsive design",
                "Build responsive webpages"
            ]
        },
        {
            "skill": "JavaScript",
            "steps": [
                "Learn JavaScript fundamentals",
                "Understand DOM manipulation",
                "Work with events",
                "Build interactive webpages"
            ]
        },
        {
            "skill": "Web Development",
            "steps": [
                "Learn frontend development",
                "Learn backend fundamentals",
                "Understand APIs",
                "Build a full-stack project"
            ]
        },
        {
            "skill": "Programming",
            "steps": [
                "Practice programming logic",
                "Learn functions and data structures",
                "Practice debugging",
                "Build multiple small projects"
            ]
        }
    ],

    "Software Developer": [
        {
            "skill": "Programming",
            "steps": [
                "Strengthen programming fundamentals",
                "Learn data structures",
                "Practice algorithms",
                "Solve programming problems"
            ]
        },
        {
            "skill": "Software Development",
            "steps": [
                "Learn software development lifecycle",
                "Practice modular programming",
                "Learn Git and version control",
                "Build complete applications"
            ]
        },
        {
            "skill": "Database",
            "steps": [
                "Learn SQL fundamentals",
                "Understand database design",
                "Practice CRUD operations",
                "Connect applications to databases"
            ]
        },
        {
            "skill": "Problem Solving",
            "steps": [
                "Practice algorithmic thinking",
                "Solve coding problems",
                "Analyze time and space complexity",
                "Build problem-solving projects"
            ]
        }
    ],

    "Cybersecurity Analyst": [
        {
            "skill": "Cybersecurity",
            "steps": [
                "Learn cybersecurity fundamentals",
                "Understand common threats",
                "Study authentication and access control",
                "Practice security analysis"
            ]
        },
        {
            "skill": "Networking",
            "steps": [
                "Learn networking fundamentals",
                "Understand TCP/IP",
                "Study DNS and HTTP",
                "Practice network troubleshooting"
            ]
        },
        {
            "skill": "Security Analysis",
            "steps": [
                "Learn vulnerability concepts",
                "Study security logs",
                "Learn incident response basics",
                "Practice defensive security techniques"
            ]
        },
        {
            "skill": "Python",
            "steps": [
                "Learn Python fundamentals",
                "Practice automation scripts",
                "Work with files and APIs",
                "Build security-related utilities"
            ]
        }
    ],

    "Cloud Engineer": [
        {
            "skill": "Cloud Computing",
            "steps": [
                "Learn cloud computing fundamentals",
                "Understand compute and storage",
                "Learn networking in the cloud",
                "Deploy a simple application"
            ]
        },
        {
            "skill": "Linux",
            "steps": [
                "Learn Linux commands",
                "Understand files and permissions",
                "Practice shell commands",
                "Manage a Linux environment"
            ]
        },
        {
            "skill": "Networking",
            "steps": [
                "Learn TCP/IP",
                "Understand DNS",
                "Study routing and firewalls",
                "Practice network configuration"
            ]
        },
        {
            "skill": "Programming",
            "steps": [
                "Strengthen programming fundamentals",
                "Learn scripting",
                "Practice automation",
                "Build a cloud automation project"
            ]
        }
    ],

    "UI/UX Designer": [
        {
            "skill": "UI Design",
            "steps": [
                "Learn visual design fundamentals",
                "Study typography and spacing",
                "Learn color principles",
                "Create interface designs"
            ]
        },
        {
            "skill": "UX Design",
            "steps": [
                "Learn user research",
                "Understand user journeys",
                "Create wireframes",
                "Design user flows"
            ]
        },
        {
            "skill": "Creativity",
            "steps": [
                "Study design principles",
                "Analyze existing interfaces",
                "Create design concepts",
                "Build a design portfolio"
            ]
        },
        {
            "skill": "Communication",
            "steps": [
                "Practice presenting design decisions",
                "Learn to receive feedback",
                "Explain user-centered decisions",
                "Collaborate with developers"
            ]
        }
    ]
}


def get_learning_roadmap(career, missing_skills=None):
    """
    Return a learning roadmap for the recommended career.

    If missing_skills are available, prioritize those skills.
    """

    roadmap = ROADMAPS.get(career, [])

    if not missing_skills:
        return roadmap

    missing_names = []

    for item in missing_skills:
        if isinstance(item, dict):
            missing_names.append(item.get("skill"))
        else:
            missing_names.append(str(item))

    prioritized = []
    remaining = []

    for item in roadmap:
        if item["skill"] in missing_names:
            prioritized.append(item)
        else:
            remaining.append(item)

    return prioritized + remaining