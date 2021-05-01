import os

def coba(method):
    def coba(*args, **kw):
        result = method(*args, **kw)
        print(kw)
        print(args)
        return result
    return coba


@coba
def haha(x):
    return 2*10


print(haha(2))
