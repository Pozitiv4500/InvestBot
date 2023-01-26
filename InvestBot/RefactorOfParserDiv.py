from PARSER_DIVIDENDOV import DIV_DAY_PLZ
from PriceAndDeltaPrice import price_now
def DIVI(a):
    a = a.upper()
    if price_now(a) == 'Неверно введён тикер акции':
         return 'Невернно введён тикер акции! Возвращаю вас в меню'

    else:
        data = DIV_DAY_PLZ(a)

        if data == []:
            return "У " + a + ' не было дивидендов! Возвращаю вас в меню'

        else:
            for i in range(0, len(data)):
                try:
                    if data[i].find('strong class="dividend_canceled"') != -1:
                        for j in range(0, 8):
                            data.pop(i - 5)
                except:
                    pass
            if data[0] == a + 'P':
                b = ''

                b = str(b)
                c = int(len(data)) // 8
                b = '<b>' + a + 'P</b>' + '\n'
                for i in range(0, c, 2):
                    b = b + data[i * 8 + 2] + ' '
                    b = b + data[i * 8 + 5] + ' RUB'
                    b = b + '\n'
                b = b + '<b>' + a + '</b>' + '\n'
                for i in range(1, c, 2):
                    b = b + data[i * 8 + 2] + ' '
                    b = b + data[i * 8 + 5] + ' RUB'
                    b = b + '\n'
            elif data[8] == a + 'P':
                b = ''

                b = str(b)
                c = int(len(data)) // 8
                b = '<b>' + a + '</b>' + '\n'
                for i in range(0, c, 2):
                    b = b + data[i * 8 + 2] + ' '
                    b = b + data[i * 8 + 5] + ' RUB'
                    b = b + '\n'
                b = b + '<b>' + a + 'P</b>' + '\n'
                for i in range(1, c, 2):
                    b = b + data[i * 8 + 2] + ' '
                    b = b + data[i * 8 + 5] + ' RUB'
                    b = b + '\n'
            else:
                b = ''

                b = str(b)
                c = int(len(data)) // 8
                b = '<b>' + a + '</b>' + '\n'
                for i in range(0, c):
                    b = b + data[i * 8 + 2] + ' '
                    b = b + data[i * 8 + 5] + ' RUB'
                    b = b + '\n'
            return b








