
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
    path_workplane = "XZ"
)

shape.export_stp('sweep.stp')