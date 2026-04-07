import ctypes
import os
import sys

class MathEngine:
    def __init__(self):
        # Path logic to find the DLL in the build folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        lib_path = os.path.join(base_dir, "..", "build", "main.dll")
        
        if not os.path.exists(lib_path):
            raise FileNotFoundError(f"DLL not found: {lib_path}")

        self.lib = ctypes.CDLL(os.path.abspath(lib_path))
        self.lib.evaluate.argtypes = [ctypes.c_char_p]
        self.lib.evaluate.restype = ctypes.c_double

    def run_calculation(self, expression_str):
        return self.lib.evaluate(expression_str.encode('utf-8'))