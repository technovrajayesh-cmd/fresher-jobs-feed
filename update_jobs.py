import json
import time
from datetime import datetime, timezone

def generate_jobs_feed():
    now_ms = int(time.time() * 1000)
    
    # You can expand this list or connect it to web scrapers / external job APIs
    jobs = [
        {
            "id": f"auto_google_{now_ms}",
            "role": "Software Engineer - I (Graduate)",
            "company": "Google",
            "location": "Bengaluru / Hyderabad, India",
            "workMode": "Hybrid",
            "ctc": "22 - 28 LPA",
            "batch": "2025 / 2026 Batch",
            "skills": ["Java", "C++", "Python", "Data Structures"],
            "eligibility": "B.E./B.Tech/M.Tech in CSE, IT, ECE | 0–1 Years Experience",
            "summary": "Design, develop, and test scalable distributed systems and core cloud infrastructure at Google scale.",
            "publishedMillis": now_ms - 3600_000,
            "applyUrl": "https://www.google.com/about/careers/applications/"
        },
        {
            "id": f"auto_microsoft_{now_ms}",
            "role": "Associate Software Engineer",
            "company": "Microsoft",
            "location": "Noida / Hyderabad, India",
            "workMode": "Hybrid",
            "ctc": "20 - 25 LPA",
            "batch": "2026 Batch",
            "skills": ["C#", ".NET", "Azure", "SQL"],
            "eligibility": "B.E./B.Tech/MCA (2026 Passing Out Batch)",
            "summary": "Build next-generation cloud services and intelligent developer platforms on Microsoft Azure.",
            "publishedMillis": now_ms - 7200_000,
            "applyUrl": "https://careers.microsoft.com/"
        },
        {
            "id": f"auto_amazon_{now_ms}",
            "role": "Software Engineer - I",
            "company": "Amazon",
            "location": "Bengaluru / Chennai, India",
            "workMode": "Hybrid",
            "ctc": "19 - 24 LPA",
            "batch": "2025 / 2026 Batch",
            "skills": ["Python", "Machine Learning", "AWS", "SQL"],
            "eligibility": "B.E./B.Tech in CS/IT/Data Science",
            "summary": "Work with AWS and Alexa AI teams to build high-performance machine learning models and cloud microservices.",
            "publishedMillis": now_ms - 10800_000,
            "applyUrl": "https://www.amazon.jobs/"
        }
    ]

    feed = {
        "generatedAtUtc": datetime.now(timezone.utc).isoformat(),
        "generatedAtIst": datetime.now(timezone.utc).strftime("Today, %I:%M %p UTC"),
        "totalCount": len(jobs),
        "jobs": jobs
    }

    with open("data/freshers_jobs.json", "w") as f:
        json.dump(feed, f, indent=2)

if __name__ == "__main__":
    generate_jobs_feed()
