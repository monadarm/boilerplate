import re

def anonymize_conversation(message):
    # Pattern to match names (simple example, can be extended)
    names_pattern = r'\b(Alice|Bob|Charlie|David|Eve|Frank|Grace|Hannah|Ivy|Jack|Kathy)\b'
    message = re.sub(names_pattern, '[NAME]', message, flags=re.IGNORECASE)

    # Pattern to match email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    message = re.sub(email_pattern, '[EMAIL]', message)

    # Pattern to match phone numbers (various formats)
    phone_pattern1 = r'\b\d{10}\b'  # Simple 10 digit number
    phone_pattern2 = r'\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b'  # Format: 123-456-7890 or similar
    phone_pattern3 = r'\(\d{3}\)\s*\d{3}[-.\s]??\d{4}\b'  # Format: (123) 456-7890 or similar
    message = re.sub(phone_pattern1, '[PHONE]', message)
    message = re.sub(phone_pattern2, '[PHONE]', message)
    message = re.sub(phone_pattern3, '[PHONE]', message)

    # Pattern to match credit card numbers (simple example, can be extended)
    cc_pattern = r'\b(?:\d[ -]*?){13,16}\b'
    message = re.sub(cc_pattern, '[CREDIT_CARD]', message)

    # Pattern to match social security numbers (SSNs)
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    message = re.sub(ssn_pattern, '[SSN]', message)

    return message

# Example usage
input_message = """
Alice's email is alice@example.com and her phone number is (123) 456-7890.
Bob's phone number is 987-654-3210 and his credit card number is 1234 5678 9876 5432.
Charlie's SSN is 123-45-6789.
"""

anonymized_message = anonymize_conversation(input_message)
print(anonymized_message)
