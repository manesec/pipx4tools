import os,subprocess,sys
from pathlib import Path

def start_sign2n():
    script_path = Path(__file__).resolve().parent / "rsa_sign2n" / "standalone" / "jwt_forgery.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    os.chdir(Path(__file__).resolve().parent / "rsa_sign2n" / "standalone")
    subprocess.run(command)
