import requests
import csv
import re

# ==================================================
# CONFIG
# ==================================================

APP_ID = "aaaa"
APP_KEY = "xxxx"
COUNTRY = "us"

CATEGORIES = [
    "accounting-finance-jobs",
    "it-jobs",
    "engineering-jobs",
    "consultancy-jobs",
    "scientific-qa-jobs",
    "graduate-jobs",
    "other-general-jobs"
]

DATA_KEYWORDS = [
    "data analyst",
    "data engineer",
    "analytics",
    "engineer",
    "business intelligence",
    "bi analyst",
    "business analyst",
    "machine learning",
    "ml engineer",
    "data science",
    "quantitative",
    "statistics",
    "knowledge engineer",
    "analyst",
    "researcher",
    "data scientist",
    "data architect",
    "ux designer",
    "ux researcher",
    "user experience researcher",
    "cloud architect",
    "systems architect",
    "product manager",
    "project manager",
    "strategist",
    "prompt engineer"
]

SKILLS = [
    "python", "sql", "r", "aws", "azure", "gcp",
    "spark", "hadoop", "etl", "airflow",
    "tableau", "power bi", "excel"
]

MAX_SKILLS = 8
RESULTS_PER_PAGE = 50

# ==================================================
# HELPER FUNCTIONS
# ==================================================

def is_data_job(title, desc):
    text = f"{title} {desc}".lower()

    if any(re.search(rf"\b{re.escape(k)}\b", text) for k in DATA_KEYWORDS):
        return True

    if any(re.search(rf"\b{re.escape(skill)}\b", desc.lower()) for skill in SKILLS):
        return True

    return False


def detect_remote(desc):
    desc = desc.lower()
    if any(k in desc for k in ["fully remote", "work from home", "wfh", "100% remote"]):
        return "remote"
    if "hybrid" in desc:
        return "hybrid"
    if "remote" in desc:
        return "remote"
    return "on-site"


def detect_employment_time(desc, contract_time):
    if contract_time:
        return contract_time
    desc = desc.lower()
    if "part-time" in desc or "part time" in desc:
        return "part-time"
    if "full-time" in desc or "full time" in desc:
        return "full-time"
    return ""


def detect_employment_type(desc, contract_type):
    if contract_type:
        return contract_type
    desc = desc.lower()
    if any(k in desc for k in ["contract", "contractor", "1099"]):
        return "contract"
    if "intern" in desc:
        return "internship"
    return "permanent"


def detect_seniority(title, desc):
    text = f"{title} {desc}".lower()
    if any(re.search(rf"\b{k}\b", text) for k in ["senior", "sr", "lead", "principal", "staff"]):
        return "senior"
    if any(re.search(rf"\b{k}\b", text) for k in ["junior", "entry level", "associate"]):
        return "junior"
    return "mid"


def extract_skills(desc):
    found = []
    for skill in SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", desc, re.IGNORECASE):
            found.append(skill)

    found = found[:MAX_SKILLS]
    return found + [""] * (MAX_SKILLS - len(found))

# ==================================================
# CSV SETUP
# ==================================================

header = [
    "category",
    "title",
    "company",
    "location",
    "salary_min",
    "salary_max",
    "salary_is_predicted",
    "posted_date",
    "remote_type",
    "employment_time",
    "employment_type",
    "seniority",
    "url"
] + [f"skill_{i}" for i in range(1, MAX_SKILLS + 1)]

with open("adzuna_data_jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for category in CATEGORIES:
        url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"

        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "category": category,
            "results_per_page": RESULTS_PER_PAGE
        }

        response = requests.get(url, params=params)
        data = response.json()

        for job in data.get("results", []):
            desc = job.get("description", "")
            title = job.get("title", "")

            if not is_data_job(title, desc):
                continue  # 🔴 ONLY DATA JOBS

            row = [
                category,
                title,
                job.get("company", {}).get("display_name", ""),
                job.get("location", {}).get("display_name", ""),
                job.get("salary_min", ""),
                job.get("salary_max", ""),
                job.get("salary_is_predicted", ""),
                job.get("created", ""),
                detect_remote(desc),
                detect_employment_time(desc, job.get("contract_time")),
                detect_employment_type(desc, job.get("contract_type")),
                detect_seniority(title, desc),
                job.get("redirect_url", "")
            ] + extract_skills(desc)

            writer.writerow(row)

print("✅ Saved: adzuna_data_jobs_updated.csv")
