# social_structure_learning


The structure of these scripts is hopefully straightforward. First, running
anaconda you can import the environmental settings with

    $ conda env create -f environment.yml

though most of this code wont work if you don't have the hardware dependencies.
If you do,

    $ python experiment_main.py

from the command line will run the entire experiment. This is a high level
script that imports three main modules, 'instructions', 'stimuli', and
'exit_questions'. In addition to loading generic packages for stimulis
presentation (psychopy) and numeric computations, (numpy) or command line
operations (os) these scripts also call their own helper functions that so
most of the heavy lifting. For each module, these are outlined here:

  instructions:

    - keyboard_input: contains functions for collecting numeric and alphabetic
      key presses, and handling user input to the hardware

    - experiment_ports: contains functions for finding, selecting, and then
      communicating with hardware--in this case, the SD9 for administering
      shock.

  stimuli:

      - experiment_ports: in this case, opens the biopac and signals relevant
        stimulus markers across the experiment.

      - tracker_functions: main interface for coordinating the eyelink hardware
        for collecting gaze data, as well as toggling the experimental display
        between the eyelink and experimental hard drives. configures monitor,
        signals eyelink with relevant stimuli, aligns frames for later analysis,
        performs drift correction across experiment, saves data, etc. etc. etc.

      - design_parameters: loads design parameters like stimulus length, design
        structure, and the indices for marking events

  exit_questions:

      - keyboard_inputs: collects subjects responses to questions from slides in
        instruction_slides/, aggregates these responses with those from
        'instructions' and saves self report data.

let me know if you have any questions :)