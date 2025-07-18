from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []
    all_requirements.extend(read_requirements('src/jwt_tool/requirements.txt'))
    all_requirements.extend(read_requirements('src/DNSrebinder/requirements.txt'))
    all_requirements.extend(read_requirements('src/STEWS/fingerprint/requirements.txt'))
    all_requirements.extend(read_requirements('src/STEWS/vuln-detect/requirements.txt'))
    all_requirements.extend(read_requirements('src/peas/requirements.txt'))
    return all_requirements

setup(
    name='pipx4tools',
    version='0.0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "jwt_tool.py=src.start:start_sign2n",
            "dnsrebinder.py=src.start:start_dns_rebinder",
            "php_filter_chain_generator.py=src.start:start_php_filter_chain_generator",
            "STEWS-fingerprint.py=src.start:start_STEWS_fingerprint",
            "STEWS-vuln-detect.py=src.start:start_STEWS_vuln_detect",
            "peas.py=src.start:start_peas",
        ],
    },
    install_requires=install_requirements(),
    python_requires='>=3.6',
    author='manesec, silentsignal',
    author_email='mane@manesec.com',
    description='collection for pipx with redteam tools.',
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manesec/pipx4tools',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
