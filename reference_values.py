alias_dict = {
    "pass": "pass",
    "fail": "fail",
    "empty": None,
    "first_only": -int(0b100),
    "middle_only": -int(0b010),
    "last_only": -int(0b001),
    "first_middle": -int(0b110),
    "last_middle": -int(0b011),
    "first_last": -int(0b101),
    "first_middle_last": -int(0b111),
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