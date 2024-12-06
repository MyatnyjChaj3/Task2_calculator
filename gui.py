import sys
from PyQt6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTabWidget,
                             QVBoxLayout, QWidget)

from calc_functions import Calculator
calc = Calculator()

class StandardCalculator(QWidget):
    """Калькулятор с интерфейсом"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Поле ввода
        self.display = QLineEdit("0")
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px; color: white; background-color: black;")
        main_layout.addWidget(self.display)

        # Панель управления памятью
        memory_layout = QHBoxLayout()
        memory_buttons = ['mc', 'mr', 'm+', 'm-', 'ms', 'm:']
        for text in memory_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            memory_layout.addWidget(btn)
        main_layout.addLayout(memory_layout)

        # Основной контейнер для числовых кнопок и групп справа
        central_layout = QHBoxLayout()

        # Сетка для кнопок
        buttons_layout = QGridLayout()

        # Числовые кнопки
        num_buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('+/-', 3, 0), ('0', 3, 1), ('.', 3, 2)
        ]
        for text, row, col in num_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_number_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            buttons_layout.addWidget(btn, row, col)

        # Кнопка "C" и "="
        btn_C = QPushButton("C")
        btn_C.clicked.connect(lambda: self.on_function_click("C"))
        btn_C.setStyleSheet("font-size: 16px;")
        buttons_layout.addWidget(btn_C, 4, 0)

        btn_equal = QPushButton("=")
        btn_equal.clicked.connect(lambda: self.on_function_click("="))
        btn_equal.setStyleSheet("font-size: 16px;")
        buttons_layout.addWidget(btn_equal, 4, 2)

        central_layout.addLayout(buttons_layout)

        # Боковая панель
        side_layout = QVBoxLayout()

        # Операции
        operations_group = QGroupBox()
        operations_layout = QVBoxLayout()
        operations_buttons = ['+', '-', '*', '/']
        for text in operations_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            operations_layout.addWidget(btn)
        operations_group.setLayout(operations_layout)
        operations_group.setStyleSheet("border: 2px solid yellow;")

        # Тригонометрия
        trig_group = QGroupBox()
        trig_layout = QVBoxLayout()
        trig_buttons = ['sin', 'cos']
        for text in trig_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_unary_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            trig_layout.addWidget(btn)
        trig_group.setLayout(trig_layout)
        trig_group.setStyleSheet("border: 2px solid orange;")

        # Специальные функции
        special_group = QGroupBox()
        special_layout = QVBoxLayout()
        special_buttons = ['sqrt', '^', 'mod']
        for text in special_buttons:
            if text in ['sqrt', 'floor', 'ceil']:
                btn = QPushButton(text)
                btn.clicked.connect(lambda checked, btn=text: self.on_unary_function_click(btn))
            else:
                btn = QPushButton(text)
                btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            special_layout.addWidget(btn)
        special_group.setLayout(special_layout)
        special_group.setStyleSheet("border: 2px solid pink;")

        # Остальные функции
        other_group = QGroupBox()
        other_layout = QVBoxLayout()
        other_buttons = ['floor', 'ceil']
        for text in other_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_unary_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            other_layout.addWidget(btn)
        other_group.setLayout(other_layout)
        other_group.setStyleSheet("border: 2px solid brown;")

        side_layout.addWidget(operations_group)
        side_layout.addWidget(trig_group)
        side_layout.addWidget(special_group)
        side_layout.addWidget(other_group)

        central_layout.addLayout(side_layout)
        main_layout.addLayout(central_layout)

        self.setLayout(main_layout)

    def on_number_click(self, btn):
        current_text = self.display.text()
        if current_text == "0":
            self.display.setText(btn)
        else:
            self.display.setText(current_text + btn)

    def on_unary_function_click(self, btn):
        # Для унарных функций ожидаем формат: "sin 30", "cos 45", "sqrt 16", "floor 4.7", "ceil 4.2"
        current_text = self.display.text().strip()
        # Если текст "0", то заменим его на пустой для удобства
        if current_text == "0":
            current_text = ""
        # Формируем строку: "<op> <value>"
        # Если сейчас есть число, то ставим операцию впереди.
        self.display.setText(btn + " " + current_text)

    def on_function_click(self, btn):
        # Обработка кнопок функций, операций и результата
        if btn == "C":
            self.display.setText("0")
        elif btn == "=":
            try:
                expression = self.display.text().strip()
                tokens = expression.split()

                # Проверка формата
                if len(tokens) == 3:
                    # Формат: a op b
                    a, op, b = tokens
                    a = float(a)
                    b = float(b)

                    if op == "+":
                        result = calc.add(a, b)
                    elif op == "-":
                        result = calc.subtract(a, b)
                    elif op == "*":
                        result = calc.multiply(a, b)
                    elif op == "/":
                        result = calc.divide(a, b)
                    elif op == "mod":
                        result = calc.remainder(a, b)
                    elif op == "^":
                        result = calc.pow(a, b)
                    else:
                        result = "Ошибка"

                elif len(tokens) == 2:
                    # Формат: op a (унарная операция, например: "sin 30")
                    op, val = tokens
                    a = float(val)

                    if op == "sin":
                        result = calc.sin(a)
                    elif op == "cos":
                        result = calc.cos(a)
                    elif op == "sqrt":
                        result = calc.sqrt(a)
                    elif op == "floor":
                        result = calc.floor(a)
                    elif op == "ceil":
                        result = calc.ceil(a)
                    else:
                        result = "Ошибка"
                else:
                    result = "Ошибка"

                self.display.setText(str(result))
            except Exception:
                self.display.setText("Ошибка")

        elif btn == "mc":
            calc.memory_clear()
        elif btn == "mr":
            self.display.setText(str(calc.memory_recall()))
        elif btn == "m+":
            try:
                value = float(self.display.text())
                calc.memory_add(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif btn == "m-":
            try:
                value = float(self.display.text())
                calc.memory_subtract(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif btn == "ms":
            try:
                value = float(self.display.text())
                calc.memory_set(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif btn == "m:":
            self.display.setText(str(calc.memory_recall()))
        else:
            # Операции вроде +, -, *, /, mod, ^
            current_text = self.display.text().strip()
            if current_text == "0":
                current_text = "0"
            self.display.setText(current_text + " " + btn + " ")


class CalculatorGUI(QWidget):
    """Основной интерфейс с вкладками"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(200, 200, 500, 500)

        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(StandardCalculator(), "Калькулятор")
        layout.addWidget(tabs)
        self.setLayout(layout)

    def run(self):
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    gui = CalculatorGUI()
    gui.run()
    sys.exit(app.exec())
