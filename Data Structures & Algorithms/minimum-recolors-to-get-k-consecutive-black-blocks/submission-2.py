class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_b = 0
        max_b = 0

        count_b = blocks[:k].count("B")
        max_b = count_b

        for i in range(0, len(blocks)-k):
            if blocks[i+k] == "B":
                count_b += 1

            if blocks[i] == "B":
                count_b -= 1
            
            max_b = max(max_b, count_b)

        return k-max_b


            
