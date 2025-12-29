from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import REVOLUT_LINK, EUR_PRICE

router = Router()

@router.message(Command("pay"))
async def pay_cmd(msg: types.Message):
    text = (
        "💶 *EUR Payment — Revolut*\n\n"
        f"💰 Price: *{EUR_PRICE:.2f} EUR*\n\n"
        f"👉 Pay here:\n{REVOLUT_LINK}\n\n"
        "After payment press the button below."
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="✅ I have paid", callback_data="paid_eur")]
        ]
    )

    await msg.answer(text, reply_markup=kb, parse_mode="Markdown")
