from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


but_create = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='📄Створити резюме📄')
        ]
    ],
    resize_keyboard=True
)

no_experience = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='У мене немає своїх проектів')
        ]
    ],
    resize_keyboard=True
)

end_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Так', callback_data='15'),
            InlineKeyboardButton(text='Ні', callback_data='16')
        ]
    ]
)

changes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
         InlineKeyboardButton(text="🎩Ім'я та прізвище", callback_data='name_surname'),
         InlineKeyboardButton(text='📸Фото', callback_data='image')
        ],
        [
            InlineKeyboardButton(text='☎Номер телефону', callback_data='phone'),
            InlineKeyboardButton(text='📧Email', callback_data='email')
        ],
        [
            InlineKeyboardButton(text='📚Освіта', callback_data='education'),
            InlineKeyboardButton(text='📈Soft Навички', callback_data='soft_skills' ),
        ],
        [
            InlineKeyboardButton(text='🧮Tech Навички', callback_data='tech_skills'),
            InlineKeyboardButton(text='🗂Проекти', callback_data='projects')
        ],
        [
            InlineKeyboardButton(text='🌐Мова', callback_data='lang'),
            InlineKeyboardButton(text='🗣Рівень мови', callback_data='lang_level' )
        ],
        [
            InlineKeyboardButton(text="🏳Країна", callback_data='country'),
            InlineKeyboardButton(text="🏙Місто", callback_data='city')
        ],
        [
            InlineKeyboardButton(text="💻Професія", callback_data='profession'),
            InlineKeyboardButton(text="💭Очікування", callback_data='description')
        ],
        [
            InlineKeyboardButton(text="🤝Досвід роботи", callback_data='work_experience'),
            InlineKeyboardButton(text="⏰Попередній стаж",callback_data='how_long')

        ],
        [
            InlineKeyboardButton(text="📝Обов'язки на минулій роботі", callback_data='job_description'),
        ]
    ]
)


lists = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='Продовжити складання резюме')
        ]
    ],
    resize_keyboard=True
)

confirm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Підтвердити', callback_data='confirm'),
            InlineKeyboardButton(text='Скасувати', callback_data='cancel')
        ]
    ]
)

work_pass = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='Немає досвіду роботи')
        ]
    ],
    resize_keyboard=True
)

image = ReplyKeyboardMarkup(
    keyboard=[
        [
          KeyboardButton(text='Не хочу додавати фото'),
        ]
    ],
    resize_keyboard=True
)