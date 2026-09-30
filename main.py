tasks = []

def show_menu():
    print("\n--- Список задач (To-Do List) ---")
    print("1. Добавить задачу")
    print("2. Вывести список задач")
    print("3. Удалить задачу")
    print("4. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == '1':
            print("Функция добавления в разработке...")
        elif choice == '2':
            print("Функция просмотра в разработке...")
        elif choice == '3':
            print("Функция удаления в разработке...")
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()