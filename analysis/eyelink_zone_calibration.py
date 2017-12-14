"""
Functions to load raw EYELINK data,
and extract gaze zones, based on s99_d1 data.
"""

import pprint as pp
import os

def load_file(file_path):
    """Load %s and convert to a list""" % file_path

    with open(file_path) as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
    return lines


def get_gazes(lines):
    """Get gazes, as defined by eye data between long blinks ('.' values)"""

    blinks = 0
    frame = 0
    gazes = []
    gaze = []

    for line in lines:
        values = line.split()
        if '/Users/ssnl_booth2/Desktop/model_experiment_two.MP4' in line:
            frame = values[5]
        elif frame:
            if values[0].isdigit():
                if values[1] == '.':
                    blinks += 1
                elif blinks >= 15:
                    values = list(map((lambda x: float(x)), values[0:4]))
                    blinks = 0
                    gazes.append(gaze)
                    gaze = [values]
                else:
                    values = list(map((lambda x: float(x)), values[0:4]))
                    gaze.append(values)
    return gazes


def get_gaze_ranges(gazes):
    """Get the minimum and maximum x, y values of each gaze"""

    ranges = []
    for gaze in gazes:
        if gaze:
            min_x = min(gaze, key=lambda x: x[1])[1]
            max_x = max(gaze, key=lambda x: x[1])[1]
            min_y = min(gaze, key=lambda x: x[2])[2]
            max_y = max(gaze, key=lambda x: x[2])[2]
            ranges.append([
                min_x,
                max_x,
                min_y,
                max_y
            ])
    return ranges


# TODO Make more generic - extract zones into a param
def get_zone_ranges(gaze_ranges):
    """
    Assign gazes to zones: face, monitor and arm, based on order.
    Get the minimum and maximum x, y values of each zone
    """

    face = []
    monitor = []
    arm = []
    # grabs only the first 6 gazes
    for idx, gaze_range in enumerate(gaze_ranges[0:7]):
        if idx % 3 == 0:
            face.append(gaze_range)
        elif idx % 3 == 1:
            monitor.append(gaze_range)
        elif idx % 3 == 2:
            arm.append(gaze_range)

    zone_ranges = {
        'face': [
            min(face, key=lambda x: x[0])[0],
            max(face, key=lambda x: x[1])[1],
            min(face, key=lambda x: x[2])[2],
            max(face, key=lambda x: x[3])[3],
        ],
        'monitor': [
            min(monitor, key=lambda x: x[0])[0],
            max(monitor, key=lambda x: x[1])[1],
            min(monitor, key=lambda x: x[2])[2],
            max(monitor, key=lambda x: x[3])[3],
        ],
        'arm': [
            min(arm, key=lambda x: x[0])[0],
            max(arm, key=lambda x: x[1])[1],
            min(arm, key=lambda x: x[2])[2],
            max(arm, key=lambda x: x[3])[3],
        ],
    }
    return zone_ranges


def get_zones():
    """Combine all the steps and return the zones and their ranges"""

    # path = os.getcwd() + '/collection/gaze_data/s99_d1.asc'
    # path = os.getcwd() + '/collection/gaze_data/s99_short.asc'
    path = os.getcwd() + '/collection/gaze_data/s98_d1.asc'
    # path = os.getcwd() + '/collection/gaze_data/s98_short.asc'

    print """
Loading zone gaze data based on calibration in
# %s""" % path
    data = load_file(path)
    print "Getting gazes"
    gazes = get_gazes(data)

    print "Getting gaze x,y mins & maxes"
    gaze_ranges = get_gaze_ranges(gazes)

    print "Getting zone x,y mins & maxes"
    zone_ranges = get_zone_ranges(gaze_ranges)
    # pp.pprint(zone_ranges)
    # print len(zone_ranges)

    return zone_ranges

# pp.pprint(get_zones())
