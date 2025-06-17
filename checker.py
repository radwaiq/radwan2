import requests
from concurrent.futures import ThreadPoolExecutor

def is_username_available(username):
    url = f'https://t.me/{username}'
    try:
        r = requests.get(url, timeout=5)
        if "tgme_username_link" in r.text:
            return False
        elif "If you have Telegram" in r.text:
            return True
        else:
            return False
    except:
        return False

def check_user(username):
    if is_username_available(username):
        print(f"[متاح] @{username}")
        return username
    return None

def main():
    with open("usernames.txt", "r") as f:
        users = [line.strip() for line in f if line.strip()]

    print(f"بدء فحص {len(users)} يوزر...")

    available = []
    with ThreadPoolExecutor(max_workers=200) as executor:  # سرعة عالية جداً
        for result in executor.map(check_user, users):
            if result:
                available.append(result)

    print(f"\nتم العثور على {len(available)} يوزر متاح:")
    for u in available:
        print(f"@{u}")

    with open("available.txt", "w") as f:
        for u in available:
            f.write(f"{u}\n")

if __name__ == "__main__":
    main()
