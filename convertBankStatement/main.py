import sys
from read_statement import convert_pdf


if __name__ == '__main__':
    par = sys.argv[1:]
    result = convert_pdf(par)
    print(result)
