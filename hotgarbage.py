# HotGarbage AI - v1.1 with License Lock
# FAFO Brand - Aeon Vanta 2025

ALLOWED_KEYS = ['HGFAFO-7TMZBMFS', 'HGFAFO-BHQPZVO8', 'HGFAFO-X3CN0KX4', 'HGFAFO-VXE57TJN', 'HGFAFO-7FA6HU9T', 'HGFAFO-MMCWY879', 'HGFAFO-2UCE06XW', 'HGFAFO-ME8S11UA', 'HGFAFO-7JP7OU7F', 'HGFAFO-J7UR004T', 'HGFAFO-IM2ZQ8NT', 'HGFAFO-ZHC8LH1Y', 'HGFAFO-YP9TFA3S', 'HGFAFO-ZJ0D0Y5A', 'HGFAFO-42OTKISW', 'HGFAFO-J6HKQT1N', 'HGFAFO-JE8981C3', 'HGFAFO-87PPZRPM', 'HGFAFO-PG8JS56O', 'HGFAFO-B98CS1VB']

def roast_and_fix(code):
    print("\n🔥 Roast:")
    if "while True" in code:
        print("This loop is infinite and useless. You trying to crash the server or what?")
        print("\n🛠️ Fix Suggestion:")
        print("Replace 'while True:' with a proper loop condition, or use a for-loop if range-based.")
    elif "==" in code and "None" in code:
        print("You're comparing to None with '=='. Python's not Java, buddy.")
        print("\n🛠️ Fix Suggestion:")
        print("Use 'is None' instead of '== None'. It's cleaner and Pythonic.")
    else:
        print("This code is generic, but probably still trash.")
        print("\n🛠️ Fix Suggestion:")
        print("Use ChatGPT to rewrite this mess, or pray for mercy.")

user_key = input("Enter your license key: ")
if user_key not in ALLOWED_KEYS:
    print("🚫 Invalid license. Access denied.")
    exit()

sample_code = input("Paste your code: ")
roast_and_fix(sample_code)
