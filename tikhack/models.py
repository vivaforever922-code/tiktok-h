from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Verdict(str, Enum):
    SUCCESS = "success"
    INVALID = "invalid"
    THROTTLED = "throttled"
    CAPTCHA = "captcha"
    USER_UNKNOWN = "user_unknown"
    BLOCKED = "blocked"
    ERROR = "error"

    @property
    def fatal(self) -> bool:
        return self in (self.SUCCESS, self.USER_UNKNOWN)


@dataclass
class Attempt:
    password: str
    verdict: Verdict
    elapsed: float
    detail: str = ""
    proxy: str | None = None


@dataclass
class RunState:
    target: str
    tried: list[str] = field(default_factory=list)
    found: str | None = None
"""