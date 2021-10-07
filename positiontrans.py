from numpy import *
from numpy import array
import math
class PoseMat:
    def __init__(self,xformMat):
        self.PoseMat = []
        self.PoseMat.append(xformMat[0][3])
        self.PoseMat.append(xformMat[1][3])
        self.PoseMat.append(xformMat[2][3])
        x = 0
        y = 0
        z = 0
        angle = 0
        rot = AxisAngleMat([[xformMat[0][0], xformMat[0][1], xformMat[0][2]],
               [xformMat[1][0], xformMat[1][1], xformMat[1][2]],
               [xformMat[2][0], xformMat[2][1], xformMat[2][2]]],x,y,z,angle)
        rv = rot.getRotationVectorr()
        self.PoseMat.append(rv[0])
        self.PoseMat.append(rv[1])
        self.PoseMat.append(rv[2])

    def __str__(self):
        return "[" + str(float(round(self.PoseMat[0],4))) +","+ str(float(round(self.PoseMat[1],4))) +","+ str(float(round(self.PoseMat[2],4)))\
               + ","+str(float(round(self.PoseMat[3],4)))+ ","+str(float(round(self.PoseMat[4],4)))+","+ str(float(round(self.PoseMat[5],4)))+"]"
    def converter(self):
        convert = [float(round(self.PoseMat[0],4)),float(round(self.PoseMat[1],4)),float(round(self.PoseMat[2],4)),float(round(self.PoseMat[3],4)),float(round(self.PoseMat[4],4)),float(round(self.PoseMat[5],4))]
        return convert
class Pose:
    # Vector < Double > pose
    def __init__(self, pose):
        self.pose = pose
        for i in range(6):
            self.pose.append(self.pose[i])

    #def setRxRyRz(rot):
    #    setRxRyRz(rot[0], rot[1], rot[2])

    #def setRxRyRz(rx,ry,rz) :
    #    pose.set(3, rx)
    #    pose.set(4, ry)
    #    pose.set(5, rz)

    #def setXYZ(pos) :
    #    setXYZ(pos[0], pos[1], pos[2])


    #def setXYZ(x,y,z) :
    #    pose.set(0, x)
    #    pose.set(1, y)
    #    pose.set(2, z)

    def getRotationVector(self):
        sublist = self.pose[3:6]
        return sublist
            #convertListToPrimitives(sublist.toArray())


 #   def convertListToPrimitives(list) :
#      length = list.len()
  #      retArr = double[len]
  #      for i in len:
   #         retArr[i] = list[i]
   #     return retArr

    def getTranslationVector(self):
        sublist = self.pose[0:3]
        return sublist
        #convertListToPrimitives(sublist.toArray(new Double[3]))

    def invert(self):
        rotMat = Matrix(self.pose.getTransformMatrix())
        invMat = rotMat.invertTransformation()
        angle = AxisAngle(invMat.subMatrix(0, 3, 0, 3))
        rotVec = angle.getRotationVector()
        transMat = invMat.subMatrix(0, 3, 3, 4)

        newPose = [transMat[0][0], transMat[1][0], transMat[2][0], rotVec[0], rotVec[1], rotVec[2]]

        return newPose


    def getTransformMatrix(self):
        trans = self.getTranslationVector()
        rot = self.getRotationVector()

        Mat = None
        _angle = math.sqrt(math.pow(rot[0], 2) + math.pow(rot[1], 2) + math.pow(rot[2], 2))
        if (_angle == 0):
            _y = _z = 0
            _x = 1
        else:
            _x = rot[0] / _angle
            _y = rot[1] / _angle
            _z = rot[2] / _angle

        angle = AxisAngle(rot,Mat,_x,_y,_z,_angle)
        rotMat = angle.getRotationMatrix()

        mat = [[rotMat[0][0], rotMat[0][1], rotMat[0][2], trans[0]],
        [rotMat[1][0], rotMat[1][1], rotMat[1][2], trans[1],],
        [rotMat[2][0], rotMat[2][1], rotMat[2][2], trans[2]],
        [0, 0, 0, 1]]

        return mat

    def pose_trans(self,p2):
        result = Matrix.multiply(self.getTransformMatrix(), p2.getTransformMatrix())
        result2 = PoseMat(result)
        return result2
        #new ?!

    def pose_transs(self,p1,p2):
        pose1 = Pose(p1)
        pose2 = Pose(p2)
        result = Matrix.multiply(pose1.getTransformMatrix(), pose2.getTransformMatrix())
        xform = Pose(result)
        return xform.toDoubleArray()


    def toDoubleArray(self):
        # czy aby na pewno pose jako parameter czy czasem nic ?!
        ret = []
        ret[0] = self.get(0)
        ret[1] = self.get(1)
        ret[2] = self.get(2)
        ret[3] = self.get(3)
        ret[4] = self.get(4)
        ret[5] = self.get(5)
        return ret


    #def tostring():
    #    DecimalFormat df = new DecimalFormat()
    #    df.setMaximumFractionDigits(4)
    #    string = "< "
    #    for i in range(6):
    #        stringing = stringing + df.format(epsilon(pose.get(i)))
    #        if (i < pose.size() - 1) string += ", "
    #        string += " >"
    #    return string


    def epsilon(comp) :
        if abs(comp) < .001:
            return 0
        else:
            return comp


    def pose_inv(pos) :
        return (Pose(pos)).invert



