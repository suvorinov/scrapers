# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-12-21 09:30:05
# @Last Modified by:   suvorinov
# @Last Modified time: 2024-01-05 10:21:48

from typing import List
from datetime import datetime
from dataclasses import dataclass, field

now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")


@dataclass
class Proxy:
    scheme: str = field(default='http')
    host: str = field(default='')
    port: int = field(default=80)
    export_address: List[str] = field(default_factory=list)
    anonymity: str = field(default='transparent')
    country: str = field(default='US')
    response_time: float = field(default=0.0)
    to_from: str = field(default='')
    last_checked: str = field(default=now)
