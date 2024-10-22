# Password Policy Compliance Library

A Python library that helps enforce password policies, ensuring password compliance with best practices and industry standards.

## Features

- Password validation against customizable security policies
- Policy compliance checking
- Compliance reporting and auditing

## Installation

To install the Password Policy Compliance Library, run:

```
pip install password-policy-compliance
```

## Usage

Here's a quick example of how to use the library:

```python
from password_policy_compliance import password_validator, policy_compliance, compliance_reporter

# Create a policy
policy = policy_compliance.Policy(
    name="Custom Policy",
    min_length=8,
    require_uppercase=True,
    require_lowercase=True,
    require_digits=True,
    require_special=True
)

# Validate a password
password = "MyP@ssw0rd"
result = password_validator.validate_password(password, policy)

if result["valid"]:
    print(f"Password '{password}' is valid!")
else:
    print(f"Password '{password}' is invalid. Errors:")
    for error in result["errors"]:
        print(f"- {error}")

# Generate a compliance report
passwords = ["StrongP@ss1", "weakpass", "NoSpecial1", "sh0rt", "AllLowercase123!"]
report = compliance_reporter.generate_compliance_report(passwords, policy)
print(f"\nCompliance report:")
print(f"Total passwords: {report['total_passwords']}")
print(f"Compliant passwords: {report['compliant_passwords']}")
print(f"Non-compliant passwords: {report['non_compliant_passwords']}")
print(f"Compliance rate: {report['compliance_rate']}%")

# Audit password compliance
print("\nPassword audit:")
audit_results = compliance_reporter.audit_password_compliance(passwords, policy)
for result in audit_results:
    print(f"Password: {result['password']}, Compliant: {result['compliant']}")
    if not result['compliant']:
        print(f"Errors: {', '.join(result['errors'])}")
```

For more detailed examples, check the `examples` directory in the repository.

## Documentation

For more detailed documentation, please refer to the docstrings in the source code. Full documentation will be available soon.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Bassem Abidi (abidi.bassem@me.com)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