class AxisAngleMat :
    def __init__(self, rotMat,x,y,z,angle) :
        self.rotMat = rotMat
        self._x = x
        self._y = y
        self._z = z
        self._angle = angle

        rotVec = None
        epsilon = 0.01
        epsilon2 = 0.1
        if ((abs(rotMat[0][1] - rotMat[1][0]) < epsilon) & (abs(rotMat[0][2] - rotMat[2][0]) < epsilon)
        & (abs(rotMat[1][2] - rotMat[2][1]) < epsilon)) :
            if ((abs(rotMat[0][1] + rotMat[1][0]) < epsilon2)
            & (abs(rotMat[0][2] + rotMat[2][0]) < epsilon2)
            & (abs(rotMat[1][2] + rotMat[2][1]) < epsilon2)
            & (abs(rotMat[0][0] + rotMat[1][1] + rotMat[2][2] - 3) < epsilon2)) :
                _angle = _y = _z = 0
                _x = 1
                return
        # otherwise this singularity is angle = 180
            angle = math.pi
            xx = (rotMat[0][0] + 1) / 2
            yy = (rotMat[1][1] + 1) / 2
            zz = (rotMat[2][2] + 1) / 2
            xy = (rotMat[0][1] + rotMat[1][0]) / 4
            xz = (rotMat[0][2] + rotMat[2][0]) / 4
            yz = (rotMat[1][2] + rotMat[2][1]) / 4
            if ((xx > yy) & (xx > zz)) :

                if (xx < epsilon):
                    x = 0
                    y = 0.7071
                    z = 0.7071
                else:
                    x = math.sqrt(xx)
                    y = xy / x
                    z = xz / x

            elif(yy > zz) :
                #// m[1][1] is the largest diagonal term
                if (yy < epsilon) :
                    x = 0.7071
                    y = 0
                    z = 0.7071
                else :
                    y = math.sqrt(yy)
                    x = xy / y
                    z = yz / y
            else :
        #// m[2][2] is th largest diagonal term so base result  on // this
                if (zz < epsilon) :
                    x = 0.7071
                    y = 0.7071
                    z = 0
                else :
                    z = math.sqrt(zz)
                    x = xz / z
                    y = yz / z
                _x = x
                _y = y
                _z = z
                _angle = angle
            return
        s = math.sqrt((rotMat[2][1] - rotMat[1][2]) * (rotMat[2][1] - rotMat[1][2])
        + (rotMat[0][2] - rotMat[2][0]) * (rotMat[0][2] - rotMat[2][0])
        + (rotMat[1][0] - rotMat[0][1]) * (rotMat[1][0] - rotMat[0][1]))
        if (abs(s) < 0.001):
            s = 1
        anglee = math.acos((rotMat[0][0] + rotMat[1][1] + rotMat[2][2] - 1) / 2)
        xx = (rotMat[2][1] - rotMat[1][2]) / s
        yy = (rotMat[0][2] - rotMat[2][0]) / s
        zzz = (rotMat[1][0] - rotMat[0][1]) / s
        self._x = xx
        self._y = yy
        self._z = zzz
        self._angle = anglee
    def getRotationVectorr(self):
