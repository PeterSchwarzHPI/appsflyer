from setuptools import setup

setup(
    name='appsflyer',
    version='0.0.12',
    description='AppsFlyer client for Python',
    author='PeteBlack',
    url='https://github.com/PeterSchwarzHPI/appsflyer',
    packages=[
        'appsflyer',
    ],
    license='GNU General Public License v3.0',
    install_requires=[
        'requests',
    ],
)
