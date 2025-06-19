
def loadfb(data):
    with open(data, "r") as FBR:
        return FBR.readlines()

###############


def savefb(data, fblist):
    with open(data, "w") as FBM:
        for fb in fblist:
            FBM.writelines(fb + "\n")

if __name__ == "__main__":
    from Core_Feedback_Management_System import mainapp
    data_file = "C:/PyStuff/Brain360/examples/from_ahmed/Core_Feedback_Management_System/Feedback_list.txt"
    testlist = []
    loadfb(data_file)
    mainapp()
    savefb(data_file, testlist)