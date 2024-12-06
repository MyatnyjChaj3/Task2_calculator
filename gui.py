import sys

from PyQt6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
                             QPushButton, QTabWidget, QVBoxLayout, QWidget)

from graphics import plot_linear, plot_quadratic, plot_trig
from super_calc import Calculator


class StandardCalculator(QWidget):
    """Калькулятор со стандартным интерфейсом"""
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        # Layout
        layout = QVBoxLayout()
        
        # Поле ввода
        self.display = QLineEdit("0")
        layout.addWidget(self.display)

        # Кнопки
        grid = QGridLayout()
        buttons = [
            ('7', (0, 0)), ('8', (0, 1)), ('9', (0, 2)), 
            ('4', (1, 0)), ('5', (1, 1)), ('6', (1, 2)), 
            ('1', (2, 0)), ('2', (2, 1)), ('3', (2, 2)), 
            ('0', (3, 1)), ('+', (3, 2)), ('-', (3, 3)), 
            ('*', (4, 2)), ('/', (4, 3)), ('C', (4, 1)), ('=', (4, 0))
        ]

        for (text, pos) in buttons:
            button = QPushButton(text)
            button.clicked.connect(lambda checked, btn=text: self.on_button_click(btn))
            grid.addWidget(button, *pos)

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_button_click(self, btn):
        if btn == 'C':
            self.display.setText('')
        elif btn == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Ошибка")
        else:
            self.display.setText(self.display.text() + btn)


class GraphsTab(QWidget):
    """Вкладка для визуализации графиков"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Поле ввода для уравнения
        self.equation_input = QLineEdit()
        self.equation_input.setPlaceholderText("Введите уравнение: например, 2x + 3")
        layout.addWidget(self.equation_input)

        # Кнопка для построения графика
        self.plot_button = QPushButton("Построить график")
        self.plot_button.clicked.connect(self.plot_graph)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def plot_graph(self):
        text = self.equation_input.text()
        if "x" in text:
            # В примере реализуем линейный график
            try:
                a, b = [float(x) for x in text.replace("x", "").split()]
                plot_linear(a, b)
            except:
                self.equation_input.setText("Ошибка в уравнении")


class CalculatorGUI(QWidget):
    """Основной графический интерфейс с вкладками"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(200, 200, 600, 400)

        # Основной Layout
        layout = QVBoxLayout()

        # Создание вкладок
        self.tabs = QTabWidget()
        self.standard_calc = StandardCalculator()
        self.graph_tab = GraphsTab()

        # Добавление вкладок
        self.tabs.addTab(self.standard_calc, "Стандартный калькулятор")
        self.tabs.addTab(self.graph_tab, "Графики")

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def run(self):
        self.show()
