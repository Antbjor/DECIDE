import config
import math
import numpy as np


class LaunchInterceptorConditions:
    """A class that calculates the Launch Interceptor Conditions (LICs)."""

    def __init__(self, parameters=config.parameters, num_points=config.num_points,
                 x=config.X, y=config.Y):
        self.x = x
        self.y = y
        self.num_points = num_points  # [2, 100]
        self.parameters = parameters

    def condition_0(self):
        """
        Return true if two consecutive data points are further apart than LENGTH1
        """
        for i in range(self.num_points - 1):
            if math.dist([self.x[i], self.y[i]], [self.x[i + 1], self.y[i + 1]]) > self.parameters["LENGTH1"]:
                return True
        return False

    def condition_1(self):
        """
        Return true if three consecutive data points cannot be contained on a circle with radius RADIUS1
        """
        radius = self.parameters["RADIUS1"]
        for i in range(self.num_points - 2):

            center = [(self.x[i] + self.x[i + 1] + self.x[i + 2]) / 3, (self.y[i] + self.y[i + 1] + self.y[i + 2]) / 3]
            dist_1 = math.dist([self.x[i], self.y[i]], center)
            dist_2 = math.dist([self.x[i + 1], self.y[i + 1]], center)
            dist_3 = math.dist([self.x[i + 2], self.y[i + 2]], center)
            if dist_1 > radius or dist_2 > radius or dist_3 > radius:
                return True
        return False

    def condition_2(self):
        pi = config.PI
        epsilon = self.parameters["EPSILON"]
        if epsilon > pi or epsilon < 0:
            raise TypeError("Epsilon must fulfill 0 < Epsilon < pi")

        # special case
        if self.num_points == 2:
            return False
        for i in range(self.num_points - 2):
            # three consecutive datapoints p, q, r. q is the vertex.
            p = (self.x[i], self.y[i])
            q = (self.x[i + 1], self.y[i + 1])
            r = (self.x[i + 2], self.y[i + 2])

            # if a or c coincides with the vertex, the angle is undefined
            if p == q or q == r:
                continue
            # given two vectors a and b, the angle theta between them can be found with
            # theta = arc-cos( (a ⋅ b) / (|a|⋅|b|))
            vector_a = ([q[0] - p[0], q[1] - p[1]])
            vector_a_norm = vector_a / np.linalg.norm(vector_a)
            vector_b = [q[0] - r[0], q[1] - r[1]]
            vector_b_norm = vector_b / np.linalg.norm(vector_b)
            dot_product = np.dot(vector_a_norm, vector_b_norm)
            angle = np.arccos(dot_product)

            if angle < pi - epsilon or angle > pi + epsilon:
                return True

            return False

    def condition_3(self):
        # special cases
        if self.num_points == 2:
            return False
        # regular cases
        for i in range(self.num_points - 2):
            area = abs(self.x[i] * (self.y[i + 1] - self.y[i + 2])
                       + self.x[i + 1] * (self.y[i + 2] - self.y[i])
                       + self.x[i + 2] * (self.y[i] - self.y[i + 1])) / 2
            if area > self.parameters["AREA1"]:
                return True
        return False

    def condition_4(self):
        """
        Return true if Q_PTS consecutive data points lie in more than QUADS quadrants
        """
        q_pts = self.parameters["Q_PTS"]
        quads = self.parameters["QUADS"]
        if 2 > q_pts or q_pts > self.num_points:
            raise ValueError("Q_PTS does not satisfy 2 <= Q_PTS <= NUMPOINTS")
        if 1 > quads or quads > 3:
            raise ValueError("QUADS does not satisfy 1 <= QUADS <= 3")

        for i in range(self.num_points - q_pts + 1):
            point_in_quadrant = [False, False, False, False]
            for j in range(q_pts):
                x = self.x[i + j]
                y = self.y[i + j]
                # point_in_quadrant[index] tells whether there is a point in quadrant index + 1
                if y >= 0:
                    if x >= 0:
                        point_in_quadrant[0] = True
                    else:
                        point_in_quadrant[1] = True
                else:
                    if x <= 0:
                        point_in_quadrant[2] = True
                    else:
                        point_in_quadrant[3] = True
            if point_in_quadrant.count(True) >= quads:
                return True
        return False


    def condition_5(self):
        for i in range(self.num_points - 1):
            if self.x[i] > self.x[i + 1]:
                return True
        return False

    def condition_6(self):
        num_consecutive = self.parameters["N_PTS"]
        min_dist = self.parameters["DIST"]

        # The condition is not met when NUMPOINTS <3.
        if self.num_points < 3:
            return False

        for i in range(self.num_points - 2):
            p = np.array([self.x[i], self.y[i]])
            # if this condition is met we are at the last point in the consecutive search
            if i + num_consecutive > self.num_points:
                return False
            q = np.array([self.x[i + num_consecutive - 1], self.y[i + num_consecutive - 1]])

            # special case when the first and the last of the consecutive points coincide.
            if p.all() == q.all():
                for j in range(1, num_consecutive - 2):
                    r = np.array([self.x[i + j], self.y[i + j]])
                    # Distance between the two coinciding points and the point r in between them
                    dist = np.linalg.norm(p - r)
                    if dist > min_dist:
                        return True

            for k in range(1, num_consecutive - 2):
                r = np.array([self.x[i + k], self.y[i + k]])
                # Avoid dividing by zero
                if np.linalg.norm(q - p) == 0:
                    return False
                dist = np.cross(q - p, r - p) / np.linalg.norm(q - p)
                if dist > min_dist:
                    return True

        return False

    def condition_7(self):
        k_pts = self.parameters["K_PTS"]
        # special cases
        if self.num_points < 3:
            return False
        if k_pts > self.num_points - 2:
            return False
        # regular cases
        for i in range(self.num_points - k_pts - 1):
            j = i + k_pts + 1
            length = math.sqrt(math.pow(self.x[i] - self.x[j], 2) +
                               math.pow(self.y[i] - self.y[j], 2))
            if length > self.parameters["LENGTH1"]:
                return True
        return False

    def condition_8(self):
        """
        Return true if there exists a set of three data points, separated by A_PTS and B_PTS
        consecutive intervening points, which cannot be contained within a circle of radius RADIUS1
        """
        a_pts = self.parameters["A_PTS"]
        b_pts = self.parameters["B_PTS"]
        radius = self.parameters["RADIUS1"]

        if a_pts < 1:
            raise ValueError("A_PTS must be >= 1")
        if b_pts < 1:
            raise ValueError("B_PTS must be >= 1")

        # special case
        if self.num_points < 5:
            return False
        # regular case
        for i in range(self.num_points - (a_pts + b_pts + 2)):
            center = [(self.x[i] + self.x[i + a_pts + 1] + self.x[i + a_pts + 2 + b_pts]) / 3,
                      (self.y[i] + self.y[i + a_pts + 1] + self.y[i + a_pts + 2 + b_pts]) / 3]
            dist_1 = math.dist([self.x[i], self.y[i]], center)
            dist_2 = math.dist([self.x[i + a_pts + 1], self.y[i + a_pts + 1]], center)
            dist_3 = math.dist([self.x[i + a_pts + 2 + b_pts], self.y[i + a_pts + 2 + b_pts]], center)
            if dist_1 > radius or dist_2 > radius or dist_3 > radius:
                return True
        return False


    def condition_9(self):
        """
        Return true if there exist one or more sets of three data points separated by C_PTS and D_PTS
        consecutive intervening points that form an angle under certain conditions
        """
        c_pts = self.parameters["C_PTS"]
        d_pts = self.parameters["D_PTS"]
        epsilon = self.parameters["EPSILON"]

        # Special case
        if self.num_points < 5:
            return False
        # Regular case
        for i in range(self.num_points - (c_pts + d_pts + 2)):
            first_point = np.array([self.x[i], self.y[i]])
            vertex_point = np.array([self.x[i + c_pts + 1], self.y[i + c_pts + 1]])
            last_point = np.array([self.x[i + c_pts + d_pts + 2], self.y[i + c_pts + d_pts + 2]])

            # Special case, points coincide with the vertex
            if (np.array_equal(first_point, vertex_point)) or (np.array_equal(last_point, vertex_point)):
                continue

            ba = first_point - vertex_point
            bc = last_point - vertex_point
            cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle = np.arccos(cosine_angle)

            if (angle < (math.pi - epsilon)) or (angle > (math.pi + epsilon)):
                return True
        return False

    def condition_10(self):
        """
        There exists at least one set of three data points separated by exactly E PTS and F PTS
        consecutive intervening points, respectively, that are the vertices of a triangle with area
        greater than AREA1. The condition is not met when NUMPOINTS <5
        """

        e_pts = self.parameters["E_PTS"]
        f_pts = self.parameters["F_PTS"]
        area_1 = self.parameters["AREA_1"]

        # special cases
        if self.num_points < 5:
            return False

        for i in range(self.num_points - (e_pts + f_pts + 2)):
            a = (self.x[i], self.y[i])
            b = (self.x[i + e_pts + 1], self.y[i + e_pts + 1])
            c = (self.x[i + e_pts + f_pts + 2], self.y[i + e_pts + f_pts + 2])

            # Coordinates do not form a triangle, no computations needed
            if a == b or a == c or b == c:
                continue

            area = 0.5 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
            if area > area_1:
                return True

        return False

    def condition_11(self):
        g_pts = self.parameters["G_PTS"]
        # special cases
        if self.num_points < 3:
            return False
        if g_pts > self.num_points - 2:
            return False
        # regular cases
        for i in range(self.num_points - g_pts - 1):
            if self.x[i] > self.x[i + g_pts + 1]:
                return True
        return False

    def condition_12(self):
        """
        Return true if both conditions are true:
        1. There exists two data points, separated by K_PTS consecutive points, which are further apart than LENGTH1.
        2. There exists two data points, separated by K_PTS consecutive points, which are further apart than LENGTH2.
        """
        k_pts = self.parameters["K_PTS"]
        length1 = self.parameters["LENGTH1"]
        length2 = self.parameters["LENGTH2"]
        if length2 < 0:
            raise ValueError("LENGTH2 must not be less than 0")

        # special case
        if self.num_points < 3:
            return False
        # regular case
        cond1, cond2 = False, False
        for i in range(self.num_points - k_pts - 1):
            if math.dist([self.x[i], self.y[i]],[self.x[i + k_pts + 1], self.y[i + k_pts + 1]]) > length1:
                cond1 = True
        for i in range(self.num_points - k_pts - 1):
            if math.dist([self.x[i], self.y[i]],[self.x[i + k_pts + 1], self.y[i + k_pts + 1]]) > length2:
                cond2 = True
        return cond1 and cond2

    def condition_13(self):
        """
        Return true if there 
        1. exist one or more sets of three data points separated by A_PTS and B_PTS
        consecutive intervening points that cannot be contained within a circle of radius1
        2. exist one or more sets of three data points separated by A_PTS and B_PTS
        consecutive intervening points that can be contained within a circle of radius2
        """
        a_pts = self.parameters["A_PTS"]
        b_pts = self.parameters["B_PTS"]
        radius1 = self.parameters["RADIUS1"]
        radius2 = self.parameters["RADIUS2"]
        radius1_circle = True
        radius2_circle = False

        # special cases
        if self.num_points < 5:
            return False

        # regular cases
        for i in range(self.num_points - (a_pts + b_pts + 2)):
            center = [(self.x[i] + self.x[i + a_pts + 1] + self.x[i + a_pts + b_pts + 2]) / 3,
                      (self.y[i] + self.y[i + a_pts + 1] + self.y[i + a_pts + b_pts + 2]) / 3]
            dist_1 = math.dist([self.x[i], self.y[i]], center)
            dist_2 = math.dist([self.x[i + a_pts + 1], self.y[i + a_pts + 1]], center)
            dist_3 = math.dist([self.x[i + a_pts + b_pts + 2], self.y[i + a_pts + b_pts + 2]], center)

            # Three data points that cannot be contained within circle with radius1
            if dist_1 > radius1 or dist_2 > radius1 or dist_3 > radius1:
                radius1_circle = False

            # Three data points that can be contained within circle with radius2
            if dist_1 <= radius2 and dist_2 <= radius2 and dist_3 <= radius2:
                radius2_circle = True

        if not radius1_circle and radius2_circle:
            return True

        return False

    def condition_14(self):
        """
        There exists at least one set of three data points, separated by exactly E PTS and F PTS con-
        secutive intervening points, respectively, that are the vertices of a triangle with area greater
        than AREA1. In addition, there exist three data points (which can be the same or different
        from the three data points just mentioned) separated by exactly E PTS and F PTS consec-
        utive intervening points, respectively, that are the vertices of a triangle with area less than
        AREA2. Both parts must be true for the LIC to be true. The condition is not met when
        NUMPOINTS <5.
        """
        e_pts = self.parameters["E_PTS"]
        f_pts = self.parameters["F_PTS"]
        area_1 = self.parameters["AREA_1"]
        area_2 = self.parameters["AREA_2"]
        cond1 = False
        cond2 = False

        # special cases
        if self.num_points < 5:
            return False

        for i in range(self.num_points - (e_pts + f_pts + 2)):
            a = (self.x[i], self.y[i])
            b = (self.x[i + e_pts + 1], self.y[i + e_pts + 1])
            c = (self.x[i + e_pts + f_pts + 2], self.y[i + e_pts + f_pts + 2])

            # Coordinates do not form a triangle, no computations needed
            if a == b or a == c or b == c:
                continue

            area = 0.5 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
            if area > area_1:
                cond1 = True
            if area < area_2:
                cond2 = True
            if cond1 and cond2:
                return True

        return False

    function_list = [condition_0, condition_1, condition_2, condition_3, condition_4,
                     condition_5, condition_6, condition_7, condition_8, condition_9,
                     condition_10, condition_11, condition_12, condition_13, condition_14]
