def outor():
    print('inside outer')

    def inner():
       print('inside inner')

    return inner

reasult = outor()
reasult()