#        if (self.rotVec is None):
#            return self.rotVec
        rotVec = [self._angle * self._x, self._angle * self._y, self._angle * self._z]
        return rotVec

class AxisAngle :

   # double[][] rotMat
    #double[] rotVec
    #double _x
    #double _y
    #double _z


    def __init__(self, rotVec,rotMat, x,y,z,angle) :
        self.rotVec = rotVec
        self.rotMat = rotMat
        self._x = x
        self._y = y
        self._z = z
        self._angle = angle

        #_angle = math.sqrt(math.pow(rotVec[0], 2) + math.pow(rotVec[1], 2)+ math.pow(rotVec[2], 2))
        #if (_angle == 0) :
        #    _y = _z = 0;
        #    _x = 1;
        #else:
        #    _x = rotVec[0] / _angle
        #    _y = rotVec[1] / _angle
        #    _z = rotVec[2] / _angle

    def AxisAngless(self, x, y, z, theta):
        _x = x
        _y = y
        _z = z
        _angle = theta

    def getAngle(self):
        return self._angle

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def getRotationVector(self):
        if (self.rotVec is None):
            return self.rotVec
        rotVec = [self._angle * self._x, self._angle * self._y, self._angle * self._z]
        return rotVec

    def getRotationMatrix(self):
        #if (self.rotMat != None):
        #   return self.rotMat
        #if (self._angle == 0):
        #    doube = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        #    return doube

        c = math.cos(self._angle)
        s = math.sin(self._angle)
        t = 1.0 - c

        m00 = c + self._x * self._x * t
        m11 = c + self._y * self._y * t
        m22 = c + self._z * self._z * t
        tmp1 = self._x * self._y * t
        tmp2 = self._z * s
        m10 = tmp1 + tmp2
        m01 = tmp1 - tmp2

        tmp1 = self._x * self._z * t
        tmp2 = self._y * s
        m20 = tmp1 - tmp2
        m02 = tmp1 + tmp2
        tmp1 = self._y * self._z * t
        tmp2 = self._x * s
        m21 = tmp1 + tmp2
        m12 = tmp1 - tmp2
        double = [[m00, m01, m02], [m10, m11, m12], [m20, m21, m22]]
        return double

    def printRotationMatrix(self,epsilon):
        matrix = self.pose.getRotationMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix)) :
                print(epsilon(matrix[i][j]) + " ")
            print()

    def epsilon(comp) :
        if (abs(comp) < .001):
            return 0
        else :
            return comp

#    def computeComponentsFromRotVec():
        #    rotMat = None
        #_angle = math.sqrt(math.pow(rotVec[0], 2) + math.pow(rotVec[1], 2)+ math.pow(rotVec[2], 2))
        #if (_angle == 0) :
        #    _y = _z = 0;
        #    _x = 1;
        #else:
        #    _x = rotVec[0] / _angle
        #    _y = rotVec[1] / _angle
        #    _z = rotVec[2] / _angle





