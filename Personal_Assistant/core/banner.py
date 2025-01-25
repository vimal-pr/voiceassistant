import pyfiglet

def banner(name):
    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)