import datetime
from bank_statement import BankStatement
from utils import get_until_char, get_month, get_pay_to_from


class RevolutStatement(BankStatement):

    def get_trx(self, text):
        string_start = 'Date Description Money out Money in Balance'
        start = text.find(string_start)
        # Revolut's statements needs to be delimitated and the end only in the first page
        # and the delimitation is the account Address, Ex: Flat X, Xxx Yyy
        end = -1
        if self.page_number == 0:
            lines = text.split('\n')
            end = text.find(lines[-14])
        result = text[start:end].replace(string_start, '').replace('\n', '', 1)
        return result

    def get_full_trx_line(self, trx_lines):
        full_line = ''
        is_expense = True
        for i in range(3):
            if len(trx_lines) <= i:
                break

            line = trx_lines[i]
            if line[0].isdigit():
                full_line += line

            if trx_lines[i].startswith('From:'):
                is_expense = False
                break

        return full_line, is_expense

    def split_transactions(self, transactions):
        trx_lines_aux = []
        trx_lines = transactions.split('\n')
        while len(trx_lines) > 0:
            if trx_lines[0].strip() == '':
                trx_lines.pop(0)
                continue

            delete = 3
            line, is_expense = self.get_full_trx_line(trx_lines)
            if is_expense:
                trx_lines_aux.append('-' + line)
            else:
                if line.strip() != '':
                    trx_lines_aux.append('+' + line)
                delete = 2

            for i in range(delete):
                if len(trx_lines) > 0:
                    trx_lines.pop(0)

        result = []
        for i in range(len(trx_lines_aux)):
            line = trx_lines_aux[i]
            if line.strip() == '' or line == '\n' or line == '-':
                break
            is_expense = line[0] == '-'
            line = line[1:len(line)]
            day, line = get_until_char(line, ' ')

            month_str, line = get_until_char(line, ' ')
            month = get_month(month_str)
            year, line = get_until_char(line, ' ')
            date_trx = datetime.date(int(year), int(month), int(day))
            to_from, line = get_pay_to_from(line, '£')
            amount, line = get_until_char(line, ' ')
            x = {
                'date': date_trx,
                'to_from': to_from.lstrip(),
                'amount': amount.replace('£', '').replace(',', ''),
                'is_expense': is_expense
            }
            result.append(x)

        return result
