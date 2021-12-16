# project_megafon

Данные для запуска модели data_test.csv (после объединения с features). Ссылка на google disk
https://drive.google.com/open?id=18nKya_b8ZVpvz_H8joHr_DJ9a9MeF89u&authuser=nick.hess.m3%40gmail.com&usp=drive_fs

# Порядок запуска модели
1) Клонировать репозиторий и скачать файл с данными с Google Disk по ссылке выше
2) Создать виртуальное окружение:
python -m venv venv
3) Активировать виртуальное окружение:
из текущей папки перейти по пути \venv\Scripts\
выполнить файл activate
4) Установить библиотеки, используя файл requirments.txt
pip install -r requirments.txt
5) Запустить скрипт run_model.py:
python run_model.py

После выполнения скрипта в директории проекта появится файл answers_test.csv
# Внимание! Для корректного запуска скрипта все файлы (включая скачанный с диска data_test.csv) должны располагаться в одной директории
