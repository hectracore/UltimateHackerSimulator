import time, sys, random

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_progress(task, steps=20):
    for i in range(steps):
        sys.stdout.write(f"\r{task}: [{'='*(i+1)}{' '*(steps-i-1)}] {int((i+1)/steps*100)}%")
        sys.stdout.flush()
        time.sleep(random.uniform(0.05, 0.12))
    print()

def fake_ip():
    return ".".join(str(random.randint(0,255)) for _ in range(4))

def fake_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    return "".join(random.choice(chars) for _ in range(random.randint(6,12)))

type_text("⚠️ MOBILE INTRUSION DETECTED ⚠️")
time.sleep(1)
type_text("Starting Mobile Hacker Simulation v1.0...")
time.sleep(1)

fake_progress("Connecting to network")
type_text(f"Target IP: {fake_ip()}")
fake_progress("Bypassing mobile firewall")
type_text("Firewall bypassed ✅")

type_text("\nCracking mobile passwords...")
for _ in range(8):
    type_text(f"Trying password: {fake_password()}")
    time.sleep(0.2)
type_text("Password FOUND: ******** ✅")

type_text("\nAccessing mobile files...")
files = ["Photos.zip", "Messages.txt", "Contacts.db", "SecretNotes.txt"]
for f in files:
    type_text(f"Downloading {f}...")
    time.sleep(0.5)

type_text("\nInjecting fake logs...")
for _ in range(15):
    print(f"ACCESS GRANTED - IP {fake_ip()}")
    time.sleep(0.1)

type_text("\n⚠️ SYSTEM ALERT ⚠️")
time.sleep(1)
type_text("APRIL FOOL! 🤡")
time.sleep(1)
type_text("Your mobile is completely safe 😎")
type_text("But your friends just got pranked HARD 😏")
