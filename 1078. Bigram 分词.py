import re


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        find = re.findall(fr"(?<=\b{first}{second})(\w+)",text)
        return find