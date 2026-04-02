#!/usr/bin/env python3
import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from s2_twl_hybrid_bridge import SecurityEnclave, TraditionalLabCabin, HybridDataBridge
from s2_causal_dynamics import BigBangEngine

def run_lattice_optimization_cycle():
    print("[TWL] Starting Semiconductor Lab Demo (Strict Secure Mode)")
    
    # [最高安全级别修复] 强制获取环境变量。没有妥协，没有默认值。
    secure_token = os.environ.get("TWL_LAB_TOKEN")
    if not secure_token:
        print("[CRITICAL ERROR] TWL_LAB_TOKEN is missing in environment variables.")
        print("[CRITICAL ERROR] Execution aborted to maintain zero-trust security protocol.")
        sys.exit(1) # 触发硬退出，彻底拒绝不安全的执行

    semiconductor_sim = BigBangEngine(space_id="GaN_Growth_Chamber")
    real_lab = TraditionalLabCabin("Semiconductor_National_Lab_CVD_03")
    
    # 使用安全的 token 建立 L2 级沙箱
    enclave = SecurityEnclave(lab_token=secure_token, clearance_level="L2")
    bridge = HybridDataBridge(real_lab, semiconductor_sim, enclave)

    real_lab.ingest_real_world_data({"Barometric_Tide": 1050.5, "HVAC_气象_temp_c": 1050.0})
    bridge.sync_reality_to_virtual()
    semiconductor_sim.tick()
    divergence = bridge.compare_time_series()
    
    if divergence > 0.5:
        bridge.advise_real_world({"action": "SLOW_COOLING", "target_temp": 1020.0})

if __name__ == "__main__":
    run_lattice_optimization_cycle()
