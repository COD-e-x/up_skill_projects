from templates.glider import glider_pattern
from templates.glider_gun import glider_gun_pattern


class GameController:
    """Контроллер, управляющий логикой игры и взаимодействием с моделью и представлением."""

    def __init__(self, game, view):
        """Инициализация контроллера и привязка событий."""
        self.game = game
        self.view = view
        self.is_running = False
        self.view.bind_events(self)

    def option_handler(self, _):
        """Обрабатывает выбор паттерна пользователем."""
        self.is_running = False
        selection = self.view.choice.get()
        if selection == 'glider':
            self.game.load_pattern(glider_pattern, 10, 10)
        elif selection == 'glider gun':
            self.game.load_pattern(glider_gun_pattern, 10, 10)
        elif selection == 'random':
            self.game.randomize()
        self.update()

    def start_handler(self, _):
        """Запускает или ставит игру на паузу."""
        self.is_running = not self.is_running
        self.view.update_start_button('Pause' if self.is_running else 'Start')
        if self.is_running:
            self.update()

    def clear_handler(self, _):
        """Очищает сетку и сбрасывает игру."""
        self.is_running = False
        self.game.load_pattern([[0] * self.game.width] * self.game.height)
        self.view.update_start_button('Start')
        self.update()

    def grid_handler(self, event):
        """Обрабатывает клики по клеткам сетки, переключая их состояние."""
        x = int(event.x / self.view.cell_size)
        y = int(event.y / self.view.cell_size)
        current_value = self.game.grid_model[x][y]
        new_value = 0 if current_value == 1 else 1
        self.game.grid_model[x][y] = new_value
        self.view.draw_cell(x, y, 'black' if new_value == 1 else 'white')

    def update(self):
        """Обновляет сетку и выполняет шаг игры, если она запущена."""
        self.view.clear_canvas()
        self.game.next_generation()
        for i in range(self.game.height):
            for j in range(self.game.width):
                if self.game.grid_model[i][j] == 1:
                    self.view.draw_cell(i, j, 'black')
        if self.is_running:
            self.view.root.after(100, self.update)
