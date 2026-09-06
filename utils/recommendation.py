# utils/recommendation.py

# Career data
CAREER_DATA = [
    {
        "career": "Software Developer",
        "skills": [
            "python",
            "java",
            "programming",
            "coding",
            "javascript",
            "html",
            "css",
            "sql",
            "git",
            "problem solving"
        ],
        "interests": [
            "software",
            "coding",
            "technology",
            "programming",
            "web development",
            "applications"
        ],
        "learning_roadmap": [
            {
                "skill": "Python Programming",
                "steps": [
                    "Learn Python basics",
                    "Practice functions and loops",
                    "Learn object-oriented programming",
                    "Build small Python projects"
                ]
            },
            {
                "skill": "Web Development",
                "steps": [
                    "Learn HTML and CSS",
                    "Learn JavaScript",
                    "Learn Flask or Django",
                    "Build a web application"
                ]
            },
            {
                "skill": "Database",
                "steps": [
                    "Learn SQL basics",
                    "Learn MySQL",
                    "Practice database queries",
                    "Connect Python with MySQL"
                ]
            }
        ]
    },

    {
        "career": "Data Scientist",
        "skills": [
            "python",
            "sql",
            "statistics",
            "machine learning",
            "data analysis",
            "pandas",
            "numpy",
            "matplotlib",
            "artificial intelligence",
            "ai"
        ],
        "interests": [
            "data",
            "analytics",
            "statistics",
            "machine learning",
            "artificial intelligence",
            "research"
        ],
        "learning_roadmap": [
            {
                "skill": "Python for Data Science",
                "steps": [
                    "Learn Python basics",
                    "Learn NumPy",
                    "Learn Pandas",
                    "Practice data analysis"
                ]
            },
            {
                "skill": "Statistics",
                "steps": [
                    "Learn descriptive statistics",
                    "Learn probability",
                    "Learn correlation and regression",
                    "Practice with datasets"
                ]
            },
            {
                "skill": "Machine Learning",
                "steps": [
                    "Learn machine learning fundamentals",
                    "Learn supervised learning",
                    "Learn unsupervised learning",
                    "Build machine learning projects"
                ]
            }
        ]
    },

    {
        "career": "Web Developer",
        "skills": [
            "html",
            "css",
            "javascript",
            "python",
            "flask",
            "django",
            "php",
            "sql",
            "web development"
        ],
        "interests": [
            "web",
            "web development",
            "websites",
            "frontend",
            "backend",
            "design"
        ],
        "learning_roadmap": [
            {
                "skill": "HTML and CSS",
                "steps": [
                    "Learn HTML structure",
                    "Learn CSS styling",
                    "Create responsive layouts",
                    "Build sample webpages"
                ]
            },
            {
                "skill": "JavaScript",
                "steps": [
                    "Learn JavaScript basics",
                    "Learn DOM manipulation",
                    "Practice events and forms",
                    "Build interactive webpages"
                ]
            },
            {
                "skill": "Backend Development",
                "steps": [
                    "Learn Python",
                    "Learn Flask",
                    "Learn SQL",
                    "Build a complete web application"
                ]
            }
        ]
    },

    {
        "career": "AI / Machine Learning Engineer",
        "skills": [
            "python",
            "machine learning",
            "artificial intelligence",
            "ai",
            "deep learning",
            "tensorflow",
            "pytorch",
            "numpy",
            "pandas",
            "mathematics"
        ],
        "interests": [
            "artificial intelligence",
            "ai",
            "machine learning",
            "deep learning",
            "technology",
            "robotics"
        ],
        "learning_roadmap": [
            {
                "skill": "Python",
                "steps": [
                    "Learn Python fundamentals",
                    "Practice data structures",
                    "Learn object-oriented programming",
                    "Build Python projects"
                ]
            },
            {
                "skill": "Machine Learning",
                "steps": [
                    "Learn machine learning concepts",
                    "Learn Scikit-learn",
                    "Practice classification and regression",
                    "Build ML projects"
                ]
            },
            {
                "skill": "Deep Learning",
                "steps": [
                    "Learn neural networks",
                    "Learn TensorFlow or PyTorch",
                    "Study computer vision and NLP",
                    "Build an AI project"
                ]
            }
        ]
    },

    {
        "career": "Cybersecurity Analyst",
        "skills": [
            "cybersecurity",
            "networking",
            "linux",
            "python",
            "security",
            "ethical hacking",
            "computer networks",
            "cryptography"
        ],
        "interests": [
            "cybersecurity",
            "security",
            "ethical hacking",
            "networks",
            "privacy",
            "technology"
        ],
        "learning_roadmap": [
            {
                "skill": "Networking",
                "steps": [
                    "Learn computer networking",
                    "Study TCP/IP",
                    "Learn common network protocols",
                    "Practice network troubleshooting"
                ]
            },
            {
                "skill": "Linux",
                "steps": [
                    "Learn Linux commands",
                    "Learn file permissions",
                    "Practice shell commands",
                    "Learn basic system administration"
                ]
            },
            {
                "skill": "Cybersecurity",
                "steps": [
                    "Learn security fundamentals",
                    "Study common vulnerabilities",
                    "Learn ethical hacking concepts",
                    "Practice in legal security labs"
                ]
            }
        ]
    },

    {
        "career": "Database Administrator",
        "skills": [
            "sql",
            "mysql",
            "database",
            "postgresql",
            "oracle",
            "database management",
            "python"
        ],
        "interests": [
            "database",
            "sql",
            "data",
            "technology",
            "database management"
        ],
        "learning_roadmap": [
            {
                "skill": "SQL",
                "steps": [
                    "Learn SELECT queries",
                    "Learn INSERT, UPDATE and DELETE",
                    "Learn JOIN operations",
                    "Practice complex SQL queries"
                ]
            },
            {
                "skill": "MySQL",
                "steps": [
                    "Learn MySQL databases",
                    "Create tables",
                    "Learn indexes",
                    "Practice database backups"
                ]
            },
            {
                "skill": "Database Administration",
                "steps": [
                    "Learn database security",
                    "Learn user permissions",
                    "Learn backup and recovery",
                    "Practice database optimization"
                ]
            }
        ]
    },

    {
        "career": "UI/UX Designer",
        "skills": [
            "design",
            "ui",
            "ux",
            "figma",
            "wireframing",
            "prototyping",
            "html",
            "css"
        ],
        "interests": [
            "design",
            "ui",
            "ux",
            "creativity",
            "web design",
            "user experience"
        ],
        "learning_roadmap": [
            {
                "skill": "UI Design",
                "steps": [
                    "Learn design principles",
                    "Learn typography and colors",
                    "Learn Figma",
                    "Create interface designs"
                ]
            },
            {
                "skill": "UX Design",
                "steps": [
                    "Learn user research",
                    "Create user personas",
                    "Learn wireframing",
                    "Create prototypes"
                ]
            },
            {
                "skill": "Portfolio",
                "steps": [
                    "Create design projects",
                    "Document your design process",
                    "Build an online portfolio",
                    "Apply for internships or jobs"
                ]
            }
        ]
    }
]


