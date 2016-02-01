# find_specific_power.py
# 
# Created:  ### 2104, M. Vegh
# Modified: Sep 2105, M. Vegh
#           Jan 2016, E. Botero

# ----------------------------------------------------------------------
#  Find Specific Power
# ----------------------------------------------------------------------

def find_specific_power(battery, specific_energy):
    """determines specific specific power from a ragone curve correlation"""
    
    const_1                 = battery.ragone.const_1
    const_2                 = battery.ragone.const_2
    specific_power          = const_1*10.**(const_2*specific_energy)
    battery.specific_power  = specific_power
    battery.specific_energy = specific_energy