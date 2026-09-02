

class AutoProperty(object):

    def __init__(self, fieldName=None):
        self.fieldName = fieldName

    def __get__(self, instance, owner=None):
        if instance is not None:
            return getattr(instance, self.fieldName, None)
        else:
            return self

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class TypedProperty(AutoProperty):

    def __init__(self, allowedType, fieldName=None):
        AutoProperty.__init__(self, fieldName)
        self.allowedType = allowedType

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)


class LinkDescriptor(AutoProperty):

    def __init__(self, fieldName=None):
        AutoProperty.__init__(self, fieldName)

    def __set__(self, instance, value):
        setattr(instance, self.fieldName, value)

    def __call__(self, *args, **kwargs):
        raise AssertionError('Never execute this, it is only for autocompletion support')


class AutoPropertyInitMetaclass(type):

    def __new__(cls, name, bases, attributes):
        for attributeName, attribute in attributes.items():
            if isinstance(attribute, AutoProperty) and attribute.fieldName is None:
                attribute.fieldName = '_%s__%s' % (name, attributeName)

        return super(AutoPropertyInitMetaclass, cls).__new__(cls, name, bases, attributes)