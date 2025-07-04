import shutil
import subprocess
import sys
from pathlib import Path


def start_dns_rebinder():
    script_path = Path(__file__).resolve().parent / "DNSrebinder" / "dnsrebinder.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

def start_sign2n():
    script_path = Path(__file__).resolve().parent / "jwt_tool" / "jwt_tool.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

def start_php_filter_chain_generator():
    script_path = Path(__file__).resolve().parent / "php_filter_chain_generator" / "php_filter_chain_generator.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)


def start_STEWS_fingerprint():
    script_path = Path(__file__).resolve().parent / "STEWS" / "fingerprint" / "STEWS-fingerprint.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)

def start_STEWS_vuln_detect():
    script_path = Path(__file__).resolve().parent / "STEWS" / "vuln-detect" / "STEWS-vuln-detect.py"
    args = sys.argv[1:]
    command = [sys.executable, str(script_path)] + args
    subprocess.run(command)
