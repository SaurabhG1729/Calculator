import sys
import re
import math
from PyQt6.QtWidgets import QApplication
from src.gui import CPoweredCalculator
from src.engine import MathEngine

class AppController:
    def __init__(self):
        self.ui = CPoweredCalculator()
        
        try:
            self.engine = MathEngine()
        except Exception as e:
            self.ui.show_error("DLL MISSING")
            print(f"Error: {e}")
            return

        # Connect the UI signal to the logic method
        self.ui.request_calculation.connect(self.process_math)

    def process_math(self, user_input):
        user_input = user_input.strip()
        if not user_input: return

        # 1. Validation
        if not re.match(r'^[0-9+\-*/^. ]+$', user_input):
            self.ui.show_error("INVALID INPUT")
            return

        # 2. Execution
        try:
            res = self.engine.run_calculation(user_input)
            
            if math.isnan(res):
                self.ui.show_error("SYNTAX ERROR")
            else:
                self.ui.show_success(f"OUT: {res:g}")
        except:
            self.ui.show_error("ENGINE CRASH")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    controller = AppController()
    controller.ui.show()
    sys.exit(app.exec())