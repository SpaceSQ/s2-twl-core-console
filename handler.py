#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from core.visa_manager import SpatioTemporalVisaManager
from core.spatial_ledger import SpatialLedger
from core.lord_brain import LordGovernanceBrain

class S2JurisdictionHandler:
    def __init__(self):
        self.visa_mgr = SpatioTemporalVisaManager()
        self.ledger = SpatialLedger()
        self.lord = LordGovernanceBrain(self.visa_mgr, self.ledger)
        # 单例模式存储，确保进程内的测试数据不丢失
        self._bootstrap_system()

    def _bootstrap_system(self):
        """系统初始化，预发一个签证用于测试"""
        self.test_visa = self.visa_mgr.issue_visa("TEST-BOT-001", "DELIVERY", ["SSSU-CORRIDOR"])

    def process_tool_call(self, args: dict) -> str:
        try:
            action = args.get("action")
            res = {}
            if action == "REQUEST_VISA":
                res = self.visa_mgr.issue_visa(args.get("robot_id"), args.get("task"), args.get("requested_grids", []))
            elif action == "NEGOTIATE_ENV":
                res = self.lord.negotiate_environment(
                    args.get("visa_token"), args.get("robot_id"), args.get("element"), 
                    float(args.get("value", 0)), args.get("grid_id")
                )
            elif action == "REPORT_ANOMALY":
                res = self.lord.emergency_override(args.get("robot_id"), args.get("grid_id"), args.get("violation"))
            else:
                res = {"status": "error", "message": "Unknown action."}
            return json.dumps({"status": "success", "data": res}, ensure_ascii=False)
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    handler = S2JurisdictionHandler()
    if len(sys.argv) > 1:
        print(handler.process_tool_call(json.loads(sys.argv[1])))
    else:
        print(json.dumps({"status": "ready", "message": "S2 Jurisdiction Engine Online"}))