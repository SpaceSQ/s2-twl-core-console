# TWL Hybrid Deployment Guide: GaN Crystal Growth

## Overview
This guide demonstrates how to connect a real Chemical Vapor Deposition (CVD) reactor to the TWL 14D physical simulation using a zero-trust bridge.

## Deployment Architecture
* Physical End: Real CVD reactor outputting telemetry.
* Virtual End: TWL Quantum Dynamics sandbox (1 SSSU).
* Bridge Layer: `s2_twl_hybrid_bridge.py` via L2 clearance.

## Security Requirement
You MUST export the `TWL_LAB_TOKEN` environment variable before executing the bridge. The system strictly prohibits hardcoded credentials.

## Code Execution
Run the strictly synchronized demo file:
`python3 examples/semiconductor_lab_demo.py`

*(Refer to the source code of `examples/semiconductor_lab_demo.py` for the exact implementation details. Do not use hardcoded placeholder tokens in your production implementation.)*
