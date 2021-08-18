import random
import string


DEFAULT_TOKEN_SAMPLE = string.ascii_letters + string.digits + string.punctuation
DEFAULT_ALT_ID_SAMPLE = string.ascii_lowercase + string.digits
DEFAULT_REFERRAL_SAMPLE = string.ascii_lowercase + string.ascii_uppercase + string.digits
DEFAULT_PASSWORD_SAMPLE = string.ascii_lowercase + string.digits
DEFAULT_PIN_CODE = string.digits


def generate_random_string(length=24, sample=DEFAULT_TOKEN_SAMPLE):
    """
    Create hash (token, random password, etc), where length - line length
    """
    lst = [random.choice(sample) for _ in range(length)]
    return ''.join(lst)


def generate_alt_id(length=16, sample=DEFAULT_ALT_ID_SAMPLE):
    """Create unique alt ID key for model"""
    return generate_random_string(length=length, sample=sample)


def generate_referral_key(length=10, sample=DEFAULT_REFERRAL_SAMPLE):
    """Create random pin code"""
    return generate_random_string(length=length, sample=sample)


def generate_password(length=8, sample=DEFAULT_PASSWORD_SAMPLE):
    """Create random password"""
    return generate_random_string(length=length, sample=sample)