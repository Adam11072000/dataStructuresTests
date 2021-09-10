import sys


def unionLablDictionaries(dec1, dec2):
    for i in dec1.keys():
        if i in dec2.keys():
            dec1[i] = dec1[i] + dec2[i]
            dec2.pop(i)
    for i in dec2.keys():
        dec1[i] = dec2[i]


def emptyPixels(pixels):
    dic = list()
    for i in range(0, pixels):
        dic.append([{i}, dict()])
    return dic


def findSuperPixel(superPixelsList, pixel):
    for i in range(0, len(superPixelsList)):
        if pixel in superPixelsList[i][0]:
            return i


def sortLabels(labels):
    labelsList = sorted(labels.items(), key=lambda kv: [kv[1], kv[0]], reverse=True)
    labelsOut = dict()
    for keyVal in labelsList:
        labelsOut[keyVal[0]] = keyVal[1]
    return labelsOut


class Image:
    def __init__(self, pixels):
        self.pixels = pixels
        self.superPixelList = emptyPixels(pixels) #list

    def setLabelScore(self, pixel, label, score):
        if pixel < 0 or pixel >= self.pixels or label <= 0 or score <= 0:
            return "setLabelScore: INVALID_INPUT"
        self.superPixelList[findSuperPixel(self.superPixelList, pixel)][1][label] = score
        return "setLabelScore: SUCCESS"

    def resetLabelScore(self, pixel, label):
        if pixel < 0 or pixel >= self.pixels or label <= 0:
            return "resetLabelScore: INVALID_INPUT"
        if label not in self.superPixelList[findSuperPixel(self.superPixelList, pixel)][1]:
            return "resetLabelScore: FAILURE"
        self.superPixelList[findSuperPixel(self.superPixelList, pixel)][1].pop(label)
        return "resetLabelScore: SUCCESS"

    def getHighestScoredLabel(self, pixel):
        if pixel < 0 or pixel >= self.pixels:
            return "getHighestScoredLabel: INVALID_INPUT"
        if len(self.superPixelList[findSuperPixel(self.superPixelList, pixel)][1]) == 0:
            return "getHighestScoredLabel: FAILURE"
        return "getHighestScoredLabel: %s" \
               % (list(sortLabels(self.superPixelList[findSuperPixel(self.superPixelList, pixel)][1]).keys())[0])

    def mergeSuperPixels(self, pixel1, pixel2):
        if pixel1 < 0 or pixel1 >= self.pixels or pixel2 < 0 or pixel2 >= self.pixels:
            return "mergeSuperPixels: INVALID_INPUT"
        superPixel1 = findSuperPixel(self.superPixelList,pixel1)
        superPixel2 = findSuperPixel(self.superPixelList, pixel2)
        if superPixel1 == superPixel2:
            return "mergeSuperPixels: FAILURE"
        unionLablDictionaries(self.superPixelList[superPixel1][1], self.superPixelList[superPixel2][1])
        self.superPixelList[superPixel1][0] = self.superPixelList[superPixel1][0].union(self.superPixelList[superPixel2][0])
        self.superPixelList.remove(self.superPixelList[superPixel2])
        return "mergeSuperPixels: SUCCESS"


class ImageTagger:
    def __init__(self):
        self.pixels = 0
        self.images = dict()

    def init(self, pixels):
        self.pixels = pixels
        return "init done."

    def addImage(self, imageId):
        if imageId <= 0:
            return "addImage: INVALID_INPUT"
        if imageId in list(self.images.keys()):
            return "addImage: FAILURE"
        self.images[imageId] = Image(self.pixels)
        return "addImage: SUCCESS"

    def deleteImage(self, imageId):
        if imageId <= 0:
            return "deleteImage: INVALID_INPUT"
        if imageId not in list(self.images.keys()):
            return "deleteImage: FAILURE"
        self.images.pop(imageId)
        return "deleteImage: SUCCESS"

    def setScoreLabel(self, imageId, pixel, label, score):
        if imageId <= 0 or pixel < 0 or pixel >= self.pixels or label <= 0 or score <= 0:
            return "setLabelScore: INVALID_INPUT"
        if imageId not in list(self.images.keys()):
            return "setLabelScore: FAILURE"
        return self.images[imageId].setLabelScore(pixel, label, score)

    def resetScoreLabel(self, imageId, pixel, label):
        if imageId <= 0 or pixel < 0 or pixel >= self.pixels or label <= 0:
            return "resetLabelScore: INVALID_INPUT"
        if imageId not in list(self.images.keys()):
            return "resetLabelScore: FAILURE"
        return self.images[imageId].resetLabelScore(pixel, label)

    def getHighestScoredLabel(self, imageId, pixel):
        if imageId <= 0 or pixel < 0 or pixel >= self.pixels:
            return "getHighestScoredLabel: INVALID_INPUT"
        if imageId not in list(self.images.keys()):
            return "getHighestScoredLabel: FAILURE"
        return self.images[imageId].getHighestScoredLabel(pixel)

    def mergeSuperPixels(self, imageId, pixel1, pixel2):
        if imageId <= 0 or pixel1 < 0 or pixel1 >= self.pixels or pixel2 < 0 or pixel2 >= self.pixels:
            return "mergeSuperPixels: INVALID_INPUT"
        if imageId not in list(self.images.keys()):
            return "mergeSuperPixels: FAILURE"
        return self.images[imageId].mergeSuperPixels(pixel1, pixel2)

    def quit(self):
        return "quit done."

    def parseLine(self, line):
        if line[0] == "init":
            return self.init(int(line[1]))
        if line[0] == "addImage":
            return self.addImage(int(line[1]))
        if line[0] == "deleteImage":
            return self.deleteImage(int(line[1]))
        if line[0] == "setLabelScore":
            return self.setScoreLabel(int(line[1]), int(line[2]), int(line[3]), int(line[4]))
        if line[0] == "resetLabelScore":
            return self.resetScoreLabel(int(line[1]), int(line[2]), int(line[3]))
        if line[0] == "getHighestScoredLabel":
            return self.getHighestScoredLabel(int(line[1]), int(line[2]))
        if line[0] == "mergeSuperPixels":
            return self.mergeSuperPixels(int(line[1]), int(line[2]), int(line[3]))
        if line[0] == "quit":
            return self.quit()

def main():
    in_file = open(sys.argv[1], 'r')
    lines = in_file.readlines()
    in_file.close()
    out_file = open(sys.argv[2], 'w')
    ds = ImageTagger()
    for line in lines:
        parsed = ds.parseLine(line.split())
        out_file.write(parsed + '\n')
    out_file.close()


if __name__ == "__main__":
    # execute only if run as a script
    main()
