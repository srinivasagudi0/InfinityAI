import re
from html import unescape

CANVAS_RE = re.compile(
    r"<CANVAS(?P<attrs>[^>]*)>(?P<content>.*?)</CANVAS>",
    re.DOTALL | re.IGNORECASE,
)

ATTR_RE = re.compile(r'(\w+)="([^"]*)"')


def parse_attrs(stuff):
    return {
        key.lower(): unescape(value.strip())
        for key, value in ATTR_RE.findall(stuff)
    }


def detect_canvas(text):
    match = CANVAS_RE.search(text)

    if match:
        attrs = parse_attrs(match.group("attrs"))
        chat_text = (text[:match.start()] + text[match.end():]).strip()

        return {
            "active": True,
            "chat": chat_text or "I created it in the canvas.",
            "title": attrs.get("title", "Canvas"),
            "kind": attrs.get("type", "document"),
            "lang": attrs.get("lang", "markdown"),
            "content": match.group("content").strip(),
        }

    code_match = re.search(
        r"```(?P<lang>[a-zA-Z0-9_+-]*)\s*\n(?P<content>.*?)```",
        text,
        re.DOTALL,
    )

    if code_match:
        lang = code_match.group("lang") or "plaintext"

        return {
            "active": True,
            "chat": text,
            "title": f"{lang.title()} Code",
            "kind": "code",
            "lang": lang,
            "content": code_match.group("content").strip(),
        }

    return {
        "active": False,
        "chat": text,
        "title": "",
        "kind": "",
        "lang": "",
        "content": "",
    }

# should add logging if possiblee