class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        max_b = blocks[:k].count("B")

        for i in range(0, len(blocks)-k):
            count_b = blocks[i:i+k].count("B")
            
            max_b = max(max_b, count_b)

        return k-max_b


            
