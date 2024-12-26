import typing
TData = typing.TypeVar('TData')
TDataFactory = typing.Callable[([], TData)]
TPDCVersion = typing.Tuple[(str, ...)]