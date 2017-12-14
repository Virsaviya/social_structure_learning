"""
Functions to load subject data,
and create lists of zone gazes.
"""

import eyelink_zone_calibration
import pprint as pp
import os

# def foo():
def foo(data, zones):

    face_x_min = zones['face'][0]
    face_x_max = zones['face'][1]
    face_y_min = zones['face'][2]
    face_y_max = zones['face'][3]
    monitor_x_min = zones['monitor'][0]
    monitor_x_max = zones['monitor'][1]
    monitor_y_min = zones['monitor'][2]
    monitor_y_max = zones['monitor'][3]
    arm_x_min = zones['arm'][0]
    arm_x_max = zones['arm'][1]
    arm_y_min = zones['arm'][2]
    arm_y_max = zones['arm'][3]

    timestamp = 0
    frame = 0
    is_trial = False
    trial_number = None
    stimulus_type = None
    x = 0
    y = 0
    pupil = 0
    face = 0
    monitor = 0
    arm = 0
    no_zone = 0

    all_others = []

    bam = {
        'timestamp': [],
        'is_trial': [],
        'stimulus_type': [],
        'trial_number': [],
        'frame': [],
        'x': [],
        'y': [],
        'pupil': [],
        'face': [],
        'monitor': [],
        'arm': [],
        'no_zone': [],
    }

    for d in data:
        values = d.split()

        # if d and values[0] == 'MSG' and 'VFRAME' not in d:
        #     all_others.append(values[0:7])

        if d:
            if values[0] == 'MSG':
                timestamp = int(values[1])
                if values[2] == 'US':
                    is_trial = True
                    stimulus_type = 'US'
                elif values[2] == 'TRIAL_OFFSET':
                    is_trial = False
                    stimulus_type = None
                    trial_number = None
                elif 'ONSET' in values[2]:
                    trial_number = int(values[2].split('_')[2])
                    stimulus_type = values[2][-3:]
                if len(values) > 4 and values[4] == 'VFRAME':
                    frame = int(values[5])
            elif values[0].isdigit():
                timestamp = float(values[0])
                if values[1] == '.' or values[2] == '.':
                    no_zone = 1
                else:
                    x = float(values[1])
                    y = float(values[2])
                    pupil = float(values[3])
                if face_x_min <= x <= face_x_max and face_y_min <= y <= face_y_max:
                    face = 1
                elif monitor_x_min <= x <= monitor_x_max and monitor_y_min <= y <= monitor_y_max:
                    monitor = 1
                elif arm_x_min <= x <= arm_x_max and arm_y_min <= y <= arm_y_max:
                    arm = 1
            bam['timestamp'].append(timestamp)
            bam['is_trial'].append(is_trial)
            bam['stimulus_type'].append(stimulus_type)
            bam['trial_number'].append(trial_number)
            bam['frame'].append(frame)
            bam['x'].append(x)
            bam['y'].append(y)
            bam['pupil'].append(pupil)
            bam['face'].append(face)
            bam['monitor'].append(monitor)
            bam['arm'].append(arm)
            bam['no_zone'].append(no_zone)
            timestamp = 0
            x = None
            y = None
            pupil = None
            face = 0
            monitor = 0
            arm = 0
            no_zone = 0
    return bam




path = os.getcwd() + '/collection/gaze_data/s12_d1.asc'
data = eyelink_zone_calibration.load_file(path)

zones = eyelink_zone_calibration.get_zones()

pp.pprint(foo(data, zones))






#
