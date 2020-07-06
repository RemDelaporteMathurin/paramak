
import math
from collections import Iterable

import cadquery as cq 

from paramak import Shape

from hashlib import blake2b

# sometimes get a segmentation fault for some reason
# this is normally due to trying to access memory that isn't available
# so could be to do with accessing a particular parameter?
# look at getters/setters imports and stuff

# this seemed to work
# shape = SweepCircleShape( 
#    ...: radius = 10, 
#    ...: points = [], 
#    ...: path_points = [(50, 0), (20, 50), (30, 100)], 
#    ...: path_workplane = "XZ", 
#    ...: workplane = "XY", 
#    ...: ) 

# I've found the error,
# when the path_workplane and workplane are switched from above, causes a core dump
# have a feeling this is to do with the coordinates that i try to access
# could be the [-1] bit or just the logic of the relationship between the two planes


class SweepCircleShape(Shape):
    """Insert docstring"""

    def __init__(
        self,
        points,
        radius,
        path_points,
        path_workplane="XY",
        workplane="XZ",
        stp_filename=None,
        solid=None,
        color=None,
        azimuth_placement_angle=0,
        cut=None,
        material_tag=None,
        name=None,
        hash_value=None,
    ):

        super().__init__(
            points,
            name,
            color,
            material_tag,
            stp_filename,
            azimuth_placement_angle,
            workplane,
        )

        self.radius = radius
        self.path_points = path_points
        self.path_workplane = path_workplane
        self.hash_value = hash_value
        self.cut = cut

    @property
    def cut(self):
        return self._cut

    @cut.setter
    def cut(self, cut):
        self._cut = cut

    @property
    def solid(self):
        if self.get_hash() != self.hash_value:
            self.create_solid()
        return self._solid

    @solid.setter
    def solid(self, solid):
        self._solid = solid

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def path_points(self):
        return self._path_points

    @path_points.setter
    def path_points(self, value):
        self._path_points = value

    @property
    def path_workplane(self):
        return self._path_workplane

    @path_workplane.setter
    def path_workplane(self, value):
        self._path_workplane = value
        # here, we need to set this to the perpendicular plane to normal workplane

    @property
    def hash_value(self):
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        self._hash_value = value

    def get_hash(self):
        hash_object = blake2b()
        hash_object.update(str(self.points).encode('utf-8') +
                           str(self.radius).encode('utf-8') +
                           str(self.path_points).encode('utf-8') +
                           str(self.path_workplane).encode('utf-8') +
                           str(self.workplane).encode('utf-8') +
                           str(self.name).encode('utf-8') +
                           str(self.color).encode('utf-8') +
                           str(self.material_tag).encode('utf-8') +
                           str(self.stp_filename).encode('utf-8') +
                           str(self.azimuth_placement_angle).encode('utf-8') +
                           str(self.cut).encode('utf-8')
        )
        value = hash_object.hexdigest()
        return value

    def create_solid(self):

        path = cq.Workplane(self.path_workplane).spline(self.path_points)
        distance = float(self.path_points[-1][1] - self.path_points[0][1])

        solid_0 = (
            cq.Workplane(self.workplane)
            .moveTo(self.path_points[0][0], 0)
            .circle(self.radius)
            .workplane(offset=distance)
            .moveTo(self.path_points[-1][0], 0)
            .circle(self.radius)
            .sweep(path, multisection=True)
        )

        self.solid = solid_0

        return solid_0

    # add azimuth_placement_angle
