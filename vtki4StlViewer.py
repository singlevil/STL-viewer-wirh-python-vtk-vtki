# u can run 'python vtki4StlViewer.py' so that u can see the .stl format file u selecet 
# make sure this .py file is in the same dir

import vtki

# select the .stl file
mesh =  vtki.PolyData('test3.stl')

mesh.plot()   #  pop-up the windows 

