import re
from .policy_compliance import Policy

def validate_password(password: str, policy: Policy) -> dict:
    """
    Validate a password against the given policy.
    
    Args:
    password (str): The password to validate
    policy (Policy): The policy to validate against
    
    Returns:
    dict: A dictionary containing validation results and any error messages
    """
    results = {
        "valid": True,
        "errors": []
    }
    
    # Check length
    if len(password) < policy.min_length:
        results["valid"] = False
        results["errors"].append(f"Password must be at least {policy.min_length} characters long")
    
    # Check complexity
    if policy.require_uppercase:
        if not any(c.isupper() for c in password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one uppercase letter")
        elif password[0].isupper() and not any(c.isupper() for c in password[1:]):
            results["valid"] = False
            results["errors"].append("Password must contain at least one uppercase letter (not counting the first character)")
    
    if policy.require_lowercase:
        if not any(c.islower() for c in password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one lowercase letter")
    
    if policy.require_digits:
        if not any(c.isdigit() for c in password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one digit")
    
    if policy.require_special:
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            results["valid"] = False
            results["errors"].append("Password must contain at least one special character")
    
    return results
