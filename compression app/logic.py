# logic.py
import string
import secrets
import random

def generate_password_core(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=False):
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()-_=+[]{};:,.<>?/|\\"

    if not charset:
        raise ValueError("No character sets selected")

    return ''.join(secrets.choice(charset) for _ in range(length))


def generate_email_core(add_numbers=True):
    """
    توليد إيميل جيميل عشوائي
    """
    
    # أسماء مستخدمين عشوائية
    names = [
        "alpha", "beta", "gamma", "delta", "omega", "shadow", "phoenix",
        "thunder", "cyber", "nova", "lunar", "solar", "cosmic", "digital",
        "tech", "pro", "master", "elite", "legend", "hero", "warrior",
        "cool", "super", "mega", "ultra", "hyper", "awesome", "epic",
        "dark", "ghost", "dragon", "wolf", "eagle", "tiger", "lion"
    ]
    
    # اختيار اسم عشوائي
    username = random.choice(names)
    
    # إضافة أرقام لو محتاج
    if add_numbers:
        username += str(random.randint(100, 9999))
    
    return f"{username}@gmail.com"