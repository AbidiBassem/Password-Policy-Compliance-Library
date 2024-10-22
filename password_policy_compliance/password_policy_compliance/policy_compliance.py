from dataclasses import dataclass

@dataclass
class Policy:
    """
    Represents a password policy with various requirements.
    
    Attributes:
        name (str): The name of the policy.
        min_length (int): The minimum required length for passwords.
        require_uppercase (bool): Whether uppercase letters are required.
        require_lowercase (bool): Whether lowercase letters are required.
        require_digits (bool): Whether digits are required.
        require_special (bool): Whether special characters are required.
    """
    name: str
    min_length: int
    require_uppercase: bool
    require_lowercase: bool
    require_digits: bool
    require_special: bool

def get_policy(policy_name: str) -> Policy:
    """
    Retrieve a predefined policy by name.
    
    This function returns a predefined Policy object based on the given policy name.
    Currently supported policies are "NIST" and "OWASP".
    
    Args:
        policy_name (str): The name of the policy to retrieve.
    
    Returns:
        Policy: The requested policy object.
    
    Raises:
        ValueError: If the policy name is not recognized.
    
    Example:
        >>> nist_policy = get_policy("NIST")
        >>> print(nist_policy)
        Policy(name='NIST', min_length=8, require_uppercase=False, require_lowercase=False, require_digits=False, require_special=False)
    """
    policies = {
        "NIST": Policy(
            name="NIST",
            min_length=8,
            require_uppercase=False,
            require_lowercase=False,
            require_digits=False,
            require_special=False
        ),
        "OWASP": Policy(
            name="OWASP",
            min_length=10,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True
        )
    }
    
    if policy_name not in policies:
        raise ValueError(f"Unknown policy: {policy_name}")
    
    return policies[policy_name]

def create_custom_policy(name: str, min_length: int, require_uppercase: bool,
                         require_lowercase: bool, require_digits: bool,
                         require_special: bool) -> Policy:
    """
    Create a custom password policy.
    
    This function allows you to create a custom Policy object with specific requirements.
    
    Args:
        name (str): The name of the custom policy.
        min_length (int): The minimum password length.
        require_uppercase (bool): Whether to require uppercase letters.
        require_lowercase (bool): Whether to require lowercase letters.
        require_digits (bool): Whether to require digits.
        require_special (bool): Whether to require special characters.
    
    Returns:
        Policy: The created custom policy object.
    
    Example:
        >>> custom_policy = create_custom_policy("Custom", 12, True, True, True, False)
        >>> print(custom_policy)
        Policy(name='Custom', min_length=12, require_uppercase=True, require_lowercase=True, require_digits=True, require_special=False)
    """
    return Policy(
        name=name,
        min_length=min_length,
        require_uppercase=require_uppercase,
        require_lowercase=require_lowercase,
        require_digits=require_digits,
        require_special=require_special
    )
