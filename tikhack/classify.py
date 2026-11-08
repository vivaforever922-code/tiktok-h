"""Classification des réponses. L'ordre des tests fait partie de la correction."""
from __future__ import annotations

from .models import Verdict

SUCCESS = ("success",)
THROTTLE = (
    "too many attempts",
    "maximum number of attempts",
    "try again in 24 hours",
    "trop de tentatives",
)
CAPTCHA = ("verify", "captcha", "slider")
BLOCK = ("unusual traffic", "access denied", "forbidden")
UNKNOWN_USER = (
    "couldn't find your account",
    "couldn't find this account",
    "user not found",
    "no account",
)
INVALID = (
    "incorrect password",
    "wrong password",
    "mot de passe incorrect",
    "password is incorrect",
)

CAPTCHA_SEL = (
    "#captcha_container",
    ".captcha_verify_container",
    "div[id*='captcha']",
    "iframe[src*='captcha']",
)


def _hit(low: str, needles) -> bool:
    return any(n in low for n in needles)


def classify_message(message: str, status_code: int = 0) -> Verdict:
    low = (message or "").lower()
    if status_code == 0 and _hit(low, SUCCESS):
        return Verdict.SUCCESS
    if _hit(low, THROTTLE):
        return Verdict.THROTTLED
    if _hit(low, CAPTCHA):
        return Verdict.CAPTCHA
    if _hit(low, BLOCK):
        return Verdict.BLOCKED
    if _hit(low, UNKNOWN_USER):
        return Verdict.USER_UNKNOWN
    if _hit(low, INVALID):
        return Verdict.INVALID
    return Verdict.ERROR


def classify_page(page_src: str, cookies: list[dict], captcha_present: bool) -> Verdict:
    if captcha_present:
        return Verdict.CAPTCHA
    low = (page_src or "").lower()
    names = {c.get("name") for c in (cookies or [])}
    if "sessionid" in names:
        return Verdict.SUCCESS
    if _hit(low, UNKNOWN_USER):
        return Verdict.USER_UNKNOWN
    if _hit(low, THROTTLE):
        return Verdict.THROTTLED
    if _hit(low, BLOCK):
        return Verdict.BLOCKED
    if _hit(low, INVALID):
        return Verdict.INVALID
    return Verdict.ERROR