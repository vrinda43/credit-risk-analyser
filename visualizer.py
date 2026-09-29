import matplotlib.pyplot as plt

def generate_risk_breakdown_chart(analysis_result, applicant_name):
    """
    Renders a bar chart breakdown of individual financial metrics.
    """
    metrics = ['DTI Ratio (%)', 'Credit Util (%)', 'Risk Score']
    values = [
        analysis_result['dti_ratio'],
        analysis_result['utilization_rate'],
        analysis_result['risk_score']
    ]
    
    plt.figure(figsize=(7, 4))
    
    # Choose color based on risk tier
    bar_color = '#e74c3c' if analysis_result['risk_score'] >= 65 else '#2ecc71'
    colors = ['#3498db', '#f39c12', bar_color]
    
    plt.bar(metrics, values, color=colors)
    plt.title(f"Financial Profile Analysis: {applicant_name}")
    plt.ylabel("Value Percentage")
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()