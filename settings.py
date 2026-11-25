import os

from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

PRODUCTS = {
    "tshirt": ("Fudbolka", 150000),
    "hoodie": ("Xudi", 300000),
    "sweatshirt": ("Svitshot", 280000),
    "cap": ("Kepka", 15000),

}