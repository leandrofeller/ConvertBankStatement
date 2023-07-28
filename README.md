ConvertBankStatement

ConvertBankStatement is a Python package designed to convert bank statements from PDF files to JSON format. Currently, the software supports statements from two banks, namely Monzo and Revolut.

Installation
To install ConvertBankStatement, you can use pip. Open your terminal or command prompt and run the following command:

pip install ConvertBankStatement

Usage
To use ConvertBankStatement, you need to run the main.py script with the appropriate parameters:

python main.py '<bank_name>' '<statement_file_path>'

The bank_name parameter should be either 'Monzo' or 'Revolut', depending on the bank you want to process the statement for. 
The statement_file_path parameter should be the path to the PDF file of the bank statement you wish to read.


Example

python main.py 'Monzo' 'C:/path/to/monzo_statement.pdf'
The script will process the specified Monzo statement PDF file and output the results in a JSON format.

Support
Currently, ConvertBankStatement supports the following banks:

Monzo
Revolut

Limitations
HSBC statements are not accepted as the PDFs are encrypted.


If you encounter any issues or have suggestions for improvements, feel free to report them on our GitHub repository.

License
ConvertBankStatement is licensed under the GNU License.