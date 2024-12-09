import webbrowser
import random

def open_random(websites):
    random_num = random.randint(0, len(websites) - 1)
    web_name = websites[random_num]
    webbrowser.open(f'http://{web_name}.com')

websites = ["google", "facebook", "youtube", "amazon", "twitter", "wikipedia", "instagram", "linkedin", "reddit", "netflix"]

open_random(websites)
