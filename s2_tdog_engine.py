#!/usr/bin/env python3
class TDOG_Engine:
    def __init__(self):
        self.objects_in_space = {}
    def spawn_object(self, obj_name: str, level: str, reality_type: str, physics_impact: dict):
        self.objects_in_space[obj_name] = physics_impact
    def apply_physics_impact(self, tensor_state: dict):
        pass