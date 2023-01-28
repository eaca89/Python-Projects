from PyQt5 import QtCore, QtGui, QtWidgets


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 480, 620)
        self.setWindowTitle("Calculator")
        self.display = QtWidgets.QLineEdit(self)
        self.display.setFixedSize(460, 40)
        self.display.move(10, 10)
        self.display.setReadOnly(True)
        self.create_button("1", 50, 70, 80, 80)
        self.create_button("2", 140, 70, 80, 80)
        self.create_button("3", 230, 70, 80, 80)
        self.create_button("4", 50, 160, 80, 80)
        self.create_button("5", 140, 160, 80, 80)
        self.create_button("6", 230, 160, 80, 80)
        self.create_button("7", 50, 250, 80, 80)
        self.create_button("8", 140, 250, 80, 80)
        self.create_button("9", 230, 250, 80, 80)
        self.create_button("0", 140, 340, 80, 80)
        self.create_button("+", 320, 70, 80, 80)
        self.create_button("-", 320, 160, 80, 80)
        self.create_button("*", 320, 250, 80, 80)
        self.create_button("/", 320, 340, 80, 80)
        self.create_button("=", 410, 340, 80, 80)
        self.create_button(".", 410, 250, 80, 80)
        self.create_button("C", 410, 160, 80, 80)

    def create_button(self, text, x, y, width, height):
        button = QtWidgets.QPushButton(text, self)
        button.setFixedSize(width, height)
        button.move(x, y)
        button.clicked.connect(lambda: self.handle_button(text))

    def handle_button(self, text):
        if text == "C":
            self.display.setText("")
        elif text in "0123456789.":
            self.display.setText(self.display.text() + text)
        else:
            expression = self.display.text()
            expression += text
            try:
                self.display.setText(str(eval(expression)))
            except:
                self.display.setText("Error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
