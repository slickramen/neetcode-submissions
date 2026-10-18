class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1

        gc = instructions.count("G")
        reps = 10

        for j in range(reps):
            for ins in instructions:
                if ins == "G":
                    x += dx
                    y += dy
                elif ins == "L":
                    dx, dy = -dy, dx
                elif ins == "R":
                    dx, dy = dy, -dx
        
        if abs(x) <= gc and abs(y) <= gc:
            return True
        else:
            return False
            
            

