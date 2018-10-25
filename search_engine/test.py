def test(t):
    return [t*10,True]

dic = {'one':test(2)}
print(type(dic['one']))
if isinstance(dic['one'], list):
    print('hello')
