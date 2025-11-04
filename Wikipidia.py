import os
import time
from urllib.parse import quote_plus
import wikipediaapi

# CONFIG
SAVE_DIR = "./wiki_corpus"
os.makedirs(SAVE_DIR, exist_ok=True)

wiki = wikipediaapi.Wikipedia(
    language="en",
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="my-rag-bot/1.0"
)

# Put the exact wiki page titles you want to save
titles = [
    "Deep learning",
    "Neural network",
    "Backpropagation",
    "Gradient descent"
]

SLEEP_BETWEEN = 0.8  # keep polite to the API

for title in titles:
    print(f"\n→ Processing: {title}")
    page = wiki.page(title)
    if not page.exists():
        print("   ✖ Page does not exist — skipping.")
        continue

    content = page.text or page.summary or ""
    if not content.strip():
        print("   ✖ Page returned empty text — skipping.")
        continue

    safe_name = quote_plus(title.lower().replace(" ", "_"))
    filename = f"{safe_name}.txt"
    path = os.path.join(SAVE_DIR, filename)

    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        size_kb = os.path.getsize(path) / 1024
        print(f"   ✓ Saved {filename} ({size_kb:.1f} KB)")
    except Exception as e:
        print("   ✖ Failed to save:", e)

    time.sleep(SLEEP_BETWEEN)

print(f"\nDone. Check files in: {os.path.abspath(SAVE_DIR)}")
