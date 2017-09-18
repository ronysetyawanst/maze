import math

class Maze:
    def __init__(self, sizeMaze=None):
        self.sizeMaze = sizeMaze
        
    def setSizeMaze(self, sizeInput):
        self.sizeMaze = (4*sizeInput)-1
        
    def getSizeMaze(self):
        return self.sizeMaze
        
    def getPatternOne(self):
        sizeMaze = self.getSizeMaze()
        for loopY in range(sizeMaze):
            mazeX = ""
            if ((loopY%4)==0):
                for loopX in range(sizeMaze):
                    if (loopX==1):
                        mazeX = mazeX+" "+" "
                    else:
                        mazeX = mazeX+" "+"@"
            elif ((loopY%2)==1):
                for loopX in range(sizeMaze):
                    if (loopX==0):
                        mazeX = mazeX+" "+"@"
                    elif (loopX==(sizeMaze-1)):
                        mazeX = mazeX+" "+"@"
                    else:
                        mazeX = mazeX+" "+" "
            elif (((loopY+2)%4)==0):
                for loopX in range(sizeMaze):
                    if (loopX==(sizeMaze-2)):
                        mazeX = mazeX+" "+" "
                    else:
                        mazeX = mazeX+" "+ "@"
            print(mazeX+"\n")
                
    def getPatternTwo(self):
        sizeMaze = self.getSizeMaze()
        centerY = math.floor(sizeMaze/2)
        for loopY in range(sizeMaze):
            mazeX = ""
            if(loopY==centerY):
                for loopX in range(sizeMaze):
                    if(loopX%2==0):
                        mazeX = mazeX+" "+"@"
                    else:
                        mazeX = mazeX+" "+" "
            else:
                for loopX in range(sizeMaze):
                    if((loopY<centerY) and ((loopX>=(loopY+3)) and (loopX<=(sizeMaze-(loopY+1))))):
                        if(loopY%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    elif((loopY>centerY) and ((loopX>=(sizeMaze-(loopY+1))) and (loopX<=(loopY)))):
                        if(loopY%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    else:
                        if(loopX%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
            print(mazeX+"\n")
    
    def getPatternThree(self):
        sizeMaze = self.getSizeMaze()
        centerY = math.floor(sizeMaze/2)
        for loopY in range(sizeMaze):
            mazeX = ""
            if(loopY==centerY):
                for loopX in range(sizeMaze):
                    if(loopX%2==0):
                        mazeX = mazeX+" "+"@"
                    else:
                        mazeX = mazeX+" "+" "
            else:
                for loopX in range(sizeMaze):
                    if((loopY<centerY) and ((loopX>=(loopY+3)) and (loopX<=(sizeMaze-(loopY+1))))):
                        if(loopY%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    elif((loopY>centerY) and ((loopX>=(sizeMaze-(loopY+1))) and (loopX<=(loopY-2)))):
                        if(loopY%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    else:
                        if(loopX%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
            print(mazeX+"\n")
            
    def getPatternFour(self):
        sizeMaze = self.getSizeMaze()
        for loopY in range(sizeMaze):
            mazeX = ""
            for loopX in range(sizeMaze):
                if(loopY==0):
                    if(loopX==1):
                        mazeX = mazeX+" "+" "
                    else:
                        mazeX = mazeX+" "+"@"
                elif(loopY==1):
                    if(loopX>0):
                        if((loopX+2)%4==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    else:
                        if(loopX%4==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                else:
                    if((loopX>=(sizeMaze-(loopY+1))) and (loopX<=(sizeMaze-2))):
                        if(loopY%2==0):
                            if((loopY%4==0) and (loopX==(sizeMaze-2))):
                                mazeX = mazeX+" "+" "
                            else:
                                mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
                    else:
                        if(loopX%2==0):
                            mazeX = mazeX+" "+"@"
                        else:
                            mazeX = mazeX+" "+" "
            print(mazeX+"\n")
 
def main():
    sizeInput= int(input("Please Enter Your Size(Positive Number) of the Maze Which You Want to Generate(example => 2) : "))
    maze = Maze()
    maze.setSizeMaze(sizeInput)
    maze.getPatternOne()
    maze.getPatternTwo()
    maze.getPatternThree()
    maze.getPatternFour()
    
if __name__ == '__main__':
    main()
