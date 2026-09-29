import os

# Base directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "applicants.json")

# Business rule weights for credit risk scoring
SCORING_WEIGHTS = {
    "dti_ratio": 0.35,          # Debt-to-Income ratio weight
    "credit_score": 0.30,       # Credit score influence
    "delinquencies": 0.20,      # Missed payments history
    "utilization": 0.15          # Credit line utilization rate
}

# Score threshold levels
THRESHOLD_LOW_RISK = 35.0
THRESHOLD_HIGH_RISK = 65.0