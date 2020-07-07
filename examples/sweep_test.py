
import paramak as p

shape = p.SweepStraightShape(
    points = [
        (0, 0),
        (0, 40),
        (20, 40),
        (30, 20),
        (20, 0)
    ],
    path_points = [
        (20, 0),
        (50, 50), 
        (35, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('straight.stp')

shape = p.SweepSplineShape(
    points = [
        (0, 0),
        (0, 10),
        (20, 30),
        (40, 10),
        (30, 5),
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100),
        (50, 150),
        (80, 200),
        (100, 300)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('spline.stp')

shape = p.SweepMixedShape(
    points = [
        (0, 0, "straight"),
        (0, 20, "spline"),
        (10, 10, "spline"),
        (10, 0, "straight")
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('mixed.stp')

shape = p.SweepStraightShape(
    points = [
        (-10, 10),
        (10, 10),
        (10, -10),
        (-10, -10)
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_straight_central.stp')


shape = p.SweepStraightShape(
    points = [
        (0, 0),
        (0, 20),
        (20, 20),
        (20, 0)
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_straight_offset.stp')




shape = p.SweepSplineShape(
    points = [
        (0, 0),
        (0, 10),
        (20, 30),
        (40, 10),
        (30, 5),
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100),
        (50, 150),
        (80, 200),
        (100, 300)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_spline_offset.stp')


shape = p.SweepSplineShape(
    points = [
        (-20, -20),
        (-20, -10),
        (0, 10),
        (20, -10),
        (10, -15),
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100),
        (50, 150),
        (80, 200),
        (100, 300)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_spline_central.stp')



shape = p.SweepMixedShape(
    points = [
        (0, 0, "straight"),
        (0, 20, "spline"),
        (10, 10, "spline"),
        (10, 0, "straight")
    ],
    path_points = [
        (50, 0),
        (35, 50),
        (70, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_mixed_offset.stp')



shape = p.SweepMixedShape(
    points = [
        (-10, -10, "straight"),
        (-10, 10, "spline"),
        (0, 5, "spline"),
        (10, -10, "straight")
    ],
    path_points = [
        (50, 0),
        (35, 50),
        (70, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('azimuth_mixed_central.stp')




shape = p.SweepCircleShape(
    points = [],
    path_points = [
        (30, 0),
        (50, 50),
        (40, 100)
    ],
    radius = 10,
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('circles.stp')



shape = p.SweepCircleShape(
    points = [],
    path_points = [
        (30, -50),
        (50, 0),
        (40, 50)
    ],
    radius = 10,
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('circle_center_z_test.stp')




shape = p.SweepStraightShape(
    points = [
        (-10, 10),
        (10, 10),
        (15, 0),
        (10, -10),
        (-10, -10)
    ],
    path_points = [
        (20, -50),
        (50, 0),
        (35, 50)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 90, 180, 270]
)
shape.export_stp('straight_center_z_test.stp')


shape = p.SweepSplineShape(
    points = [
        (-20, -20),
        (-20, -10),
        (0, 10),
        (20, -10),
        (10, -15),
    ],
    path_points = [
        (20, 0),
        (50, 50),
        (35, 100)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 120, 240]
)
shape.export_stp('spline_center_z_test.stp')



shape = p.SweepMixedShape(
    points = [
        (-10, -10, "straight"),
        (-10, 10, "spline"),
        (0, 5, "spline"),
        (10, -10, "straight")
    ],
    path_points = [
        (50, -50),
        (35, 0),
        (70, 50)
    ],
    workplane = "XY",
    path_workplane = "XZ",
    azimuth_placement_angle = [0, 120, 240]
)
shape.export_stp('mixed_center_z_test.stp')



