import queue  # модуль очереди
import sounddevice as sd    # модуль для микрофона
import vosk    # голосвая модель
import json     # обменник данными
import words    # тригерные фразы
from sklearn.feature_extraction.text import CountVectorizer     # преобразователь текста в вектор
from sklearn.linear_model import LogisticRegression     # наша логика, проход по фразам
from skills import *    # все наши функции для работы

q = queue.Queue()  # контейнер из данных

model = vosk.Model('model_small')  # передаём модель данных
device = sd.default.device = 1, 4  # откуда берем микрофон
samplerate = int(sd.query_devices(device[1], 'input')['default_samplerate'])  # делаем запрос к микрофону


def callback(indata, frames, time, status):  # функция, которая обрабатываем запрос с микрофона
    q.put(bytes(indata))  # конвертируем в байты


def recognize(data, vectorizer, clf):   # функция обработки запроса
    trg = words.TRIGGERS.intersection(data.split())     # записываем тригерные слова
    if not trg:   # проверяем обратились ли мы к боту
        return
    if 'пока' in trg:
        speaker('Всего хорошего сэр')
        offBot()
        return
    elif 'спасибо' in trg:
        speaker('Всегда пожалуйста')
        return
    elif 'понял' in trg:
        speaker('Что-нибудь ещё?')
        return
    elif 'нет' in trg:
        speaker('Жду новых указаний')
        return
    elif 'привет' in trg:
        speaker('Рада вас видеть сэр')
        return
    elif 'напиши' in trg:
        msg_pr = data
        speaker('Я в процессе написания')
        if 'вопрос' == msg_pr.split()[-1]:
            send_email(" ".join(msg_pr.split()[0:-1]) + '?')
            return
        else:
            send_email(" ".join(msg_pr.split()[0:-1]) + '.')
            return
    elif 'закинь' in trg:
        msg_pr = data
        speaker('Загружаю, дайте минутку')
        main_fraz = msg_pr.partition('подписью')
        kartinka(main_fraz[2] + '.')
        return
    data.replace(list(trg)[0], '')  # удаляем название бота из тригера
    text_vector = vectorizer.transform([data]).toarray()[0]     # обработка запроса в вектор ответа
    answer = clf.predict([text_vector])[0]  # формируем ответ

    func_name = answer.split()[0]   # функцию, которую нужно выполнить
    answer = answer.replace(func_name, '')  # организуем наш ответ
    speaker(answer)     # проговарием его
    exec(func_name + '()')      # выполняем эту функцию


def main():     # основная функция
    vectorizer = CountVectorizer()      # инициализируем класс векторайзера
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))     # хешируем вопросы

    clf = LogisticRegression()      # инициализируем класс логики
    clf.fit(vectors, list(words.data_set.values()))     # хэшируем ответы

    del words.data_set  # удаляем из оперативки наш словарик

    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[1],  # передаём параметры
                           dtype="int16", channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)  # наш аудиопоток, который принимает микрофон и семплы
        while True:  # постоянная прослушка микрофона
            data = q.get()  # забираем данные
            if rec.AcceptWaveform(data):  # если замокли
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)    # передаём распознанные слова


if __name__ == '__main__':
    main()
