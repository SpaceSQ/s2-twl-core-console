# plugins/swarm_sync.py
import logging
import math
import os

class S2SwarmSyncEngine:
    def __init__(self):
        self.danger_index_registry = {
            "CARRYING_BOILING_WATER": 95,
            "HUMAN_ESCORT": 100,
            "EMPTY_CRUISING": 20
        }

    def _verify_peer_signature(self, peer_state: dict) -> bool:
        signature = peer_state.get("cryptographic_signature", "")
        return signature == "VALID_S2_FLEET_SIG"

    def _parse_hex_code(self, hex_code: str) -> dict:
        clean_str = hex_code.replace('(', '').replace(')', '').replace('m', '').replace('°', '')
        parts = [float(p.strip()) for p in clean_str.split(',')]
        return {"x": parts[3], "y": parts[4]}

    def execute_swarm_sync(self, my_state: dict, peer_state: dict) -> dict:
        logging.info(f"🤝 [社会层] 拦截到 P2P 广播: 节点 [{peer_state.get('agent_id')}]")

        if not self._verify_peer_signature(peer_state):
            logging.warning("⛔ 警告：节点身份签名验证失败！已丢弃伪造广播。")
            return {"status": "rejected"}

        pos_a = self._parse_hex_code(my_state["center_hex"])
        pos_b = self._parse_hex_code(peer_state["center_hex"])
        distance_mm = math.sqrt((pos_a["x"] - pos_b["x"])**2 + (pos_a["y"] - pos_b["y"])**2)
        
        if distance_mm > 6000:
            return {"status": "no_overlap"}
            
        my_danger = self.danger_index_registry.get(my_state.get("task_type", "EMPTY_CRUISING"), 10)
        peer_danger = self.danger_index_registry.get(peer_state.get("task_type", "EMPTY_CRUISING"), 10)
        
        sync_result = {"status": "overlap", "right_of_way_arbitration": {}}
        if my_danger >= peer_danger:
            sync_result["right_of_way_arbitration"]["decision"] = "PROCEED"
        else:
            sync_result["right_of_way_arbitration"]["decision"] = "YIELD"

        return sync_result