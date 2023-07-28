import datetime
from bank_statement import BankStatement
from utils import get_until_char, get_until_char_opposite, delete_non_number


class MonzoStatement(BankStatement):

    def get_trx(self, text):
        string_start = 'Date Description (GBP) Amount(GBP) Balance'
        string_end = 'Monzo Bank Limited (https://monzo.com) is a company registered in England'
        start = text.find(string_start)
        end = text.find(string_end)
        return text[start:end].replace(string_start, '').replace('\n', '', 1)

    def get_full_trx_line(self, trx_lines):
        pass

    def split_transactions(self, transactions):
        trx_lines = self.make_adjustments(transactions)
        result = []
        for i in range(len(trx_lines)):
            if not trx_lines[i][0].isdigit():
                continue

            line = trx_lines[i]
            if line == '':
                break

            day, line = get_until_char(line, '/')
            month, line = get_until_char(line, '/')
            year = line[0:4]
            line = line.replace(year, '')
            date_trx = datetime.date(int(year), int(month), int(day))
            discard, line = get_until_char_opposite(line, ' ')
            amount, line = get_until_char_opposite(line, ' ')
            amount = delete_non_number(amount)
            is_expense = amount.find('-') >= 0
            x = {
                'date': date_trx,
                'to_from': line.replace(' ', '', 1),
                'amount': amount.replace('-', '').replace(' ', '').replace(',', ''),
                'is_expense': is_expense
            }
            result.append(x)
        return result

    @staticmethod
    def make_adjustments(transactions):
        trx_lines = transactions.split('\n')
        lines_adjusted = []

        while len(trx_lines) > 0:
            line = trx_lines[0]

            if line.strip() == '':
                trx_lines.pop(0)
                continue

            trx_lines.pop(0)

            if not line[len(line) - 1].isdigit():
                line += ' ' + trx_lines[0]
                trx_lines.pop(0)

            lines_adjusted.append(line)

        return lines_adjusted
