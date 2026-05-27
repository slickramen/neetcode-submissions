class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        index = 0
        decoded = []
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])

            word = s[j + 1 : j + length + 1]
            decoded.append(word)
            index = j + length + 1

        return decoded



