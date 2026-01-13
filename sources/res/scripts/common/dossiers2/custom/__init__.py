

def init():
    from dossiers2.custom.cache import buildCache
    buildCache()
    from dossiers2.custom.collector20 import loadCollector20Config
    loadCollector20Config()
    from dossiers2.custom.dependencies import init as dependencies_init
    dependencies_init()