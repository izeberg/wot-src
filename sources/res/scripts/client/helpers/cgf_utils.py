

def toggleCgfComponent(go, componentType, enable, *componentArgs):
    component = go.findComponentByType(componentType)
    if enable:
        if component is None:
            go.createComponent(componentType, *componentArgs)
    elif component is not None:
        go.removeComponentByType(componentType)
    return