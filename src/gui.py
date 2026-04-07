import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal

class CPoweredCalculator(QMainWindow):
    # This signal sends the user input out to the main script
    request_calculation = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("C-Engine Calculator")
        self.setFixedSize(450, 300)
        self.apply_dark_theme()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setSpacing(15)

        self.header = QLabel("C-POWERED CALCULATOR")
        self.header.setObjectName("HeaderLabel")
        self.layout.addWidget(self.header)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter expression...")
        self.input_box.setFixedHeight(45)
        self.input_box.returnPressed.connect(self.emit_request) 
        self.layout.addWidget(self.input_box)

        self.btn = QPushButton("EVALUATE")
        self.btn.setFixedHeight(50)
        self.btn.clicked.connect(self.emit_request)
        self.layout.addWidget(self.btn)

        self.result_label = QLabel("IDLE...")
        self.result_label.setObjectName("ResultLabel")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.result_label)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #0f0f0f; }
            #HeaderLabel { font-size: 24px; color: #555; letter-spacing: 2px; font-weight: bold; }
            QLineEdit {
                background-color: #1a1a1a;
                color: #00ff00; 
                border: 1px solid #333;
                border-radius: 2px;
                padding: 8px;
                font-family: 'Consolas', monospace;
                font-size: 18px;
            }
            QPushButton {
                background-color: #222;
                color: #aaa;
                border: 1px solid #444;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #333; color: #fff; }
            #ResultLabel { font-size: 24px; color: #444; font-family: 'Consolas'; }
        """)

    def emit_request(self):
        self.request_calculation.emit(self.input_box.text())

    def show_success(self, res_text):
        self.result_label.setText(res_text)
        self.result_label.setStyleSheet("color: #00ff00; font-size: 24px;")

    def show_error(self, msg):
        self.result_label.setText(msg)
        self.result_label.setStyleSheet("color: #ff3333; font-size: 20px;")