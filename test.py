# from loader import db


# user_id = 875587704
# country = 'Uzbekistan'
# place = 'Tashkent'


# # db.reg_country(user_id, country, place)
# # db.del_country(user_id, country)


# user_id = 6737735
# country = 'USA'
# place = 'New-York'


# # db.reg_country(user_id, country, place)
# # db.del_country(user_id, country)

class A:
    def _single_method(self):
        print('_single_method')
    def __double_method(self): # for mangling
        print('__double_method')


class B(A):
    def __double_method(self): # for mangling
        print('__double_method from inherit')


a = A()
a._single_method()

b = B()
# b.__double_method()