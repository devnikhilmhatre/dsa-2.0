from dataclasses import dataclass
from typing import Optional


@dataclass
class Data:
    id: int


@dataclass
class SingleNode:
    data: Data
    next: Optional["SingleNode"] = None


@dataclass
class DoubleNode:
    data: Data
    next: Optional["DoubleNode"] = None
    prev: Optional["DoubleNode"] = None
