"""Last Text at One Percent — entry for make.fun.

Writes one line to /output/entry.txt. The line is the last text a dying phone sends at one percent battery, under 200 characters.
"""
import os

LINE = "Goodbye. Tell my charger I loved it, tell the group chat I died ignoring them, and tell my owner the alarm will not be going off tomorrow."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
