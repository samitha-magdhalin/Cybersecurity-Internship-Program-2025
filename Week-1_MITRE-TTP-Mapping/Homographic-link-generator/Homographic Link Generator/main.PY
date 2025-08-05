import os
import random
import string
from homograph_generator import generate_homograph

TEMPLATE_PATH = "templates/redirect_template.html"
LINK_FOLDER = "links"
os.makedirs(LINK_FOLDER, exist_ok=True)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_redirect_html(target_url, fake_domain, short_code):
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    filled_template = template.replace("{{redirect_url}}", target_url)
    filename = f"{fake_domain.replace('.', '_')}_{short_code}.html"
    path = os.path.join(LINK_FOLDER, filename)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(filled_template)
    
    return path

def main():
    real_url = input("Enter destination URL (e.g., https://youtube.com): ").strip()
    fake_base = input("Enter domain to mimic (e.g., bitly.in or youtube.com): ").strip()
    
    homograph = generate_homograph(fake_base)
    short_code = generate_short_code()

    print(f"[+] Homographic Base: {homograph}")
    print(f"[+] Generated short link: https://{homograph}/{short_code}")
    
    output_file = create_redirect_html(real_url, homograph, short_code)

    with open("short_links.txt", "a", encoding='utf-8') as f:
        f.write(f"https://{homograph}/{short_code} -> {real_url} ({output_file})\\n")

if __name__ == "__main__":
    main()
