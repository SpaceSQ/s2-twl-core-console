#!/usr/bin/env python3
import uuid
from s2_14d_tensor import S2TensorGenerator

class SSSUNode:
    def __init__(self, soul_name: str, env_mode: str = "DEEP_SPACE"):
        self.node_id = f"SSSU_{uuid.uuid4().hex[:6].upper()}"
        self.soul_name = soul_name
        self.physics_state = S2TensorGenerator(env_mode).get_context_aware_state()