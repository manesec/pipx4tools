import shutil
import subprocess
import sys
from pathlib import Path

def copy_asn_files(overwrite=False):
    asn_dir = Path(__file__).resolve().parent / "rsa_sign2n" / "standalone"
    pkcs1_src = asn_dir / "pkcs1.asn"
    x509_src = asn_dir / "x509.asn"
    pkcs1_dst = Path.cwd() / "pkcs1.asn"
    x509_dst = Path.cwd() / "x509.asn"
    
    for src, dst in [(pkcs1_src, pkcs1_dst), (x509_src, x509_dst)]:
        if not src.exists():
            print(f"[!] Error: {src} does not exist!")
            sys.exit(1)
    
    files_exist = any(dst.exists() for dst in [pkcs1_dst, x509_dst])
    if files_exist:
        print("[!] One or both of pkcs1.asn and x509.asn already exist in the current directory.")
        response = input("Do you want to overwrite them? (Y/n): ").strip().lower()
        if response != 'y':
            print("[!] Operation cancelled. Exiting.")
            sys.exit(1)
    
    for src, dst in [(pkcs1_src, pkcs1_dst), (x509_src, x509_dst)]:
        shutil.copy(src, dst)
        print(f"[*] Copied {src} -> {dst}")

def cleanup_asn_files():
    for f in [Path.cwd() / "pkcs1.asn", Path.cwd() / "x509.asn"]:
        if f.exists():
            f.unlink()
            print(f"[*] Cleaning up: {f}")

def start_sign2n():
    copy_asn_files()
    
    try:
        script_path = Path(__file__).resolve().parent / "rsa_sign2n" / "standalone" / "jwt_forgery.py"
        args = sys.argv[1:]
        command = [sys.executable, str(script_path)] + args
        subprocess.run(command)
    finally:
        print("================================================================================")
        cleanup_asn_files()
