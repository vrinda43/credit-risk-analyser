from config.settings import SCORING_WEIGHTS, THRESHOLD_LOW_RISK, THRESHOLD_HIGH_RISK
from src.preprocessor import calculate_financial_ratios

def compute_risk_score(applicant_data):
    """
    Computes a risk score (0 to 100) using weighted financial metrics.
    """
    income = applicant_data['income']
    debt = applicant_data['monthly_debt']
    score = applicant_data['credit_score']
    delinquencies = applicant_data['delinquencies']
    limit = applicant_data['credit_limit']
    balance = applicant_data['current_balance']
    
    dti, utilization = calculate_financial_ratios(income, debt, limit, balance)
    
    # 1. DTI Factor
    dti_factor = min(dti * 2, 100)
    
    # 2. Credit Score Factor (Normalized: 850 = 0 risk, 300 = 100 risk)
    credit_factor = max(0, (850 - score) / 5.5)
    
    # 3. Delinquency Factor
    delinquency_factor = min(delinquencies * 25, 100)
    
    # 4. Credit Utilization Factor
    util_factor = min(utilization, 100)
    
    # Calculate weighted total
    final_risk_score = (
        (dti_factor *SCORING_WEIGHTS['dti_ratio']) +
        (credit_factor * SCORING_WEIGHTS['credit_score']) +
        (delinquency_factor * SCORING_WEIGHTS['delinquencies']) +
        (util_factor *SCORING_WEIGHTS['utilization'])
    )
    
    final_risk_score = round(final_risk_score, 2)
    
    # Determine risk tier
    if final_risk_score < THRESHOLD_LOW_RISK:
        category = "Low Risk"
    elif final_risk_score < THRESHOLD_HIGH_RISK:
        category = "Moderate Risk"
    else:
        category = "High Risk"
        
    return {
        "risk_score": final_risk_score,
        "category": category,
        "dti_ratio": dti,
        "utilization_rate": utilization
    }