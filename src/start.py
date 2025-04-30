import shutil
import subprocess
import sys
from pathlib import Path

def start_sign2n():
    script_path = Path(__file__).resolve().parent / "jwt_tool" / "jwt_tool.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)
