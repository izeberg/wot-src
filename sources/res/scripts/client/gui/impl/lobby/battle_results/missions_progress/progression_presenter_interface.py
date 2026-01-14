

class IProgressionCategoryPresenter(object):

    @classmethod
    def getPathToResource(cls):
        return NotImplementedError

    @classmethod
    def getViewAlias(cls):
        return NotImplementedError