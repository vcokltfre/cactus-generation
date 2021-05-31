from cactusgen.jrandom import Random


class CactusSim:
    def __init__(self, count, floorLevel):
        self.heightMap = [floorLevel for i in range(32**2)]

        self.count = count
        self.floorLevel = floorLevel

        self.currentHighestPos = 0

    def populate(self, seed):
        random = Random(seed ^ 0x5DEECE66D)

        for i in range(self.count):
            initialPosX = random.nextInt(16) + 8
            initialPosZ = random.nextInt(16) + 8
            terrainHeight = (self.heightMap[initialPosX + initialPosZ * 32] + 1) * 2

            if terrainHeight > 0:
                initialPosY = random.nextInt(terrainHeight)
                self.generateCactus(random, initialPosX, initialPosY, initialPosZ)

        return self.heightMap[self.currentHighestPos] - self.floorLevel

    def generateCactus(self, random, initialPosX, initialPosY, initialPosZ):
        for i in range(10):
            posX = initialPosX + random.nextInt(8) - random.nextInt(8)
            posY = initialPosY + random.nextInt(4) - random.nextInt(4)
            posZ = initialPosZ + random.nextInt(8) - random.nextInt(8)

            if not self.isAir(posX, posY, posZ):
                continue

            offset = 1 + random.nextInt(random.nextInt(3) + 1)
            posMap = posX + posZ * 32

            for j in range(offset):
                if self.isAir(posX, posY + j - 1, posZ):
                    continue
                if not self.isAir(posX + 1, posY + j, posZ):
                    continue
                if not self.isAir(posX - 1, posY + j, posZ):
                    continue
                if not self.isAir(posX, posY + j, posZ + 1):
                    continue
                if not self.isAir(posX, posY + j, posZ - 1):
                    continue

                self.heightMap[posMap] += 1

                if self.heightMap[self.currentHighestPos] < self.heightMap[posMap]:
                    self.currentHighestPos = posMap

    def isAir(self, x, y, z):
        height = self.heightMap[x + z * 32]
        return y > height or y < 0

def generate(seed, floorlevel=63):
    desert = 10
    test = CactusSim(desert, floorlevel)
    cactusheight = test.populate(seed)
    return cactusheight
