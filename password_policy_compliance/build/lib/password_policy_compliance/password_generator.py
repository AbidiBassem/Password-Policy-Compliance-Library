import secrets
import string
from .policy_compliance import Policy

def generate_password(length: int, policy: Policy) -> str:
    """
    Generate a random password that complies with the given policy.
    
    Args:
    length (int): The desired length of the password
    policy (Policy): The policy to comply with
    
    Returns:
    str: A randomly generated password that complies with the policy
    """
    if length < policy.min_length:
        raise ValueError(f"Length must be at least {policy.min_length}")

    characters = ""
    if policy.require_lowercase:
        characters += string.ascii_lowercase
    if policy.require_uppercase:
        characters += string.ascii_uppercase
    if policy.require_digits:
        characters += string.digits
    if policy.require_special:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (not policy.require_lowercase or any(c.islower() for c in password)) and \
           (not policy.require_uppercase or any(c.isupper() for c in password)) and \
           (not policy.require_digits or any(c.isdigit() for c in password)) and \
           (not policy.require_special or any(c in string.punctuation for c in password)):
            return password

def generate_passphrase(num_words: int, word_list: list, separator: str = "-") -> str:
    """
    Generate a random passphrase using the given word list.
    
    Args:
    num_words (int): The number of words to use in the passphrase
    word_list (list): A list of words to choose from
    separator (str): The separator to use between words (default: "-")
    
    Returns:
    str: A randomly generated passphrase
    """
    if num_words < 3:
        raise ValueError("Number of words must be at least 3")
    
    return separator.join(secrets.choice(word_list) for _ in range(num_words))
