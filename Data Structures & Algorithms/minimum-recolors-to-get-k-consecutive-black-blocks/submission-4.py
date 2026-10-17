class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count("W")

        for i in range(0, len(blocks)-k):
            count_b = blocks[i:i+k].count("W")
            
            white = min(white, count_b)

        return white


            
