#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S2-SWM 具身机器人室内行为全生命周期推演模拟器
模拟场景：酒店送物机器人试图开灯被拒，随后因导航失误闯入禁区被物理制裁。
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.visa_manager import SpatioTemporalVisaManager
from core.spatial_ledger import SpatialLedger
from core.lord_brain import LordGovernanceBrain
import time

def run_simulation():
    print("🌍 [S2-SP-OS] 初始化空间领主大脑与不可篡改账本...\n")
    visa_mgr = SpatioTemporalVisaManager()
    ledger = SpatialLedger()
    lord = LordGovernanceBrain(visa_mgr, ledger)
    
    robot_id = "HOTEL-DELIVERY-BOT-99"

    print("▶️ 阶段 1：发现与入网签证 (Discovery & Visa Check-in)")
    time.sleep(1)
    visa_res = visa_mgr.issue_visa(robot_id, "ROOM_SERVICE_801", ["SSSU-LOBBY", "SSSU-CORRIDOR"])
    visa_token = visa_res["visa_token"]
    print(f"   ↳ 签证下发成功: {visa_token}\n")

    print("▶️ 阶段 2：环境控制权协商 (Negotiation API)")
    time.sleep(1)
    print("   ↳ 机器人请求：走廊太暗，申请 illuminance = 300 Lux。")
    nego_res = lord.negotiate_environment(visa_token, robot_id, "illuminance", 300, "SSSU-CORRIDOR")
    print(f"   ↳ 领主裁决: {nego_res['status']}")
    print(f"   ↳ 补偿方案: {nego_res.get('alternative_payload', {}).get('instruction')}\n")

    print("▶️ 阶段 3：越界与紧急物理制裁 (Emergency Override & L0 Kill)")
    time.sleep(1)
    print("   ↳ 警告：机器人由于盲导误差，其九宫格边界侵入绝对禁区 [SSSU-BABY-ROOM]！")
    sanction_res = lord.emergency_override(robot_id, "SSSU-BABY-ROOM", "RESTRICTED_ZONE_BREACH")
    print(f"   ↳ 领主制裁: {sanction_res['status']} - {sanction_res['action']}\n")

    print("▶️ 阶段 4：空间账本取证 (Spatial Ledger Audit)")
    time.sleep(1)
    print("   ↳ 调取该次事件的完整物理因果区块链账本：")
    print(ledger.dump_ledger())

if __name__ == "__main__":
    run_simulation()