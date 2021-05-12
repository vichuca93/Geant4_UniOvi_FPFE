

import ROOT as r

# Open rootfile
f = r.TFile.Open("YourApplication.root")

# Get the directory as a tree
t = f.Get("histograms")

# Get the histograms
edep = t.Get("Edep")
trackL = t.Get("trackL")


# -----------------------------------------------------
# Creamos el Canvas
c = r.TCanvas("c", "Si_elec_100MeV_22.4um", 20, 20, 1000, 1000)

c.Divide(1, 2) 

c.cd(1)
edep.Draw("hist")
edep.SaveAs("./histogramas/Si_elec_100MeV_22.4um_edep.xlsx")

c.cd(2)
trackL.Draw("hist")
edep.SaveAs("./histogramas/Si_elec_100MeV_22.4um_trackL.xlsx")

c.Print("./histogramas/Si_elec_100MeV_22.4um.png", "png")

out = r.TFile("./histogramas/Si_elec_100MeV_22.4um.root", "recreate")
c.Write()
