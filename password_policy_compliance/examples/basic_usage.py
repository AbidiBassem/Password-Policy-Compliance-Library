from password_policy_compliance import password_validator, policy_compliance, compliance_reporter

def main():
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

if __name__ == "__main__":
    main()
