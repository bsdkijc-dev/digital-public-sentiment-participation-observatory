import re

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
NIK_RE = re.compile(r"\b\d{16}\b")
PHONE_RE = re.compile(r"(?:\+62|62|0)8[1-9][0-9\-\s]{7,12}\b")
HANDLE_RE = re.compile(r"(?<!\w)@[A-Za-z0-9_.-]{2,30}")


def scrub_pii(text: str) -> str:
    """Redact emails, 16-digit NIKs, Indonesian mobile numbers, and @handles."""
    if not text:
        return ""
    cleaned = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    cleaned = NIK_RE.sub("[REDACTED_NIK]", cleaned)
    cleaned = PHONE_RE.sub("[REDACTED_PHONE]", cleaned)
    cleaned = HANDLE_RE.sub("[REDACTED_HANDLE]", cleaned)
    return cleaned.strip()


def contains_pii(text: str) -> bool:
    """Return True if any deterministic PII pattern is detected."""
    if not text:
        return False
    return bool(
        EMAIL_RE.search(text)
        or NIK_RE.search(text)
        or PHONE_RE.search(text)
        or HANDLE_RE.search(text)
    )
