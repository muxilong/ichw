#!/usr/bin/env python3

"""exchange.py: To tell how much you will receive
when you exchange one currency with another

__author__ = "Muxilong"
__pkuid__  = "1800011745"
__email__  = "1800011745@pku.edu.cn"
"""


def f1(currency_1, currency_2, amount):
    return ('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' +
            currency_1 + '&to=' + currency_2 + '&amt='+str(amount))


def test_f1():
    bytes_ = f1('USD', 'EUR', '2.5')
    assert bytes_ == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5'


def f2(URL):
    from urllib.request import urlopen

    doc = urlopen(URL)
    docstr = doc.read()
    doc.close()
    jsonstr = docstr.decode('ascii')
    return (jsonstr)


def test_f2():
    jsonstr = f2('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    assert jsonstr == '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'


def f3(jsonstr):
    jsonstr = jsonstr.replace(":", ",")
    jsonlist_0 = jsonstr.split(',')
    str_0 = jsonlist_0[3]
    str_0 = str_0.strip('" ')
    jsonlist = str_0.split()
    number = float(jsonlist[0])
    return number


def test_f3():
    number = f3('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')
    assert number == 2.1589225


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    bytes_ = f1(currency_from, currency_to, amount_from)
    jsonstr = f2(bytes_)
    number = f3(jsonstr)
    return number


def test_exchange():
    number = exchange('USD', 'EUR', 2.5)
    assert number == 2.1589225


def test_all():
    test_f1()
    test_f2()
    test_f3()
    test_exchange()
    print('All tests passed')


if __name__ == '__main__':
    currency_from = input('输入原货币名称')
    currency_to = input('输入目标货币名称')
    amount_from = input('输入原货币数额')
    test_all()
    print(exchange(currency_from, currency_to, amount_from))
