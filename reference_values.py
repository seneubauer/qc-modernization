alias_dict = {
    "pass": int(0x8001),            # hexadecimal -> 32,768
    "fail": int(0x8000),            # hexadecimal -> 32,769
    "empty": None,
    "gauges": {
        "mating_part": {
            "keys": ["mate", "mating"],
            "alias": 0b0000000000000000000001
        },
        "cmm": {
            "keys": ["cmm"],
            "alias": 0b0000000000000000000010
        },
        "comparator": {
            "keys": ["comp"],
            "alias": 0b0000000000000000000100
        },
        "vision_system": {
            "keys": ["scope"],
            "alias": 0b0000000000000000001000
        },
        "caliper": {
            "keys": ["caliper", "cal"],
            "alias": 0b0000000000000000010000
        },
        "id_caliper": {
            "keys": ["id"],
            "alias": 0b0000000000000000100000
        },
        "indicator": {
            "keys": ["ind"],
            "alias": 0b0000000000000001000000
        },
        "profilometer": {
            "keys": ["prof"],
            "alias": 0b0000000000000010000000
        },
        "visual": {
            "keys": ["visual"],
            "alias": 0b0000000000000100000000
        },
        "plug": {
            "keys": ["plug", "plg"],
            "alias": 0b0000000000001000000000
        },
        "height_gauge": {
            "keys": ["height"],
            "alias": 0b0000000000010000000000
        },
        "feeler_gauge": {
            "keys": ["feeler"],
            "alias": 0b0000000000100000000000
        },
        "bore_gauge": {
            "keys": ["bore"],
            "alias": 0b0000000001000000000000
        },
        "thread_mic": {
            "keys": ["thread"],
            "alias": 0b0000000010000000000000
        },
        "groove_mic": {
            "keys": ["groove", "grv"],
            "alias": 0b0000000100000000000000
        },
        "blade_mic": {
            "keys": ["blade"],
            "alias": 0b0000001000000000000000
        },
        "spring_gauge": {
            "keys": ["spring"],
            "alias": 0b0000010000000000000000
        },
        "wilson": {
            "keys": ["wilson"],
            "alias": 0b0000100000000000000000
        },
        "pushpull": {
            "keys": ["pushpull"],
            "alias": 0b0001000000000000000000
        },
        "verify": {
            "keys": ["verif"],
            "alias": 0b0010000000000000000000
        },
        "pins": {
            "keys": ["pin"],
            "alias": 0b0100000000000000000000
        },
        "ring": {
            "keys": ["ring"],
            "alias": 0b1000000000000000000000
        }
    }
}

probe_base_length_mm = 205
probe_clearance_cube_mm = 10
probe_dict = {
    "probe_1x575": float(probe_clearance_cube_mm + probe_base_length_mm + 1 + 57.5),
    "probe_3x70": float(probe_clearance_cube_mm + probe_base_length_mm + 3 + 70),
    "probe_5x20": float(probe_clearance_cube_mm + probe_base_length_mm + 5 + 20),
    "probe_5x50": float(probe_clearance_cube_mm + probe_base_length_mm + 5 + 50),
    "probe_8x75": float(probe_clearance_cube_mm + probe_base_length_mm + 8 + 75),
    "probe_disc": float(probe_clearance_cube_mm + probe_base_length_mm + 1 + 44.5),
    "probe_star": float(probe_clearance_cube_mm + probe_base_length_mm + 30 + 250)
}