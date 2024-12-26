try:
   
    module_name = input("Введіть назву модуля для імпорту: ")
    imported_module = __import__(module_name)

    
    function_name = input("Введіть назву функції, яку потрібно викликати: ")

   
    if hasattr(imported_module, function_name):
        func = getattr(imported_module, function_name)
        
        # Викликаємо функцію
        print(f"Виклик функції '{function_name}' з модуля '{module_name}':")
        result = func() 
        print("Результат виконання функції:", result)
    else:
        raise AttributeError(f"Функція '{function_name}' не знайдена у модулі '{module_name}'")
except ModuleNotFoundError:
    print("Помилка: Вказаний модуль не знайдено. Перевірте правильність назви.")
except AttributeError as e:
    print(e)
except Exception as e:
    print(f"Сталася непередбачена помилка: {e}")
