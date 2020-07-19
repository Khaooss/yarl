from typing import overload, Any, Tuple, Optional, Mapping, Union, Sequence, Type
from typing_extensions import TypedDict
import multidict
from functools import _CacheInfo

_QueryVariable = Union[str, int]
_Query = Union[
    None, str, Mapping[str, _QueryVariable], Sequence[Tuple[str, _QueryVariable]]
]

class URL:
    scheme: str
    raw_user: str
    user: Optional[str]
    raw_password: Optional[str]
    password: Optional[str]
    raw_host: Optional[str]
    host: Optional[str]
    port: Optional[int]
    raw_path: str
    path: str
    raw_query_string: str
    query_string: str
    path_qs: str
    raw_path_qs: str
    raw_fragment: str
    fragment: str
    query: multidict.MultiDict[str]
    raw_name: str
    name: str
    raw_parts: Tuple[str, ...]
    parts: Tuple[str, ...]
    parent: URL
    def __init__(
        self, val: Union[str, "URL"] = ..., *, encoded: bool = ...
    ) -> None: ...
    @classmethod
    def build(
        cls,
        *,
        scheme: str = ...,
        user: Optional[str] = ...,
        password: Optional[str] = ...,
        host: str = ...,
        port: Optional[int] = ...,
        path: str = ...,
        query: Optional[_Query] = ...,
        query_string: str = ...,
        fragment: str = ...,
        encoded: bool = ...
    ) -> URL: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __truediv__(self, name: str) -> URL: ...
    def __mod__(self, query: _Query) -> URL: ...
    def is_absolute(self) -> bool: ...
    def is_default_port(self) -> bool: ...
    def origin(self) -> URL: ...
    def relative(self) -> URL: ...
    def with_scheme(self, scheme: str) -> URL: ...
    def with_user(self, user: Optional[str]) -> URL: ...
    def with_password(self, password: Optional[str]) -> URL: ...
    def with_host(self, host: str) -> URL: ...
    def with_port(self, port: Optional[int]) -> URL: ...
    def with_path(self, path: str, *, encoded: bool = ...) -> URL: ...
    @overload
    def with_query(self, query: _Query) -> URL: ...
    @overload
    def with_query(self, **kwargs: _QueryVariable) -> URL: ...
    @overload
    def update_query(self, query: _Query) -> URL: ...
    @overload
    def update_query(self, **kwargs: _QueryVariable) -> URL: ...
    def with_fragment(self, fragment: Optional[str]) -> URL: ...
    def with_name(self, name: str) -> URL: ...
    def join(self, url: URL) -> URL: ...
    def human_repr(self) -> str: ...
    # private API
    @classmethod
    def _normalize_path(cls, path: str) -> str: ...

class cached_property:
    def __init__(self, wrapped: Any) -> None: ...
    def __get__(self, inst: URL, owner: Type[URL]) -> Any: ...
    def __set__(self, inst: URL, value: Any) -> None: ...

class CacheInfo(TypedDict):
    idna_encode: _CacheInfo
    idna_decode: _CacheInfo

def cache_clear() -> None: ...
def cache_info() -> CacheInfo: ...
def cache_configure(
    *, idna_encode_size: Optional[int] = ..., idna_decode_size: Optional[int] = ...
) -> None: ...
