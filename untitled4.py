try:
   
    file_path = input("Введіть шлях до файлу: ")
    

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
  
    print("Вміст файлу:")
    print(content)
except FileNotFoundError:
   
    print("Помилка: Файл за вказаним шляхом не знайдено. Перевірте правильність шляху.")
except Exception as e:
  
    print(f"Сталася непередбачена помилка: {e}")
