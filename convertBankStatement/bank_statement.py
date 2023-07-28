from abc import ABC, abstractmethod
import PyPDF2

valid_banks = ['Monzo', 'Revolut']


class BankStatement(ABC):
    page_number = 0

    @abstractmethod
    def get_trx(self, text):
        pass

    @abstractmethod
    def get_full_trx_line(self, trx_lines):
        pass

    @abstractmethod
    def split_transactions(self, transactions):
        pass

    @staticmethod
    def read_pdf_statement(self, pdf_file):
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            transactions = ''
            for i in range(num_pages):
                self.page_number = i
                page = pdf_reader.pages[self.page_number]
                text = page.extract_text()
                transactions += self.get_trx(text)

            transactions_arr = self.split_transactions(transactions)
            return transactions_arr
        except Exception as e:
            raise e
