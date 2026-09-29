# Credit Risk & Loan Default Assessment Tool

An interactive Python application designed to analyze individual credit applicant metrics and calculate overall loan default risk exposure using custom financial scoring algorithms.

## Project Features
- **Data Entry & Validation:** Verifies applicant financial details (income, debt, credit scores, delinquencies).
- **Risk Assessment Engine:** Computes Debt-to-Income (DTI) ratio and credit utilization rate to determine a weighted risk score (0-100).
- **JSON Storage:** Preserves applicant records locally across program sessions.
- **Visual Reporting:** Displays graphical chart breakdowns for applicant risk factors using Matplotlib.

## Tech Stack
- Python 3
- Matplotlib (for visualization)
- Standard Libraries: `os`, `json`

## Installation and Execution Steps

1. Open Terminal / Command Prompt and navigate to the project directory:
   cd credit-risk-analysis

2. Install Required Library:
   pip install matplotlib

3. Run the Application:
   python app.py

## Instructions for Testing
1. Choose option 1 in the main menu to assess a new applicant.
2. Enter sample values (e.g., Name: John, Income: 5000, Debt: 1500, Credit Score: 720, Delinquencies: 0, Limit: 10000, Balance: 2000).
3. View the generated risk score and choose 'y' when prompted to render the Matplotlib graph.
4. Choose option 2 to verify that the record was stored in data/applicants.json.