from __future__ import absolute_import
import typing
TData = typing.TypeVar('TData')
TDataFactory = typing.Callable[([], TData)]
TPDCVersion = typing.Tuple[(str, ...)]