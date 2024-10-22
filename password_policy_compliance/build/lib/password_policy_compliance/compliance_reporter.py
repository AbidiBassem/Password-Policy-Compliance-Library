from typing import List, Dict
from .password_validator import validate_password
from .policy_compliance import Policy

def generate_compliance_report(passwords: List[str], policy: Policy) -> Dict:
    """
    Generate a compliance report for a list of passwords against the given policy.
    
    Args:
    passwords (List[str]): A list of passwords to check
    policy (Policy): The policy to check against
    
    Returns:
    Dict: A report containing compliance statistics and details
    """
    total_passwords = len(passwords)
    compliant_passwords = 0
    non_compliant_passwords = 0
    error_counts = {}

    for password in passwords:
        result = validate_password(password, policy)
        if result["valid"]:
            compliant_passwords += 1
        else:
            non_compliant_passwords += 1
            for error in result["errors"]:
                error_counts[error] = error_counts.get(error, 0) + 1

    compliance_rate = (compliant_passwords / total_passwords) * 100 if total_passwords > 0 else 0

    report = {
        "total_passwords": total_passwords,
        "compliant_passwords": compliant_passwords,
        "non_compliant_passwords": non_compliant_passwords,
        "compliance_rate": compliance_rate,
        "error_counts": error_counts,
        "policy": policy.__dict__
    }

    return report

def audit_password_compliance(passwords: List[str], policy: Policy) -> List[Dict]:
    """
    Audit a list of passwords for compliance with the given policy.
    
    Args:
    passwords (List[str]): A list of passwords to audit
    policy (Policy): The policy to audit against
    
    Returns:
    List[Dict]: A list of audit results for each password
    """
    audit_results = []

    for password in passwords:
        result = validate_password(password, policy)
        audit_results.append({
            "password": password,
            "compliant": result["valid"],
            "errors": result["errors"]
        })

    return audit_results
