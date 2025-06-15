
#this page is weird
#this the code will call the txt file so we can modify it
def loadfb(data):
    with open(data, "r") as FBR:
        return FBR.readlines()

###############

#this code will modify it
def savefb(data, fblist):
    with open(data, "w") as FBM:
        for fb in fblist:
            FBM.writelines(fb + "\n")