def clean_text(text):
    """
    Convert input into simple lowercase text.
    """
    if text is None:
        return ""

    return str(text).lower().strip()


def split_input(text):
    """
    Convert comma-separated user input into a list.
    """
    text = clean_text(text)

    if not text:
        return []

    parts = text.replace(";", ",").split(",")

    return [
        part.strip()
        for part in parts
        if part.strip()
    ]


def get_career_recommendations(skills, interests):
    """
    Generate career recommendations based on
    the user's skills and interests.
    """

    user_skills = split_input(skills)
    user_interests = split_input(interests)

    recommendations = []

    for career in CAREER_DATA:

        career_skills = career["skills"]
        career_interests = career["interests"]

        matched_skills = []
        matched_interests = []

        # Match skills
        for user_skill in user_skills:

            for career_skill in career_skills:

                if (
                    user_skill == career_skill
                    or user_skill in career_skill
                    or career_skill in user_skill
                ):
                    if career_skill not in matched_skills:
                        matched_skills.append(career_skill)

        # Match interests
        for user_interest in user_interests:

            for career_interest in career_interests:

                if (
                    user_interest == career_interest
                    or user_interest in career_interest
                    or career_interest in user_interest
                ):
                    if career_interest not in matched_interests:
                        matched_interests.append(career_interest)

        skill_score = len(matched_skills)
        interest_score = len(matched_interests)

        # Skills have slightly higher weight
        score = (skill_score * 10) + (interest_score * 7)

        # Keep every career available,
        # even when the score is zero.
        recommendations.append(
            {
                "career": career["career"],
                "score": score,
                "matched_skills": matched_skills,
                "matched_interests": matched_interests,
                "learning_roadmap": career["learning_roadmap"]
            }
        )

    # Highest score first
    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    # Return top 5 careers
    return recommendations[:5]


def get_recommendation_explanation(
    career,
    matched_skills=None,
    matched_interests=None
):
    """
    Generate an explanation for a career recommendation.
    """

    matched_skills = matched_skills or []
    matched_interests = matched_interests or []

    if matched_skills:
        skill_text = ", ".join(matched_skills)
        strength = (
            f"Your matching skills include {skill_text}."
        )
    else:
        strength = (
            "You currently have limited matching skills "
            "for this career."
        )

    if matched_interests:
        interest_text = ", ".join(matched_interests)
        interest_message = (
            f" Your interests match areas such as "
            f"{interest_text}."
        )
    else:
        interest_message = (
            " Your interests can be explored further "
            "to confirm this career choice."
        )

    if matched_skills:
        improvement = (
            "Focus on building projects and gaining "
            "practical experience in this field."
        )
    else:
        improvement = (
            "Start by learning the fundamental skills "
            "required for this career."
        )

    return (
        f"{career} may be a suitable career option. "
        f"{strength}"
        f"{interest_message}"
        f" {improvement}"
    )