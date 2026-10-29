import json
import logging
from pathlib import Path
from utils.reader import read_numbers
from utils.statistics import calculate_average, find_max, find_min
def load_config(config_file):
    with open(config_file, "r", encoding="utf-8") as file:
        return json.load(file)
def validate_numbers(numbers):
    if len(numbers) == 0:
        raise ValueError("Список измерений пуст")
def main():
    base_dir = Path(__file__).parent
    config_file = base_dir / "config.json"
    config = load_config(config_file)
    input_file = base_dir / config["input_file"]
    log_file = base_dir / config["log_file"]
    log_file.parent.mkdir(exist_ok=True)
    logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s", encoding="utf-8")
    logging.info("Запуск программы")
    logging.info("Конфигурация загружена: %s", config_file)
    print("Текущий рабочий каталог:", Path.cwd())
    print("Файл измерений:", input_file)
    print("Файл существует:", input_file.exists())
    try:
        numbers = read_numbers(input_file)
        logging.info("Файл успешно прочитан: %s", input_file)
        logging.info("Количество прочитанных значений: %d", len(numbers))
        validate_numbers(numbers)
        count = len(numbers)
        average = round(calculate_average(numbers), 2)
        minimum = find_min(numbers)
        maximum = find_max(numbers)
        print("Количество значений:", count)
        print("Среднее значение:", average)
        print("Минимум:", minimum)
        print("Максимум:", maximum)
        logging.info("Статистика: количество=%d, минимум=%s, максимум=%s, среднее=%s", count, minimum, maximum, average)
    except FileNotFoundError:
        logging.error("Ошибка: файл не найден — %s", input_file)
        print("Ошибка: файл не найден")
    except ValueError as error:
        logging.error("Ошибка данных: %s", error)
        print("Ошибка:", error)
    finally:
        logging.info("Завершение программы")
if __name__ == "__main__":
    main()
