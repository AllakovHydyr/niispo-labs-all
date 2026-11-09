import os

def main():
    data_file = '/var/data/data.txt'
    result_file = '/var/result/result.txt'
    
    if not os.path.exists(data_file):
        print(f"Файл {data_file} не найден!")
        return

    # Читаем файл и извлекаем все числа
    with open(data_file, 'r') as f:
        content = f.read()
    
    # Разбиваем по пробелам и переносам строк, оставляя только числа
    numbers = []
    for word in content.split():
        try:
            numbers.append(int(word))
        except ValueError:
            pass # Пропускаем, если это не число

    if len(numbers) < 2:
        print("В файле недостаточно чисел для вычисления произведения.")
        return

    # Берём первое и последнее число
    first_num = numbers[0]
    last_num = numbers[-1]
    product = first_num * last_num

    # Сохраняем результат
    with open(result_file, 'w') as f:
        f.write(str(product))

    # Выводим на экран (по требованию задания)
    print(f"Первое число: {first_num}")
    print(f"Последнее число: {last_num}")
    print(f"Произведение: {product}")

if __name__ == "__main__":
    main()