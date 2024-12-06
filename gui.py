import sys

from PyQt6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTabWidget,
                             QVBoxLayout, QWidget)

from super_calc import Calculator


class StandardCalculator(QWidget):
    """Калькулятор с интерфейсом, соответствующим дизайну"""
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()  
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

        # Кнопки памяти
        memory_buttons = ['mc', 'mr', 'm+', 'm-', 'ms', 'm:']
        for text in memory_buttons:
            btn = QPushButton(text)
            btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            memory_layout.addWidget(btn)

        # Добавляем панель памяти под строку ввода
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
        btn_C.clicked.connect(self.on_function_click)
        btn_C.setStyleSheet("font-size: 16px;")
        buttons_layout.addWidget(btn_C, 4, 0)

        btn_equal = QPushButton("=")
        btn_equal.clicked.connect(self.on_function_click)
        btn_equal.setStyleSheet("font-size: 16px;")
        buttons_layout.addWidget(btn_equal, 4, 2)

        # Добавляем сетку числовых кнопок в центральный макет
        central_layout.addLayout(buttons_layout)

        # Боковая панель с QGroupBox
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
            btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            trig_layout.addWidget(btn)
        trig_group.setLayout(trig_layout)
        trig_group.setStyleSheet("border: 2px solid orange;")

        # Специальные функции
        special_group = QGroupBox()
        special_layout = QVBoxLayout()
        special_buttons = ['sqrt', '^', 'mod']
        for text in special_buttons:
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
            btn.clicked.connect(lambda checked, btn=text: self.on_function_click(btn))
            btn.setStyleSheet("font-size: 16px;")
            other_layout.addWidget(btn)
        other_group.setLayout(other_layout)
        other_group.setStyleSheet("border: 2px solid brown;")

        # Добавляем все группы на боковую панель
        side_layout.addWidget(operations_group)
        side_layout.addWidget(trig_group)
        side_layout.addWidget(special_group)
        side_layout.addWidget(other_group)

        # Добавляем боковую панель в центральный макет
        central_layout.addLayout(side_layout)

        # Добавляем центральный макет в основной макет
        main_layout.addLayout(central_layout)

        self.setLayout(main_layout)

    def on_number_click(self, btn):
        current_text = self.display.text()
        if current_text == "0":
            self.display.setText(btn)
        else:
            self.display.setText(current_text + btn)

    def on_function_click(self, btn=None):
        sender = self.sender()
        if sender.text() == "C":
            self.display.setText("0")
        elif sender.text() == "=":
            try:
                # Получаем выражение из дисплея
                expression = self.display.text()
                tokens = expression.split()  # Разделяем текст на элементы
                
                if len(tokens) == 3:
                    # Бинарная операция (например, 5 + 3)
                    a = float(tokens[0])
                    op = tokens[1]
                    b = float(tokens[2])
                    
                    # Выполняем операцию
                    if op == "+":
                        result = self.calculator.add(a, b)
                    elif op == "-":
                        result = self.calculator.subtract(a, b)
                    elif op == "*":
                        result = self.calculator.multiply(a, b)
                    elif op == "/":
                        result = self.calculator.divide(a, b)
                    elif op == "mod":
                        result = self.calculator.modulus(a, b)
                    elif op == "^":
                        result = self.calculator.power(a, b)
                    else:
                        result = "Ошибка"
                elif len(tokens) == 2:
                    # Унарная операция (например, sin 30)
                    op = tokens[0]
                    a = float(tokens[1])
                    
                    if op == "sin":
                        result = self.calculator.sin(a)
                    elif op == "cos":
                        result = self.calculator.cos(a)
                    elif op == "sqrt":
                        result = self.calculator.sqrt(a)
                    elif op == "floor":
                        result = self.calculator.floor(a)
                    elif op == "ceil":
                        result = self.calculator.ceil(a)
                    else:
                        result = "Ошибка"
                else:
                    result = "Ошибка"

                # Устанавливаем результат
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Ошибка")
        elif sender.text() == "mc":
            self.calculator.mc()
        elif sender.text() == "mr":
            self.display.setText(str(self.calculator.mr()))
        elif sender.text() == "m+":
            try:
                value = float(self.display.text())
                self.calculator.m_plus(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif sender.text() == "m-":
            try:
                value = float(self.display.text())
                self.calculator.m_minus(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif sender.text() == "ms":
            try:
                value = float(self.display.text())
                self.calculator.ms(value)
            except ValueError:
                self.display.setText("Ошибка")
        elif sender.text() == "m:":
            self.display.setText(str(self.calculator.mr()))
        else:
            current_text = self.display.text()
            self.display.setText(current_text + " " + sender.text() + " ")



class CalculatorGUI(QWidget):
    """Основной интерфейс с вкладками"""
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Калькулятор")
        self.setGeometry(200, 200, 500, 500)

        layout = QVBoxLayout()

        # Вкладки
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
