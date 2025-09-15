from django.shortcuts import render

def resume_view(request):
    cv = {
        "name": "Pin-Ray Liao",
        "title": "Backend Engineer or a prmpt engineer",
        "contact": {
            "email": "pl2999@nyu.edu",
            "phone": "(+1) 347-278-9212",
            "location": "809 marcy ave Brooklyn, NY"
        },
        "summary": (
            "I am a backend engineer who enjoys building reliable systems that people use every day.I started with quality assurance, then moved into data engineering and backend development. Along the way, I worked on financial trading systems, cloud data pipelines, and personal projects that explore AI and compliance. I believe in writing clear, maintainable code and in learning from every project."
        ),
        "skills": [
            "Python", "Java", "C#", "Django", "Spring Boot", "Vue.js",
            "Docker", "Kubernetes", "GCP", "AWS", "SQL"
        ],
        "experience": [
            {
                "company": "Cathay Securities",
                "role": "Backend Engineer",
                "time": "2024 – 2025",
                "bullets": [
                    "Designed and developed Java APIs for securities trading systems.",
                    "Implemented stock borrowing logic for international investors under Taiwan’s regulations.",
                    "Collaborated with frontend teams and QA to ensure stable, low-latency trading services."
                ]
            },
            {
                "company": "CloudMile",
                "role": "Data Engineering Intern",
                "time": "2022 – 2023",
                "bullets": [
                    "Built data pipelines to Google Cloud Storage and BigQuery for large-scale training data.",
                    "Automated Apigee configuration migration, reducing setup time by 95%.",
                    "Enabled downstream machine learning models to improve product recommendations."
                ]
            },
            {
                "company": "TPI Software",
                "role": "QA Intern",
                "time": "2021",
                "bullets": [
                    "Wrote over 100 detailed test cases for a Vue.js frontend and Java backend system.",
                    "Developed Selenium scripts to catch edge cases before release.",
                    "Learned how to view software from the perspective of real end users."
                ]
            }
        ]
    }
    return render(request, "resume/resume.html", {"cv": cv})