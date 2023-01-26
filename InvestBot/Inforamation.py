from PriceAndDeltaPrice import price_now
def my_self_sort(file,user_id):
    right = -1
    a = ""
    m = 0
    p = 0
    for i in range(0, 100):
        try:
            l = file['USERS'][i][str(user_id)]
            right = i
            break
        except:
            pass
    if right == -1 or file['USERS'][i][str(user_id)] == [{}]:
        a = "Ваш портфель пока пуст"
        return a
    else:

            for i in file['USERS'][right][str(user_id)]:
                try:
                    a = a + '<b>' + i['ticker'] + '</b>' + '\n'
                    b = float(price_now(i['ticker'])) * int(i['kol_vo'])
                    c = float(i['price']) * float(i['kol_vo'])
                    x = int(i['kol_vo'])
                    if int(i['kol_vo']) > 0:
                        a = a + 'Разница: <b>' + str(int(b - c)) + '</b> RUB(c учётом комиссии в '+ i['commision']+'%: '+ str(int(b - (c/100*(100+float(i["commision"])))))+')' + '\n'
                    else:
                        a = a + 'Разница: <b>' + str(int(b - c)) + '</b> RUB(c учётом комиссии '+ i['commision']+'%: ' + str(
                            int(b - (c / 100 * (100 - float(i["commision"]))))) + ')' + '\n'
                    a = a + 'Стоимость актива: <b>' + str(int(b)) + '</b> RUB(' + str(x) +" шт.)"+"\n"

                    p = p + int(b - c)
                except:
                    pass
            a = a + "\nВаш суммарный доход составляет: <b>" + str(p)+'</b>'
            return a

