from setuptools import setup

setup(
    name='citizenshell',
    version='0.3.3',
    packages=['citizenshell'],
    url='https://github.com/meuter/citizenshell',
    license='MIT',
    author='Cedric Meuter',
    author_email='cedric.meuter@gmail.com',
    description='Interact with shell locally or over different connection types (telnet, ssh, serial, adb)',
    keywords=["shell", "telnet", "adb", "ssh", "serial"],
    classifiers=[],
    download_url="https://github.com/meuter/citizenshell/archive/0.3.3.tar.gz",
    install_requires=[
        'termcolor',
        'paramiko'
    ]
)
