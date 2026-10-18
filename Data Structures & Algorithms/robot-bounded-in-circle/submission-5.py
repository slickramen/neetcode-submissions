class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        posX = 0
        posY = 0
        d = 0

        gc = instructions.count("G")
        reps = 10

        for j in range(reps):
            for ins in instructions:
                if ins == "L":
                    d -= 1

                    if d < 0:
                        d += 4
                
                elif ins == "R":
                    d += 1

                    if d >= 4:
                        d -= 4

                else:
                    if d == 0:
                        posY -= 1
                    elif d == 1:
                        posX += 1
                    elif d == 2:
                        posY += 1
                    else:
                        posX -= 1
        
        if abs(posX) <= gc and abs(posY) <= gc:
            return True
        else:
            return False
            
            

