import sys
from PyQt4.QtGui import QApplication, QMainWindow, QGridLayout, QLineEdit, QPushButton, QWidget

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 250, 250)

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QGridLayout()
        self.widget.setLayout(self.layout)

        self.entry = QLineEdit()
        self.layout.addWidget(self.entry, 0, 0, 1, 4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', self.func_number), ('8', self.func_number), ('9', self.func_number), ('/', self.func_operator),
            ('4', self.func_number), ('5', self.func_number), ('6', self.func_number), ('*', self.func_operator),
            ('1', self.func_number), ('2', self.func_number), ('3', self.func_number), ('-', self.func_operator),
            ('0', self.func_number), ('.', self.func_number), ('C', self.func_clear), ('+', self.func_operator),
            ('=', self.func_equal)
        ]

        positions = [(i+1, j) for i in range(5) for j in range(4)]
        for position, (text, handler) in zip(positions, buttons):
            button = QPushButton(text)
            button.clicked.connect(lambda _, t=text, h=handler: h(t))
            self.layout.addWidget(button, *position)

    def func_number(self, value):
        current = self.entry.text()
        self.entry.setText(current + value)

    def func_operator(self, operator):
        current = self.entry.text()
        if current and current[-1] in '+-*/':
            # Son karakter zaten operatörse değiştir
            self.entry.setText(current[:-1] + operator)
        else:
            self.entry.setText(current + operator)

    def func_clear(self, _):
        self.entry.clear()

    def func_equal(self, _):
        try:
            result = eval(self.entry.text())
            self.entry.setText(str(result))
        except Exception:
            self.entry.setText("Hata")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
