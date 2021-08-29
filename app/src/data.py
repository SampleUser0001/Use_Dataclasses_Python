# -*- coding: utf-8 -*-
import dataclasses

@dataclasses.dataclass
class User:
  name: str
  age: int = 0