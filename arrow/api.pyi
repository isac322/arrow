# coding: UTF-8

from datetime import tzinfo
from typing import Any, Text, Type, TypeVar, Union

from .arrow import Arrow
from .factory import ArrowFactory


# TODO
def get(*args: Any, **kwargs: Any) -> Arrow: ...


def utcnow() -> Arrow: ...


def now(tz: Union[Text, tzinfo, None] = None) -> Arrow: ...


_AT = TypeVar('_AT', bound=Arrow)


def factory(type: Type[_AT]) -> ArrowFactory: ...
