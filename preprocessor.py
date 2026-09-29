def validate_applicant_input(data):
    """
    Validates numeric inputs to prevent runtime errors.
    """
    required_fields = ['name', 'income', 'monthly_debt', 'credit_score', 'delinquencies', 'credit_limit', 'current_balance']
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
            
    if data['income'] <= 0:
        return False, "Monthly income must be greater than zero."
        
    if not (300 <= data['credit_score'] <= 850):
        return False, "Credit score must be between 300 and 850."
        
    if data['delinquencies'] < 0:
        return False, "Delinquency count cannot be negative."
        
    return True, "Valid input"


def calculate_financial_ratios(income, monthly_debt, credit_limit, current_balance):
    """
    Calculates Debt-to-Income (DTI) and Credit Utilization percentages.
    """
    dti = (monthly_debt / income) * 100
    
    if credit_limit > 0:
        utilization = (current_balance / credit_limit) * 100
    else:
        utilization = 100.0
        
    return round(dti, 2), round(utilization, 2)