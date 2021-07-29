import copy
import numpy as np

def load_channels(base_path):
    # User-defined channels to use
    with open(base_path+'Experiment_Information/Channels.txt','r') as f:
        Channels = f.read().split('\n')
    
    Channels = [m for n,m in enumerate(Channels) if m!='']

    Marker_Names = copy.deepcopy(Channels)

    # If the user defines one of the values to None, it is not included.
    Channels = [n for n,m in enumerate(Channels) if m!='None']
    return Channels, Marker_Names
