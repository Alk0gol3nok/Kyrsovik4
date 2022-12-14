TRIGGERS = {
    # имена для бота
    'ксюха', 'ксю', 'ксюш', 'ксюша', 'ксюшь', 'ксюшка',
    # тригерные фразы
    'а', 'подскажи', 'расскажи', 'вот', 'не знаешь', 'как думаешь', 'пока', 'у меня',
    'нет', 'напиши', 'запиши', 'привет', 'закинь', 'спасибо', 'понял',
    # для диалога
    'да', 'ну', 'слушай', 'ну слушай', 'мне', 'да конечно', 'конечно', 'называется', 'ну что', 'есть', 'да есть'
            }


data_set = {
    # погода
    'какая погода на улице': 'weather а шо такое замерз??, сейчас скажу',
    'какая погода за окном': 'weather эх, сейчас выйду и скажу',
    'что там на улице': 'weather погоди, ща гляну',
    'сколько там градусов': 'weather опять выходить на балкон и мерзнуть из-за тебя',
    # браузер
    'открой браузер': 'browser ща миленький погоди немного',
    'ютуб чекнуть': 'youtube интересно, что сегодня будет в рекомендациях',
    'проверить почту': 'gmail да уж, давно нас там не было',
    'нужен гитхаб': 'github наконец-то мы снова туда заглянем',
    'документацию питона': 'python рада, что вы снова принялись за обучение',
    # диалог
    'как у тебя дела': 'passive всё хорошо, а у тебя?',     # да
    'тоже всё хорошо': ' passive отлично, о чём поговорим?',    # ну слушай
    'давай о музыке': 'passive хорошо, какая музыка вам нравится?',  # ну мне
    'нравится хип-хоп, трэп наверное': 'passive поняла, есть любимый исполнитель?',     # да, конечно
    'сода лав': 'passive так, а есть ли любимый трек? я бы послушала',      # да, есть называется
    'голодный пёс': 'pes такс, щас заценим',    # ну что
    'что как тебе трек': 'passive неплохо неплохо, а у вас есть какой-нибудь любимый момент из другого трека?',     # да
    'можешь найти его': 'moment запускаю, рассчитывая на ваш вкус',     # что скажешь
    'понравился момент': 'passive мне понравилось, спасибо за музыкальную паузу',
    # функция поиска по айпи
    'пробить один адрес': 'get_info_ip Начинаю поиск',
    # функция открытия exe файла
    'открой програмку': 'prg начинаю запуск программы',
    # функция создания word-таблицы
    'создай мне таблицу': 'create_doc Хорошо, босс, сейчас сделаю',
    # функция создания заметки
    'создай заметку': 'zashita готово, проверяйте',
    # функция дополнения заметок
    'дополни мои заметки': 'dop сделала, сейчас покажу файл',
    # функция прочтения Word документа
    'прочти документ': 'chitka_doc Начинаю процесс чтения',
    # функция прочтения Excel файла
    'выведи мне в консоль': 'excel начинаю процесс читки',
    # функция создания Excel документа
    'создай эксель файл': 'excel_random начинаю заполнение данными',
    # функция вывода уведомления  //через?//
    'выведи какое-нибудь уведомление на экран': 'yved Погодите, создаю уведомление',
    # функция вывода времени и даты
    'подскажи время и дату': 'date секунду, начинаю анализ времени',
    # функция рандомных фраз
    'как себя чувствуешь?': 'fraza',
    # функция отправки сообщения
    'отправь сообщение мне на почту': 'passive Хорошо, что написать?',
}