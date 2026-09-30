tasks = []

def add_task():
    task = input("Введите текст задачи: ").strip()
    if task:
        tasks.append(task)
        print(f"Задача '{task}' успешно добавлена!")
    else:
        print("Текст задачи не может быть пустым.")

def list_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task():
    list_tasks()
    if not tasks:
        return
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Задача '{removed}' удалена.")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Ошибка: введите числовой номер задачи.")

def main():
    while True:
        print("\n--- Список задач (To-Do List) ---")
        print("1. Добавить задачу")
        print("2. Вывести список задач")
        print("3. Удалить задачу")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

if __name__ == "__main__":
    main()