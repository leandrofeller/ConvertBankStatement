import bank_statement
from monzo_statement import MonzoStatement
from revolut_statement import RevolutStatement


def convert_pdf(parameters):
    are_par_valid, bank, pdf_file = get_parameter_values(parameters)

    if not are_par_valid:
        return [-1, "Wrong number of parameters"]

    match bank:
        case 'Monzo':
            statement = MonzoStatement()
        case 'Revolut':
            statement = RevolutStatement()
        case _:
            return [-2, f'Invalid bank name. Possibible options: {bank_statement.valid_banks}']

    try:
        transactions = statement.read_pdf_statement(self=statement, pdf_file=pdf_file)
        return [0, transactions]
    except FileNotFoundError:
        return [-3, 'File not found']
    except Exception as e:
        raise e


def get_parameter_values(parameters):
    if len(parameters) < 2:
        return False, '', ''

    bank = parameters[0] if parameters[0] is not None else ''
    pdf_file = parameters[1] if parameters[1] is not None else ''
    return [True, bank, pdf_file]
