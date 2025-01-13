from random import randint


class GridModel:
    """Модель для работы с сеткой игры, управление состоянием ячеек и генерациями."""

    def __init__(self, width, height):
        """Инициализация модели с заданными размерами сетки."""
        self.width = width
        self.height = height
        self.grid_model = [[0] * width for _ in range(height)]
        self.next_grid = [[0] * width for _ in range(height)]

    def load_pattern(self, pattern, x_offset=0, y_offset=0):
        """Загружает паттерн в сетку с заданным смещением."""
        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid_model[i][j] = 0
        j = y_offset
        for row in pattern:
            i = x_offset
            for value in row:
                self.grid_model[i][j] = value
                i = i + 1
            j = j + 1

    def randomize(self):
        """Заполняет сетку случайными значениями 0 и 1."""
        for i in range(self.height):
            for j in range(self.width):
                self.grid_model[i][j] = randint(0, 1)

    def next_generation(self):
        """Обновляет сетку до следующего поколения согласно правилам игры."""
        for i in range(self.height):
            for j in range(self.width):
                count = self.count_neighbors(i, j)
                if self.grid_model[i][j] == 0 and count == 3:
                    self.next_grid[i][j] = 1
                elif self.grid_model[i][j] == 1 and count in (2, 3):
                    self.next_grid[i][j] = 1
                else:
                    self.next_grid[i][j] = 0
        self.grid_model, self.next_grid = self.next_grid, self.grid_model

    def count_neighbors(self, row, col):
        """Подсчитывает количество соседей, которые живы, для клетки."""
        count = 0
        if row - 1 >= 0:
            count += self.grid_model[row - 1][col]
        if row - 1 >= 0 and col - 1 >= 0:
            count += self.grid_model[row - 1][col - 1]
        if row - 1 >= 0 and col + 1 < self.width:
            count += self.grid_model[row - 1][col + 1]
        if col - 1 >= 0:
            count += self.grid_model[row][col - 1]
        if col + 1 < self.width:
            count += self.grid_model[row][col + 1]
        if row + 1 < self.height:
            count += self.grid_model[row + 1][col]
        if row + 1 < self.height and col - 1 >= 0:
            count += self.grid_model[row + 1][col - 1]
        if row + 1 < self.height and col + 1 < self.width:
            count += self.grid_model[row + 1][col + 1]
        return count
