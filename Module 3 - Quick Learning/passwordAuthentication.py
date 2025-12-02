import getpass
import time

# Sample in-memory database (username: password)
USER_DATABASE = {
    "hanzy_coding": "999888",
    "mehran_uni": "0001"
}

# Constants
MAX_ATTEMPTS = 3
LOCKOUT_DELAY = 5  # seconds (simulate cooldown after failed attempts)


def authenticate_user(username: str, password: str) -> bool:
    """Check if the provided credentials are valid."""
    return USER_DATABASE.get(username) == password


def login():
    print("🔐 Welcome to Secure Login Portal\n")

    username = input("👤 Enter username: ").strip()

    if username not in USER_DATABASE:
        print("❌ Username not found.")
        return

    attempts = MAX_ATTEMPTS
    while attempts > 0:
        password = getpass.getpass("🔑 Enter password: ").strip()

        if authenticate_user(username, password):
            print("✅ Login verified! Welcome,", username)
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Incorrect password. {attempts} attempt(s) left.\n")
            else:
                print("🚫 Account locked due to too many failed attempts.")
                print(f"⏳ Please wait {LOCKOUT_DELAY} seconds before trying again.")
                time.sleep(LOCKOUT_DELAY)


if __name__ == "__main__":
    login()
