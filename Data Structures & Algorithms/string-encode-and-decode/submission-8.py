class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word))
            encoded += "#"
            encoded += word

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            count = 0

            while s[i] != "#":
                count *= 10
                count += int(s[i])
                i += 1

            if s[i] == "#":
                i += 1

                decoded.append(s[i:i+count])
                i += count

        return decoded
