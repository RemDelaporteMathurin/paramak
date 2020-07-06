
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


class SweepStraightShape(Shape):
    """Insert docstring"""

    def __init__(
        self,
        points,
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

        # we create a workplane,
        # move to the start path point
        # create a new workplane with an origin at this point
        # create the 2D shape
        # move back to the origin of the original workplane, -self.path_points[0][0]
        # create a new workplane offset by distance
        # move to the end path point
        # create a new workplane with an origin at this point
        # create the 2D shape again

        solid_0 = (
            cq.Workplane(self.workplane)
            .moveTo(self.path_points[0][0], 0)
            .workplane()
            .polyline(self.points)
            .close()
            .moveTo(-self.path_points[0][0], 0)
            .workplane(offset=distance)
            .moveTo(self.path_points[-1][0], 0)
            .workplane()
            .polyline(self.points)
            .close()
            .sweep(path, multisection=True)
        )

        # for the moment, the spline defines the path between the first point of each 2D shape in each plane
        # i.e. the spline connects the 'same point' in each 2D shape
        # the start and end spline points define the 'origin' of the 2D shape so the shape should have the start point of (0, 0),
        # however, we may want to change this in the future so that the points and path_points all match
        # i.e. we would have to assert that self.points[0] = self.path_points[0]
        # however, don't think this would work because we don't have two sets of points for each face
        # this would require some rework of how the workplanes are created and such
        # maybe we can just define everything from one origin?

        # i.e. there are a few ways of doing this, but its quite difficult
        # for the moment, it is easier to assert that the first point of the 2D shape must be (0, 0), and that we set its position
        # in space by the path_points

        self.solid = solid_0
        return solid_0



