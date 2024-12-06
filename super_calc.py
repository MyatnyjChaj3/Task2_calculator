import math


class Calculator:
    def memory_clear(self):
        """Очистка памяти."""
        self.calculator.mc()
        self.display.setText("Memory Cleared")

    def memory_recall(self):
        """Вызов значения из памяти."""
        value = self.calculator.mr()
        self.display.setText(str(value))

    def memory_add(self):
        """Добавление значения к памяти."""
        try:
            value = float(self.display.text())
            self.calculator.m_plus(value)
            self.display.setText("Memory Updated")
        except ValueError:
            self.display.setText("Error")

    def memory_subtract(self):
        """Вычитание значения из памяти."""
        try:
            value = float(self.display.text())
            self.calculator.m_minus(value)
            self.display.setText("Memory Updated")
        except ValueError:
            self.display.setText("Error")

    def memory_store(self):
        """Сохранение значения в память."""
        try:
            value = float(self.display.text())
            self.calculator.ms(value)
            self.display.setText("Memory Saved")
        except ValueError:
            self.display.setText("Error")

    def memory_show(self):
        """Отображение текущего значения в памяти."""
        value = self.calculator.mr()
        self.display.setText(f"Memory: {value}")