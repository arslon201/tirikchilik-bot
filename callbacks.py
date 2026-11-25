from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes

from cart import Cart
from settings import PRODUCTS
from texts import TEXTS


def get_lang(context):
    return context.user_data.get("lang", "uz")


def get_cart(context):
    if "cart" not in context.user_data:
        context.user_data["cart"] = Cart()
    return context.user_data["cart"]


def lang_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang:ru")],
        [InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data="lang:uz")],
    ])


def main_keyboard(lang):
    t = TEXTS[lang]
    return ReplyKeyboardMarkup(
        [
            [t["btn_products"], t["btn_cart"]],
            [t["btn_partner"], t["btn_info"]],
            [t["btn_lang"]],
        ],
        resize_keyboard=True,
    )


def info_keyboard(lang):
    t = TEXTS[lang]
    return ReplyKeyboardMarkup(
        [
            [t["btn_comment"]],
            [t["btn_delivery"], t["btn_contacts"]],
            [t["btn_home"]],
        ],
        resize_keyboard=True,
    )


def products_keyboard():
    rows = []
    for key, (name, price) in PRODUCTS.items():
        rows.append([InlineKeyboardButton(
            f"{name} - {price} so'm", callback_data=f"add:{key}"
        )])
    return InlineKeyboardMarkup(rows)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        TEXTS["uz"]["choose_lang"] + "\n" + TEXTS["ru"]["choose_lang"],
        reply_markup=lang_keyboard(),
    )


async def lang_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    lang = query.data.split(":")[1]
    context.user_data["lang"] = lang
    await query.answer()
    await query.message.reply_text(
        TEXTS[lang]["welcome"], reply_markup=main_keyboard(lang)
    )


async def add_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    key = query.data.split(":")[1]
    get_cart(context).add(key)
    await query.answer(TEXTS[get_lang(context)]["added"])


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context)
    t = TEXTS[lang]
    text = update.message.text

    if text == t["btn_products"]:
        await update.message.reply_text(t["products"], reply_markup=products_keyboard())
    elif text == t["btn_cart"]:
        await update.message.reply_text(get_cart(context).text(lang))
    elif text == t["btn_partner"]:
        await update.message.reply_text(t["partnership"])
    elif text == t["btn_info"]:
        await update.message.reply_text(t["info_choose"], reply_markup=info_keyboard(lang))
    elif text == t["btn_lang"]:
        await update.message.reply_text(t["choose_lang"], reply_markup=lang_keyboard())
    elif text == t["btn_comment"]:
        await update.message.reply_text(t["comment"])
    elif text == t["btn_delivery"]:
        await update.message.reply_text(t["delivery"])
    elif text == t["btn_contacts"]:
        await update.message.reply_text(t["contacts"])
    elif text == t["btn_home"]:
        await update.message.reply_text(t["home"], reply_markup=main_keyboard(lang))