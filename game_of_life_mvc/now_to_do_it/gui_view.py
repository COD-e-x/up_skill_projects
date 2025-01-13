from tkinter import *


class GameView:
    def __init__(self, root, game, cell_size=5):
        """Отображение игры, управление визуальной частью и взаимодействие с пользователем."""
        self.root = root
        self.game = game
        self.cell_size = cell_size

        # Создание виджетов
        self.grid_view = Canvas(self.root, width=self.game.width * self.cell_size,
                                height=self.game.height * self.cell_size,
                                borderwidth=0, highlightthickness=0, bg='white')
        self.start_button = Button(self.root, text='Start', width=12)
        self.clear_button = Button(self.root, text='Clear', width=12)

        # Настройка меню для выбора паттерна
        self.choice = StringVar(self.root)
        self.choice.set('Choose a Pattern')
        self.option_menu = OptionMenu(self.root, self.choice, 'Choose a Pattern',
                                      'glider', 'glider gun', 'random')
        self.option_menu.config(width=20)

        # Инициализация интерфейса (кнопки, сетка и т.д.).
        self.grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
        self.start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        self.option_menu.grid(row=1, column=1, padx=20)
        self.clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)

    def clear_canvas(self):
        """Очищает экран от всех элементов."""
        return self.grid_view.delete(ALL)

    def bind_events(self, controller):
        """Привязывает события к методам контроллера (клики по кнопкам и клеткам)."""
        self.choice.trace_add('write', lambda varname, index, mode: controller.option_handler(self.choice.get()))
        self.grid_view.bind('<Button-1>', controller.grid_handler)
        self.start_button.bind('<Button-1>', controller.start_handler)
        self.clear_button.bind('<Button-1>', controller.clear_handler)

    def draw_cell(self, row, col, color):
        """Рисует ячейку на экране с заданными координатами и цветом."""
        outline = 'grey' if color == 'black' else 'white'
        self.grid_view.create_rectangle(row * self.cell_size, col * self.cell_size,
                                        row * self.cell_size + self.cell_size,
                                        col * self.cell_size + self.cell_size,
                                        fill=color, outline=outline)

    def update_start_button(self, text):
        """Обновляет текст на кнопке 'Start/Pause'."""
        self.start_button.config(text=text)
