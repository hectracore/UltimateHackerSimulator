---

### **File 2: infinite_hacker.py**
```python
import time, sys, random

def type_text(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_ip():
    return ".".join(str(random.randint(0,255)) for _ in range(4))

def fake_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%"
    return "".join(random.choice(chars) for _ in range(random.randint(6,12)))

# Intro
type_text("⚠️ INTRUSION DETECTED ⚠️")
time.sleep(1)
type_text("Starting Infinite Hacker Simulation v2.0...")
time.sleep(1)

type_text("Connecting to target network...")
time.sleep(1)
type_text(f"Target IP: {fake_ip()}")
time.sleep(1)
type_text("Firewall bypassed ✅\n")
time.sleep(1)

type_text("Cracking passwords...")
time.sleep(1)

try:
    while True:
        ip = fake_ip()
        pwd = fake_password()
        print(f"[ACCESS GRANTED] - IP {ip} | Password: {pwd}")
        time.sleep(0.1)
except KeyboardInterrupt:
    type_text("\n⚠️ ALERT ⚠️")
    time.sleep(1)
    type_text("APRIL FOOL! 🤡")
    time.sleep(1)
    type_text("Your system is completely safe 😎")
    type_text("But your friends just got pranked HARD 😏")
