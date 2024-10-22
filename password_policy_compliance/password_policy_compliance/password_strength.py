import math
import re

def calculate_entropy(password: str) -> float:
    """
    Calculate the entropy of a password.
    
    Entropy is a measure of password strength based on the amount of information
    (in bits) contained in the password.
    
    Args:
        password (str): The password to evaluate.
    
    Returns:
        float: The calculated entropy of the password.
    """
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += 32
    
    if charset_size == 0:
        return 0.0
    
    entropy = len(password) * math.log2(charset_size)
    return round(entropy, 3)

def score_password(password: str) -> dict:
    """
    Calculate a password strength score based on various factors.
    
    This function evaluates a password's strength considering length,
    character variety, and common patterns. It returns a score and
    a breakdown of the factors contributing to that score.
    
    Args:
        password (str): The password to evaluate.
    
    Returns:
        dict: A dictionary containing the password score and factor breakdown.
    """
    score = 0
    factors = {
        "length": 0,
        "uppercase": 0,
        "lowercase": 0,
        "digits": 0,
        "special": 0,
        "patterns": 0
    }
    
    # Length
    length = len(password)
    factors["length"] = min(length * 4, 32)
    score += factors["length"]
    
    # Character variety
    if re.search(r'[A-Z]', password):
        factors["uppercase"] = 10
    if re.search(r'[a-z]', password):
        factors["lowercase"] = 10
    if re.search(r'\d', password):
        factors["digits"] = 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        factors["special"] = 10
    
    score += factors["uppercase"] + factors["lowercase"] + factors["digits"] + factors["special"]
    
    # Patterns
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        factors["patterns"] -= 10
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):  # Sequential letters
        factors["patterns"] -= 10
    if re.search(r'(012|123|234|345|456|567|678|789|987|876|765|654|543|432|321|210)', password):  # Sequential numbers
        factors["patterns"] -= 10
    
    score += factors["patterns"]
    
    # Entropy bonus
    entropy = calculate_entropy(password)
    entropy_bonus = min(int(entropy), 20)
    score += entropy_bonus
    
    # Ensure score is between 0 and 100
    score = max(0, min(score, 100))
    
    return {
        "score": score,
        "entropy": entropy,
        **factors
    }
