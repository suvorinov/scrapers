# -*- coding: utf-8 -*-
# @Author: suvorinov
# @Date:   2023-12-21 09:30:05
# @Last Modified by:   Suvorinov Oleg
# @Last Modified time: 2024-01-08 07:32:52

from typing import List
from datetime import datetime
from dataclasses import dataclass, field

now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")


@dataclass
class Proxy:
    host: str = field(default='')
    port: int = field(default=80)
    anonymity: str = field(default='transparent')
    country: str = field(default='US')
    response_time: float = field(default=0.0)
    to_from: str = field(default='')
    last_checked: str = field(default=now)
