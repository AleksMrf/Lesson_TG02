import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
import random
from googletrans import Translator

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
translator = Translator()

@dp.message(Command('voice'))
async def voice(message: Message):
    voice = FSInputFile("Драка.ogg")
    await message.answer_voice(voice)

@dp.message(Command('video'))
async def video(message: Message):
    await bot.send_chat_action(message.chat.id, 'upload_video')
    video = FSInputFile('video.mp4')
    await bot.send_video(message.chat.id, video)

@dp.message(Command('audio'))
async def audio(message: Message):
    audio = FSInputFile('sound.mp3')
    await bot.send_audio(message.chat.id, audio)


@dp.message(F.photo)
async def photo(message: Message):
    list[str] = ['https://cdn.culture.ru/images/6d842799-bcb1-58c7-ac9d-8a6954f8b727', 'https://www.y-flights.com/storage/Avtorskie/gory-kavkaza-elbrus.jpeg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    list[str] = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'jmg/{message.photo[-1].file_id}.jpg')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message()
async def handle_text(message: Message):
    if message.text.lower() == 'test':
        await message.answer('Тестируем')
    else:
        # Перевод текста на английский
        translation = translator.translate(message.text, dest='en')
        await message.answer(f"Перевод: {translation.text}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())