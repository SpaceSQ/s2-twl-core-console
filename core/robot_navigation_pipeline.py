import logging
from plugins.boundary_scanner import S2BoundaryScanner
from plugins.multimodal_fusion import S2MultimodalPredictor
from plugins.swarm_sync import S2SwarmSyncEngine

class S2RobotNavigationPipeline:
    def __init__(self, robot_id, visa_token, lord_api):
        self.robot_id = robot_id
        self.visa_token = visa_token
        self.lord_api = lord_api # 与空间领主通信的句柄
        
        # 挂载三大神级工具
        self.scanner = S2BoundaryScanner()
        self.fusion = S2MultimodalPredictor()
        self.swarm = S2SwarmSyncEngine()

    def execute_step(self, target_hex: str, sensors: dict, peer_state: dict = None):
        """执行一个物理步进的完整决策闭环"""
        logging.info(f"\n🚀 [ROBOT {self.robot_id}] 发起向 {target_hex} 的步进决策...")

        # 1. 动态边界扫描 (s2-boundary-scanner)
        scan_res = self.scanner.execute_boundary_scan(target_hex, "North", 500)
        if "CRITICAL" in str(scan_res["collision_warnings"]):
            logging.warning("⚠️ 扫描器：检测到物理边界极度逼近！")

        # 2. 多模态融合去幻觉 (s2-multimodal-fusion-predictor)
        fusion_res = self.fusion.generate_causal_prediction(self.fusion._cross_validate_physics(self.fusion._spatio_temporal_alignment(sensors)))
        physics_truth = fusion_res["current_aligned_state"]["resolved_truth"].get("physics_truth", "")
        
        if "Glass" in physics_truth:
            logging.warning("🛑 融合引擎：视觉幻觉破解！前方为透明高硬度玻璃，立即停止物理推进！")
            return {"status": "HALTED_BY_PHYSICS"}

        # 3. 群体同步与路权博弈 (s2-swarm-sync-protocol)
        if peer_state:
            my_state = {"agent_id": self.robot_id, "center_hex": target_hex, "task_type": "EMPTY_CRUISING"}
            swarm_res = self.swarm.execute_swarm_sync(my_state, peer_state)
            if swarm_res.get("status") != "rejected":
                decision = swarm_res.get("right_of_way_arbitration", {}).get("decision")
                if decision == "YIELD":
                    logging.warning(f"⚔️ 群体引擎：轨迹冲突！对方优先级更高，执行物理避让！")
                    return {"status": "HALTED_BY_SWARM_YIELD"}

        # 4. 主权要素协商 (s2-indoor-jurisdiction-negotiator)
        # 如果前置条件都安全，但环境太暗导致下一步 SLAM 将失效
        if sensors.get("camera", {}).get("illuminance_lux", 0) < 10:
            logging.info("💬 导航申请：走廊照度不足 10 Lux，向空间领主发起 [开灯] 协商...")
            nego_res = self.lord_api.negotiate_environment(self.visa_token, self.robot_id, "illuminance", 300, "SSSU-CORRIDOR-01")
            
            if nego_res["status"] == "DENIED_WITH_ALTERNATIVE":
                logging.info(f"🛡️ 领主回复：请求被拒 ({nego_res['reason']})。")
                logging.info(f"🗺️ 载入领主补偿地图：切换至纯雷达拓扑盲导模式继续步进。")

        logging.info(f"✅ 决策闭环通过。机器人安全步进至 {target_hex}。")
        # 5. 上报空间账本
        self.lord_api.ledger.log_event("SSSU-CORRIDOR-01", self.robot_id, "PHYSICAL_STEP_COMPLETE", {"hex": target_hex})
        return {"status": "STEP_SUCCESS"}