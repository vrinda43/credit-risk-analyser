from src.preprocessor import validate_applicant_input
from src.risk_calculator import compute_risk_score
from src.data_loader import save_applicant_record, load_all_applicants, delete_applicant
from src.visualizer import generate_risk_breakdown_chart

def show_menu():
    print("\n" + "="*45)
    print("  FINANCIAL RISK ASSESSMENT SYSTEM (PYTHON)  ")
    print("="*45)
    print("1. Assess New Applicant Risk")
    print("2. View All Stored Applicants")
    print("3. Delete Applicant Record")
    print("4. Exit")
    print("="*45)

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            print("\n--- Enter Applicant Details ---")
            try:
                data = {
                    "name": input("Applicant Name: ").strip(),
                    "income": float(input("Monthly Income ($): ")),
                    "monthly_debt": float(input("Monthly Debt Payments ($): ")),
                    "credit_score": int(input("Credit Score (300-850): ")),
                    "delinquencies": int(input("Past 2-Year Delinquencies Count: ")),
                    "credit_limit": float(input("Total Credit Limit ($): ")),
                    "current_balance": float(input("Current Total Credit Balance ($): "))
                }
                
                is_valid, msg = validate_applicant_input(data)
                if not is_valid:
                    print(f"\n[Error]: {msg}")
                    continue
                    
                result = compute_risk_score(data)
                record = {**data, **result}
                
                save_applicant_record(record)
                
                print("\n" + "-"*35)
                print(f"ASSESSMENT RESULT FOR {data['name'].upper()}")
                print(f"Risk Score   : {result['risk_score']} / 100")
                print(f"Category     : {result['category']}")
                print(f"DTI Ratio    : {result['dti_ratio']}%")
                print(f"Util. Rate   : {result['utilization_rate']}%")
                print("-" * 35)
                
                show_chart = input("Display breakdown graph? (y/n): ").strip().lower()
                if show_chart == 'y':
                    generate_risk_breakdown_chart(result, data['name'])
                    
            except ValueError:
                print("\n[Error]: Please enter valid numerical values.")
                
        elif choice == '2':
            records = load_all_applicants()
            if not records:
                print("\nNo records found.")
            else:
                print(f"\nTotal Records: {len(records)}")
                for r in records:
                    print(f"- {r['name']} | Score: {r['risk_score']} | Category: {r['category']}")
                    
        elif choice == '3':
            name = input("Enter name to delete: ").strip()
            if delete_applicant(name):
                print(f"Successfully deleted record for {name}.")
            else:
                print("Applicant not found.")
                
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()