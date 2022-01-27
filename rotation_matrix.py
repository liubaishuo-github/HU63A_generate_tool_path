def transf(apt_point):
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












if __name__ == "__main__":

    input_lines = remove_parentheses.remove_par(read_file.read_file())

    temp = retrieve_coord(input_lines)
    print('======================')
    for i in temp:
        print(i)
