import os

Secrets = '‮'

choices = """\033[1;35m[1]\033[1;97m jpg extension spoofing
\033[1;35m[2]\033[1;97m pdf extension spoofing
\033[1;35m[3]\033[1;97m txt extension spoofing
\033[1;35m[4]\033[1;97m docx extension spoofing
\033[1;35m[5]\033[1;97m mp4 extension spoofing
\033[1;35m[6]\033[1;97m gif extension spoofing
\033[1;35m[7]\033[1;97m mp3 extension spoofing
\033[1;35m[8]\033[1;97m special extension spoofing
\033[1;35m[9]\033[1;97m update the tool
\033[1;35m[0]\033[1;97m exit"""

def Baner():
    os.system("clear")
    red = '\033[91m'
    logo = """
                                                                                             
                                                                                             

█████████████████████████████████████████████████████████
████████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█
████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
████████░░▄▀░░░░░░░░░░█░░░░▄▀░░██░░▄▀░░░░█░░░░░░▄▀░░░░░░█
████████░░▄▀░░███████████░░▄▀▄▀░░▄▀▄▀░░███████░░▄▀░░█████
████████░░▄▀░░░░░░░░░░███░░░░▄▀▄▀▄▀░░░░███████░░▄▀░░█████
████████░░▄▀▄▀▄▀▄▀▄▀░░█████░░▄▀▄▀▄▀░░█████████░░▄▀░░█████
████████░░▄▀░░░░░░░░░░███░░░░▄▀▄▀▄▀░░░░███████░░▄▀░░█████
████████░░▄▀░░███████████░░▄▀▄▀░░▄▀▄▀░░███████░░▄▀░░█████
█░░░░░░█░░▄▀░░░░░░░░░░█░░░░▄▀░░██░░▄▀░░░░█████░░▄▀░░█████
█░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█████░░░░░░█████
█████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████"""
    
    name = """



────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██████░░██─██░░██████░░██─██░░██████████─
─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██─────────
─██░░██████████─██░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─
─██████████░░██─██░░██████████─██░░██──██░░██─██░░██──██░░██─██░░██████████─
─────────██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██─────────
─██████████░░██─██░░██─────────██░░██████░░██─██░░██████░░██─██░░██─────────
─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────
─██████████████─██████─────────██████████████─██████████████─██████─────────
────────────────────────────────────────────────────────────────────────────
─────────────────────────────by─\033[1;35mTheEthicalGuy\033[1;97m───────────────────────────────"""
    logo_lines = logo.split("\n")
    name_lines = name.split("\n")

    for logo_line, name_line in zip(logo_lines, name_lines):
        print(f"\033[1;97m\033[1;35m{logo_line}\033[0m\033[1;97m{name_line}")
