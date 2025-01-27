import tkinter as tk
from tkinter import messagebox


class KanbanBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban-доска: План проекта")

        # Определяем этапы проекта и их задачи
        self.stages = {
            "Этап 1: Подготовка и проектирование": [
                "Определить атрибуты и методы для класса Hero.",
                "Определить атрибуты и методы для класса Game."
            ],
            "Этап 2: Реализация класса Hero": [
                "Реализовать атрибуты name, health, attack_power.",
                "Реализовать метод attack(other).",
                "Реализовать метод is_alive()."
            ],
            "Этап 3: Реализация класса Game": [
                "Реализовать атрибуты player и computer.",
                "Реализовать метод start().",
                "Реализовать ход игрока.",
                "Реализовать ход компьютера.",
                "Обрабатывать проверку состояния здоровья героев.",
                "Объявлять победителя."
            ],
            "Этап 4: Тестирование и отладка": [
                "Провести тестирование с разными параметрами здоровья и силы удара.",
                "Проверить обработку краевых случаев.",
                "Убедиться, что текстовый вывод игры информативен."
            ]
        }

        # Создаем заголовки этапов
        for i, (stage, tasks) in enumerate(self.stages.items()):
            frame = tk.LabelFrame(self.root, text=stage, padx=10, pady=10, font=("Arial", 12, "bold"))
            frame.grid(row=0, column=i, padx=10, pady=10, sticky="n")

            # Для каждой задачи создаем чекбокс
            for task in tasks:
                var = tk.BooleanVar()
                cb = tk.Checkbutton(frame, text=task, variable=var, font=("Arial", 10), wraplength=200)
                cb.pack(anchor="w", pady=2)
                cb.var = var  # Сохраняем переменную для проверки состояния

        # Добавляем кнопку для завершения всех задач
        complete_button = tk.Button(self.root, text="Завершить проект", command=self.check_completion,
                                     bg="green", fg="white", font=("Arial", 12, "bold"))
        complete_button.grid(row=1, column=0, columnspan=4, pady=10, sticky="ew")

    def check_completion(self):
        """
        Проверяет выполнение всех задач. Если все задачи завершены, поздравляет пользователя.
        """
        all_completed = True
        for frame in self.root.winfo_children():
            if isinstance(frame, tk.LabelFrame):
                for child in frame.winfo_children():
                    if isinstance(child, tk.Checkbutton) and not child.var.get():
                        all_completed = False

        if all_completed:
            messagebox.showinfo("Поздравляем!", "Все задачи выполнены! Проект завершен.")
        else:
            messagebox.showwarning("Внимание", "Некоторые задачи еще не завершены.")


if __name__ == "__main__":
    root = tk.Tk()
    app = KanbanBoard(root)
    root.mainloop()
