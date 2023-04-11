import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import random
#THINGS TO DO -- put it all in a class and make it an exportable file ;)
#fix the water -- there is so much water. please fix it
# can add more lah HAHA more terrains + expandable terrians as well (e.g. village houses and stuff)

class TerrainGenerator:

    #initialization
    def __init__(self, seed):
        self.seed = seed

    #creating the perlin map itself -- specify octaves and a seed
    def createPerlin(octaves=10, seed=0):
        noise = PerlinNoise(octaves=octaves, seed=seed)
        xpix, ypix = 100, 100
        #thank you to the weird perlin documentation for giving me something so easy to copy
        pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
        plt.imshow(pic, cmap='gray')
        #uncommenting the below line will make a popup showing you the generated terrain as a funny gradient thing
        #plt.show()
        return pic


    # creating visualization file to see lines and columns of your items (individual numbers)
    def createVisualizationFile(pic, multiplier=200):
        with open("testperlinfile.txt", "w") as theFile:
            for x in range(len(pic)):
                theFile.write(f"LINE {x}\n")
                for y in range(len(pic[x])):
                    theFile.write(f"\t{y}: {pic[x][y] * multiplier}\n")
        return

    #final terrain file generation -- the main method you should use!
    def createTerrainFile(pic):
        with open("terrainGeneration.txt", "w") as theFile:
            for x in range(len(pic)):
                if x == 0 or x == len(pic) - 1:
                    for i in range(len(pic)):
                        theFile.write("X")
                    theFile.write("\n")
                    continue
                else:
                    for y in range(len(pic[x])):
                        
                        #check for first and last column
                        if y == 0 or y == len(pic[x]) - 1:
                            theFile.write("X")
                            continue

                        value = int(pic[x][y] * 200)
                        print (value)
                        if value <= -50:
                            theFile.write("W")
                        elif 25 < value < 69:
                            theFile.write("T")
                        else:
                            theFile.write("G")
                    theFile.write("\n")
        return

# i cannot find the biggest number (skill issue)
def whatTheHeckIsTheBiggestNumber(file):
    smallestNumber = 1290348710293847102893; biggestNumber = -394853948572389475
    with open(file, "r") as theFile:
        for line in theFile:
            line = line.rstrip()
            col = line.split(" ")
            if col[0] == "LINE":
                continue
            number = float(col[1])
            if number < smallestNumber:
                smallestNumber = number
            elif number > biggestNumber:
                biggestNumber = number
    return smallestNumber, biggestNumber

item = TerrainGenerator.createPerlin(seed=random.randint(0,100))
TerrainGenerator.createTerrainFile(item)