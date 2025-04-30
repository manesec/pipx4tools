from setuptools import setup, find_packages

def read_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line and not line.startswith('#')]

def install_requirements():
    all_requirements = []
    all_requirements.extend(read_requirements('src/rsa_sign2n/standalone/requirements.txt'))

    # patch gmpy2
    for req in all_requirements:
        if req.startswith('gmpy2==2.1.2'):
            all_requirements.remove(req)
            all_requirements.append('gmpy2')

    return all_requirements

setup(
    name='pipx4tools-rsa-sign2n',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "jwt_forgery.py=src.start:start_sign2n",
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
