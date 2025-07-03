import secrets
import string


def generate_password(length: int, window) -> str:
    use_lower, use_upper, use_digits, use_symbols = window.user_settings()

    chars = ''

    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one option must be selected\n")

    return ''.join(secrets.choice(chars) for _ in range(length))
