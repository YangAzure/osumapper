# -*- coding: utf-8 -*-

#
# Part 8 Taiko hitsounds
#

from hitsound_tools import *

def step8_taiko_hitsounds_set_params(divisor=4, metronome_count=4):
    return divisor, metronome_count

def step8_apply_taiko_hitsounds(obj_array, data, hs_dataset="hs_dataset.npz", params=(4,4)):
    _, _, ticks, _, _, _, _, _, _, _, _, _ = data
    divisor, metronome_count = params

    hs_avail_flags, hs_data = read_hitsound_dataset(hs_dataset)
    hitsounds = apply_hitsounds(hs_avail_flags, hs_data, ticks, divisor=divisor, metronome_count=metronome_count)
    hitsounds = fix_taiko_big_drum(ticks, hitsounds)

    return hitsounds