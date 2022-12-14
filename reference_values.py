alias_dict = {
    "pass": "pass",
    "fail": "fail",
    "empty": None
}

probe_base_length_mm = 205
probe_clearance_cube_mm = 10
probe_dict = {
    "PROBE_1X575": float(probe_clearance_cube_mm + probe_base_length_mm + 1 + 57.5),
    "PROBE_3X70": float(probe_clearance_cube_mm + probe_base_length_mm + 3 + 70),
    "PROBE_5X20": float(probe_clearance_cube_mm + probe_base_length_mm + 5 + 20),
    "PROBE_5X50": float(probe_clearance_cube_mm + probe_base_length_mm + 5 + 50),
    "PROBE_8X75": float(probe_clearance_cube_mm + probe_base_length_mm + 8 + 75),
    "PROBE_DISC": float(probe_clearance_cube_mm + probe_base_length_mm + 1 + 44.5),
    "PROBE_STAR": float(probe_clearance_cube_mm + probe_base_length_mm + 30 + 250)
}