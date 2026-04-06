# plugins/boundary_scanner.py
import logging

class S2BoundaryScanner:
    def __init__(self):
        self.grid_topology = {
            "Grid_Front": (0, 1), "Grid_FrontRight": (1, 1), "Grid_Right": (1, 0),
            "Grid_BackRight": (1, -1), "Grid_Back": (0, -1), "Grid_BackLeft": (-1, -1),
            "Grid_Left": (-1, 0), "Grid_FrontLeft": (-1, 1)
        }

    def _get_material_by_rcs(self, rcs_value: float) -> str:
        if rcs_value > 20.0: return "Metal/Glass (High Reflectivity, Rigid)"
        elif rcs_value > 5.0: return "Concrete/Brick (Medium Reflectivity, Rigid)"
        elif rcs_value > 1.0: return "Wood/Plastic (Low Reflectivity, Semi-Rigid)"
        else: return "Fabric/Organic (Absorbent, Soft)"

    def _simulate_mmwave_readings(self, heading_vector: str) -> dict:
        return {
            "Grid_Front": {"distance_m": 0.8, "rcs": 25.5},       
            "Grid_FrontRight": {"distance_m": 1.2, "rcs": 8.0},   
            "Grid_Right": {"distance_m": 3.0, "rcs": 0.5},        
            "Grid_BackRight": {"distance_m": 3.0, "rcs": 0.5},
            "Grid_Back": {"distance_m": 3.0, "rcs": 0.5},
            "Grid_BackLeft": {"distance_m": 3.0, "rcs": 0.5},
            "Grid_Left": {"distance_m": 2.5, "rcs": 2.0},         
            "Grid_FrontLeft": {"distance_m": 1.8, "rcs": 25.5}
        }

    def execute_boundary_scan(self, center_hex_code: str, heading_vector: str, step_size_mm: int) -> dict:
        logging.info(f"📡 [感知层] 实体位移 {step_size_mm}mm，启动毫米波边界扫描...")
        sensor_data = self._simulate_mmwave_readings(heading_vector)
        scanned_grids = {}
        collision_warnings = []

        for grid_id, data in sensor_data.items():
            dist = data["distance_m"]
            if dist < 1.0:
                intrusion_pct = round(((1.0 - dist) / 1.0) * 100, 1)
                state = "Cut/Incomplete"
                if intrusion_pct > 80:
                     collision_warnings.append(f"CRITICAL: {grid_id} 极度逼近！")
            else:
                intrusion_pct = 0.0
                state = "Fully Open" if dist >= 2.0 else "Intact but Blocked Adjacent"

            scanned_grids[grid_id] = {
                "topological_state": state,
                "intrusion_percentage": intrusion_pct,
                "distance_to_boundary_m": dist,
                "material_inference": self._get_material_by_rcs(data["rcs"])
            }
        return {"peripheral_grids_state": scanned_grids, "collision_warnings": collision_warnings}