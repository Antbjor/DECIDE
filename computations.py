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
        return True

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
        return True

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
        return True

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
        return True

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
        return True

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

        if not (radius1_circle) and radius2_circle:
            return True

        return False

    def condition_14(self):
        return True

    function_list = [condition_0, condition_1, condition_2, condition_3, condition_4,
                     condition_5, condition_6, condition_7, condition_8, condition_9,
                     condition_10, condition_11, condition_12, condition_13, condition_14]
