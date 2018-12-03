"""currency.py: Exchange between different foreign currencies.

__author__ ="陈新杨"
__pkuid__  ="1800011830"
__email__  ="1800011830@pku.edu.cn"
"""


from urllib.request import urlopen
import re

determ, amount_to,has_error = 0,0,0
def get_information(jstr):
    """从字典中提取信息
    """
    global determ = jstr["success"]
    global amount_to = jstr["to"]
    global has_error = jstr["error"]
    return(determ,amount_to,has_error)

def test_A():
    assert(get_from({ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }\
    ==true,"2.24075 Euros",""))

def get_from(currency_from,currency_to,amount_from):
    """从网页上获取字节流,进行兑换,得到字典
    """
	  doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='\
    +currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

def test_B():
    """测试得到的字典的值
    """
    assert(def exchage(USD,EUR,2.5)==\
    { "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" })

currency_from = input("currency_from:")
currency_to = input("currency_to:")
amount_from = input("amount_from:")
def Exchange(currency_from,currency_to,amount_from):
    """进行货币兑换
    """
    jstr = get_from(currency_from,currency_to,amount_from)
    get_information(jstr)
    ###判断兑换能否进行
    if determ == true:
        amount_to = float(re.findall(r"\d+\.?\d*",amount_to))
        return(amount_to)
    else:
        return(has_error)

print(Exchange(currency_from,currency_to,amount_from))

def test_C:
    assert(Exchange(USD,EUR,2.5)==2.24075)
    assert(Exchange(BSD,CAD,1)==1.300473)
    assert(Exchange(ABC,BTC,2)=="Source currency code is invalid.")

def testAll()
    """测试所有函数
    """
    test_A()
    test_B()
    test_C()
    print("All tests passed")

if __name__ == '__main__':
    main()
