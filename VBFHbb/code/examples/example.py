# run this from the command line using: python -i example.py 
# flag "-i" is for interactive mode, without it will exit the python interpret as soon as the execution of the example.py script finished
import ROOT as rt

# file pointer to the root file, root file has to be in the same folder as the example.py
fp = rt.TFile.Open("VBFHToBB.root", "READ") 

# get the TTree object stored in fp, tree = the name of the TTree object
mytree = fp.Get("events")

# show first entry, counter starts at 0
mytree.Show(0) 

# make a ROOT histogram (1-D float i.e., TH1F), with 100 bins for the interval [0,1000] 
myhisto = rt.TH1F("myhisto","mytitle; MET [GeV]; #events",20,0,100) 


# fill histogram using TTree.Draw() method
mytree.Draw("met>>myhisto", "", "goff")
# met is the variable of the TTree to be "drawn", ">>" is an operator indicating on the right the name of the histogram
# "" is reserved for applying selection, empty string ""-> means no selection, try to replace "" with "met>30" 
# "goff" is to ask ROOT to not try to open graphic display interactively, try later to replace "goff" with ""
# met = missing transverse energy found in the event (e.g., due to escaping from detection neutrinos)

# make TCanvas object to draw on it, e.g., histograms
mycanvas = rt.TCanvas("c1","c1")
myhisto.Draw()

# save the figure as png and as pdf
mycanvas.SaveAs("fig.png")
mycanvas.SaveAs("fig.pdf")

# next step: try to make the y-axis scale logarithmic

