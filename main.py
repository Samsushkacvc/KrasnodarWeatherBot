# -*- coding: cp1251 -*-
import requests
import aiogram
import asyncio
import logging
import sys

from os import getenv
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters.command import Command

bot = Bot(token="6913010458:AAGGgrgGHCQwUUdcppUgZHpF9XKKisSgG2w")

dp = Dispatcher()

url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D0%B5,_%D0%9A%D1%80%D0%B0%D1%81%D0%BD%D0%BE%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D0%BA%D1%80%D0%B0%D0%B9'
class_ = 't_0'

r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')
t = html.find(class_=class_).text

temperature = t

@dp.message(Command("weather"))
async def cmd_start(message: Message):
	await message.answer("погода в Краснодаре:")
	await message.answer(temperature)

async def main():
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())