class Matrix :


    def __init__(self,data) :
        self.matrix = data


    #def setData(self,data):
    #   self.matrix = data

    def getData(self) :
        return self.matrix

    #def determinant():
     #   if (self.matrix.length != self.matrix[0].length):
       #     throw        new
      #      IllegalStateException("invalid dimensions");

        #if (self.matrix.length == 2)
         #   return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0];

        #double
        #det = 0

       # for (int i = 0; i < self.matrix[0].length; i++) {
        #    Matrix detMat = new Matrix(minor(0, i));
        #det += math.pow(-1, i) * matrix[0][i]
        #* detMat.determinant();
        #}
        #return det;
        #}

    def invertTransformation(self):
        assert (self.matrix[0].length == self.matrix.length & self.matrix.length == 4);
        rmatrix = [0, 3, 0, 3]
        tmatrix = [0, 3, 3, 4]
        rinv = Matrix.invert(rmatrix)
        tvector = Matrix.negate(Matrix.multiply(rinv, tmatrix))

        inversion = Matrix[[rinv[0][0], rinv[0][1], rinv[0][2], tvector[0][0]],
                            [rinv[1][0], rinv[1][1], rinv[1][2], tvector[1][0]],
                           [rinv[2][0], rinv[2][1], rinv[2][2], tvector[2][0]],[0, 0, 0, 1]]
        return inversion

    #def toString():
    #    String
    #    str = "";
    #    for (int i = 0; i < matrix.length; i ++){
    #   for (int j = 0; j < matrix[0].length; j++){
    #    str += epsilon(matrix[i][j])+"\t";
    #    }
    #    str += "\n";
    #    }
    #    return str

    def epsilon(comp) :
        if (abs(comp) < .001):
            return 0
        else:
            return comp
    def negate(mat):
        newmat = [mat.length][mat[0].length]
        for i in range() :
            for j in range() :
                newmat[i][j] = -mat[i][j]
        return newmat
    def subMatrix(self,rstart,rend,colstart,colend):
        rowlen = rend - rstart
        collen = colend - colstart
        sub = [rowlen][collen]
        count = 0
        i = rstart
        while i ==rstart and i < rend:
                count =+1
                sub[count] = self.matrix[i](colstart, colend+1)
                i = i+1
        return sub

    def invert(self) :
        return Matrix().inverse()

#    def inverse(self):
#        inverse = [self.matrix.len][self.matrix.len]
#        for i in self.matrix:
#            for j in self.matrix:
#               inverse = math.pow(-1, i + j) * Matrix(minor(i, j)).determinant()

#        det = 1.0 / determinant()
        #         for i in inverse:
        #             j = 0
        #             while (j<=i):
        #       temp = inverse[i][j]
        #       inverse[i][j] = inverse[j][i] * det
        #       inverse[j][i] = temp * det
        #       j+=1
        #
    #  return inverse

#    def minor(self,row,column) :
#        minor = [len(self.matrix) - 1][len(self.matrix) - 1]
#       for i in self.matrix:
#            for j in self.matrix:
#               if (j != column):
#                    minor[i < row  i: i - 1][j < column ? j: j - 1] = self.matrix[i][j]
#        return minor

    def multiply(a,b):
        if (len(a[0]) != len(b)):
            raise ValueError("invalid dimensions")
        newmatrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        # iterate through rows of X
        for i in range(len(a)):
            # iterate through columns of Y
            for j in range(len(b[0])):
                # iterate through rows of Y
                for k in range(len(b)):
                    newmatrix[i][j] += a[i][k] * b[k][j]
        #matrix = Matrix(newmatrix)
        return newmatrix



    #def multiply(self,b) :
    #  if (self.matrix[0].length != b.length):
    #        raise ValueError("invalid dimensions")
    #    newmatrix = [self.matrix.length][b[0].length]
    #    for i in self.matrix:
    #        for j in b[0]:
    #            sum = 0
    #            for k in len(self.matrix[i]):
    #                sum += self.matrix[i][k] * b[k][j]
    #            newmatrix[i][j] = sum
    #    return newmatrix

    def rref(self):

        rref = [[len(self.matrix)],[]]
        for i in self.matrix:
            rref[i] = self.matrix.slice[i:]
        r = 0
        c = 0
        while c < rref[0].length  and r < rref.length:
            j = r
            c =+1
        while i == r+1 and i < rref.length:
            if (abs(rref[i][c]) > abs(rref[j][c])):
                j = i
            if (abs(rref[j][c]) < 0.00001):
                continue
            i=i+1
        temp = rref[j]
        rref[j] = rref[r]
        rref[r] = temp
        s = 1.0 / rref[r][c]
        for j in rref:
            rref[r][j] *= s
        for i in rref :
            if (i != r) :
                t = rref[i][c]
        for j in rref:
            rref[i][j] -= t * rref[r][j]
            r=r+1

        return rref

    def transpose(self):
        transpose = [self.matrix[0].length][self.matrix.length]
        for i in self.matrix:
            for j in range(len(self.matrix[i])):
                transpose[j][i] = self.matrix[i][j]
        return transpose

pose1= Pose([-0.12, -0.43, 0.145, 0, -0.48528, -0.72793])
pose2 = Pose([0.0, 0.07, 0.0, 0.05, 0.0, 0.0])
finalny  = pose1.pose_trans(pose2)
print(finalny)
