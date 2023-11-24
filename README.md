Hello, this readme will have written on Russian, but if you wanna - you can translate it
# Программа саммаризатор

## Зависимости

- docker (https://docs.docker.com/desktop/install/windows-install/)
- установка `python 3.11`

## Настройка

- переходим в settings и заполняем все поля если нужно по сценарию, в пративном случае можете написать мне в тг (указан ссылкой в профиле)
- `docker load < telegramdigest.tar`
- переходим в корневую директорию и заполняем channels и settings
- собираем докер image `docker build -t td .`

## Запуск для пользователя

- запускаем image `docker run -i td`


## Запуск и устоновка для разработки

- переходим в venv
- или устанавливаем все зависимости `pip install -r requirements.txt`
- запускаем `python main.py`