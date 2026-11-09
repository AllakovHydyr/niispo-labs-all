import os
import shutil

def main():
    data_dir = '/var/data'
    result_dir = '/var/result'
    
    # Получаем список файлов в /var/data
    files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]
    
    if not files:
        print("Файлы не найдены в /var/data")
        return

    # Ищем самый большой по объёму файл
    largest_file = max(files, key=os.path.getsize)
    destination = os.path.join(result_dir, 'data.txt')
    
    # Копируем его в /var/result/data.txt
    shutil.copy(largest_file, destination)
    print(f"Самый большой файл '{os.path.basename(largest_file)}' скопирован в {destination}")

if __name__ == "__main__":
    main()