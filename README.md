<h1>Convert Bank Statement</h1>

ConvertBankStatement is a Python module designed to convert bank statements from PDF files to JSON format. The output will be an array with two positions. The first position is a code where negative numbers mean errors and 0 means successfully processed. The second position will be a message explain the error or the JSON with the transactions.</br>
Currently, the software supports statements from two banks, namely Monzo and Revolut.

<h3>Usage</h3>
To use ConvertBankStatement, you need to run the main.py script with the appropriate parameters:
</br></br>
<pre>
  <code>python main.py 'bank_name' 'statement_file_path'</code>
</pre>
</br>
The bank_name parameter should be either 'Monzo' or 'Revolut', depending on the bank you want to process the statement for. </br>
The statement_file_path parameter should be the path to the PDF file of the bank statement you wish to read.</br></br>

<b>Example</b>
</br>
<pre>
  <code>python main.py 'Monzo' 'C:/path/to/monzo_statement.pdf'</code>
</pre>

The script will process the specified Monzo statement PDF file and output an array with a code and the transactions in a JSON format:

<pre>
  <code>[0, [{'date': datetime.date(2023, 6, 4), 'desc': 'Payment from User Test', 'amount': '100.00', 'is_expense': False},{'date': datetime.date(2023, 6, 10), 'desc': 'Supermarket X', 'amount': '4.50', 'is_expense': True}]]</code>
</pre>

<h3>Support</h3>
Currently, ConvertBankStatement supports the following banks:</br></br>
Monzo </br>
Revolut

<h3>Limitations</h3>
HSBC statements are not accepted as the PDFs are encrypted.


<h3>License</h3>
ConvertBankStatement is licensed under the GNU License.
