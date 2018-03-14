# -*- coding: utf-8 -*-


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


# L = MyList()
# print(L)

# L.add(1)
# print(L)


# class User(Model):
#     # 定义类的属性到列的映射：
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')


# # 创建一个实例：
# u = User(id=12345, name='Micheal', email='test@orm.org', password='my-pwd')
# u.save()