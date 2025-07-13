import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

from soupsieve.util import lower


def clean_title(raw_title: str) -> str:
    # Убираем всё до первой точки и пробела: "39. Позa" -> "Поза"
    return re.sub(r"^\d+\.\s*", "", raw_title).strip()


def clean_prefix(text: str, prefix: str) -> str:
    if text and text.startswith(prefix):
        return text[len(prefix):].strip()
    return text


def handle():
    html = urlopen('https://papyrus-net.livejournal.com/653159.html')
    soup = BeautifulSoup(html, 'html.parser')
    postings = soup.find_all("div", class_="aentry-post__text aentry-post__text--view")

    data = []

    for post in postings:
        poses = post.find_all("h4")
        for pose in poses:
            pose_name = clean_title(pose.get_text(strip=True))
            img_tag = pose.find_next("img")
            img_url = img_tag['src'] if img_tag else None

            strong_tags = pose.find_all_next("strong", limit=5)
            dignity = None
            tip = None
            for s in strong_tags:
                if not dignity and "Достоинство" in s.text:
                    p_text = s.find_parent("p").get_text(strip=True)
                    dignity = clean_prefix(p_text, "Достоинство:")
                if not tip and "совет" in s.text.lower():
                    p_text = s.find_parent("p").get_text(strip=True)
                    tip = clean_prefix(p_text, "Наш совет:")

            data.append({
                "name": pose_name,
                "image": img_url,
                "dignity": dignity.lower() if dignity else None,
                "tip": tip.lower() if tip else None,
            })

    with open("poses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    handle()
