# small script to single out timepoints of videos for ilastik
from ij.io import OpenDialog, Opener, DirectoryChooser
from ij.plugin import ChannelSplitter, SubstackMaker
from ij import IJ
from os import path

# split timepoints as 3D images and save

def saveIndividualTimePoints(inputImp, outputFolder):
    imp = inputImp
    width, height, nChannels, nSlices, nFrames = imp.getDimensions()
    print nSlices
   
    for f in range(nFrames):
        print "frame: ", f
        minSlice = (f*nSlices)+1
        maxSlice = (f+1)*(nSlices)
        slices = str(minSlice) + "-" + str(maxSlice)
        print "Isolating slices ",slices
        subStack = SubstackMaker().makeSubstack(imp, slices)

        name = "t"+ str(f) + ".tif"
        IJ.save(subStack, path.join(outputFolder, name) )
        imp.close()

#--- MAIN ---
p = OpenDialog("Choose input file").getPath()
inputImp = Opener().openImage(p) # or Bioformats importer
#inputImp.show()
outputDir = DirectoryChooser("Choose output dir").getDirectory()
ch = ChannelSplitter().split(inputImp)[1]
saveIndividualTimePoints(ch, outputDir)