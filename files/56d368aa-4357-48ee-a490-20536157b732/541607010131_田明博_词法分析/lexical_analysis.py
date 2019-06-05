lexical_analysis = [{'begin': '1'}, {'if': '2'}, {'then': '3'}, {'while': '4'}, {'do': '5'}, {'end': '6'},
                    {'letter': '7'}, {'digit': '8'}, {'+': '13'}, {'-': '14'}, {'*': '15'}, {'/': '16'}, {':': '17'},
                    {':=': '18'}, {'<': '20'}, {'<>': '21'}, {'<=': '22'}, {'>': '23'}, {'>=': '24'}, {'=': '25'},
                    {';': '26'}, {'(': '27'}, {')': '28'}, {'#': '0'}]  # 词法分析种别码


def get_syn(str):  # 得到种别码
    for i in lexical_analysis:
        for k, v in i.items():
            if str == k:
                return v, str
    if str.isalpha() or str[0].isalpha() and str[1:].isdigit():
        return str, 10
    another = []
    for next in str:
        if next.isdigit():
            temp = (next, 11)
            another.append(temp)
        elif next == '+':
            temp = (next, 13)
            another.append(temp)
        elif next == '-':
            temp = (next, 14)
            another.append(temp)
        elif next == '*':
            temp = (next, 15)
            another.append(temp)
        elif next == '/':
            temp = (next, 16)
            another.append(temp)
        elif next == ':':
            temp = (next, 17)
            another.append(temp)
        elif next == ':=':
            temp = (next, 18)
            another.append(temp)
        elif next == '<':
            temp = (next, 20)
            another.append(temp)
        elif next == '<>':
            temp = (next, 21)
            another.append(temp)
        elif next == '<=':
            temp = (next, 22)
            another.append(temp)
        elif next == '>':
            temp = (next, 23)
            another.append(temp)
        elif next == '>=':
            temp = (next, 24)
            another.append(temp)
        elif next == '=':
            temp = (next, 25)
            another.append(temp)
        elif next == ';':
            temp = (next, 26)
            another.append(temp)
        elif next == '(':
            temp = (next, 27)
            another.append(temp)
        elif next == ')':
            temp = (next, 28)
            another.append(temp)
        else:
            temp = (next, 0)
            another.append(temp)
    return another


def show(s):  # 输出
    for i in s:
        if isinstance(i, list):
            show(i)
        else:
            print(i, end='')


if __name__ == '__main__':
    in_put = input().split()
    a = []
    for s in in_put:
        syn = get_syn(s)
        a.append(syn)
    show(a)
