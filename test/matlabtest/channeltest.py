from mat.MatalbClient import *
from mat.WorkingDirectory import changeDirectory

changeDirectory("F:\wpcn-full-duplex\mat")

client = MatlabClient()

H = client.InitChannel(2,2)
print H

St = client.BeamInit(H)
print St
