#!/usr/bin/env python3
class S2TensorGenerator:
    def __init__(self, env_mode="EARTH_RESIDENTIAL"):
        self.mode = env_mode
    def get_context_aware_state(self):
        return {
            "Light_光": {"lux": 300}, "HVAC_气象": {"temp_c": 24.0},
            "Barometric_Tide": 1013.25, "Thermal_Flux": 0.5,
            "Fluid_Dynamic_Vector": 0.05, "Spatial_Entropy": 0.0
        }