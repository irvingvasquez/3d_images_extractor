import open3d as o3d, pandas as pd, numpy as np

def get_bb(dire):

    arr = np.zeros((len(dire),24)) #to store the bounding boxes
    for i in range(0, len(dire)):
        mesh = o3d.io.read_triangle_mesh(dire.iat[i,0] + '/meshes/model.obj') #read mesh
        bb = o3d.geometry.OrientedBoundingBox.get_oriented_bounding_box(mesh) #create bb
        bb_p = np.asarray(bb.get_box_points()) # extract bb points
        a = np.reshape(bb_p, (1,24))
        arr[i,:] = a
    
    df = pd.DataFrame(arr, columns = ['x0','y0','z0','x1','y1','z1','x2','y2','z2','x3','y3','z3','x4','y4','z4','x5','y5','z5','x6','y6','z6','x7','y7','z7'])
    return df
