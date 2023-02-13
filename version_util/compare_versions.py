"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1
If version1 < version2 return -1
otherwise return 0

You may assume that the version strings are non-empty and contain only digits
and the 'dot' character. The 'dot' character does not represent a
decimal point and is used to separate number sequences. For instance '2.5' is
not "two and a half" or "half way to version three", it is the fifth
second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.2.9.9.9.9 < 1.3 < 1.3.4 < 1.10

1

1.2.0.0.0
1.2

- take the first subsection from each string and compare
- if one is an empty string compare the other to 0
- return 1 or -1 if not the same
- return 0 if both are empty strings
"""
from typing import Tuple

def split(s: str) -> Tuple[str,str]:
    parts = s.split(".", 1)
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[1]

def to_int(s: str) -> int:
    if s == "":
        return 0
    return int(s)

def compare(version_1: str, version_2: str) -> int:
    if version_1 == "" and version_2 == "":
        return 0
    head_1, rest_1 = split(version_1)
    head_2, rest_2 = split(version_2)
    int_1, int_2 = to_int(head_1), to_int(head_2)

    if int_1 < int_2:
        return -1
    if int_2 < int_1:
        return 1
    return compare(rest_1, rest_2)
