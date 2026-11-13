import MGLensing
import os 

folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)



MGLtest = MGLensing.MGL("ini_files/config_files/config_desy3_bacco_cuillin.yaml")
MGLtest.test()

