from distutils.core import setup

setup(
    name='ConvertBankStatement',
    author="Leandro Feller",
    version='0.1.dev0',
    packages=['convertBankStatement', ],
    dependencies=["PyPDF2==3.0.1", ],
    license='GNU GENERAL PUBLIC LICENSE',
    long_description=open('README.md').read(),
)