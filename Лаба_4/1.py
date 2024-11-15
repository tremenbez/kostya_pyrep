import json

def calculate_sum(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        total_sum = sum(item['score'] * item['weight'] for item in data)
        return round(total_sum, 3)

    except (KeyError, TypeError, ValueError) as e:
        print(f"Ошибка в обработке данных: {e}")
        return None

    except FileNotFoundError:
        print("Файл не найден.")
        return None

print(calculate_sum('input.json'))
