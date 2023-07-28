def get_until_char(imput, char):
    result = imput[0:imput.find(char)]
    replaced = imput.replace(result + char, '', 1)
    return result, replaced


def get_until_char_opposite(line, char):
    char_pos = line.rindex(char)
    result = line[char_pos:len(line)]
    replaced = line[0:char_pos]
    return result, replaced


def get_month(month):
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
              'Nov': 11, 'Dec': 12}
    try:
        return months[month]
    except:
        raise ValueError(-1)


def get_pay_to_from(imput, find_until):
    char_until = imput.find(find_until)
    result = imput[0:char_until-1]
    replaced = imput[char_until:len(imput)]
    return result, replaced


def delete_non_number(value):
    value = value.strip()
    while value and value[0].isalpha():
        value = value[1:len(value)]

    return value


def if_null(value, default):
    if value is not None:
        return value
    else:
        return default


