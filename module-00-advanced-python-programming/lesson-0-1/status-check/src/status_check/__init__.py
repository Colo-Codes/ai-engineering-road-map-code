import sys

import httpx


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else "https://www.python.org"
    response = httpx.get(url, follow_redirects=True, timeout=10)
    print(f"{url} -> {response.status_code} {response.reason_phrase}")
