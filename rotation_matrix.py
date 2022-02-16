import re, read_file, remove_parentheses, copy, os, retrieve_coord

def transf(retrieved_coord):
    from numpy import mat
    from math import sin, cos, radians, degrees, \
                  radians, asin, atan2, fabs, pi

    def translation_z(dis):
        t = mat([
                  [ 1, 0, 0, 0],
                  [ 0, 1, 0, 0],
                  [ 0, 0, 1, dis],
                  [ 0, 0, 0, 1],
                                  ])
        return t
    def translation_x(dis):
        t = mat([
                  [ 1, 0, 0, dis],
                  [ 0, 1, 0, 0],
                  [ 0, 0, 1, 0],
                  [ 0, 0, 0, 1],
                                  ])
        return t
    def rot_y(de):
        t = mat([
                  [ cos(de), 0, sin(de), 0],
                  [ 0,       1,       0, 0],
                  [-sin(de), 0, cos(de), 0],
                  [0, 0, 0, 1]
                                              ])
        return t
    def rot_x(de):
        t = mat([
                  [1, 0, 0, 0],
                  [0, cos(de), -sin(de), 0],
                  [0, sin(de), cos(de), 0],
                  [0, 0, 0, 1]
                                              ])
        return t


    transfered_coord = []
    for i in retrieved_coord:
        print(i)
        pch_x, pch_y, pch_z, pch_b, pch_c = float(i[1]), float(i[2]), float(i[3]), radians(float(i[4])), radians(float(i[5]))
        apt_coord = rot_x(-pch_c) * translation_x(-3) * rot_y(pch_b) * translation_z(37.3964) * mat([pch_x, pch_y, pch_z, 1]).T
        apt_x, apt_y, apt_z = apt_coord[0,0], apt_coord[1,0], apt_coord[2,0]

        apt_vector = rot_x(-pch_c) * rot_y(pch_b) * mat([0,0,1,1]).T
        apt_i, apt_j, apt_k = apt_vector[0,0], apt_vector[1,0], apt_vector[2,0]

        temp = [i[0], round(apt_x,5), round(apt_y,5), round(apt_z,5), round(apt_i,7), round(apt_j,7), round(apt_k,7)]
        transfered_coord.append(temp)

    return transfered_coord



if __name__ == "__main__":

    input_lines = remove_parentheses.remove_par(read_file.read_file())

    retrieved_coord = retrieve_coord.retrieve_coord(input_lines)
    transfered_coord = transf(retrieved_coord)
    print('======================')
    for i in transfered_coord:
        print(i)
