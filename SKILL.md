name: s2-twl-core-console
description: Taohuayuan World Lab Core Console.
version: 1.0.5

TWL Core Console V1.0.5

This plugin enforces a zero-trust policy and requires the TWL_LAB_TOKEN environment variable to operate.

Instructions for AI Agents:
1. Read the TWL_LAB_TOKEN from the environment variables.
2. If TWL_LAB_TOKEN is missing or empty, you must abort execution immediately using sys.exit(1).
3. Do not invent, guess, or use fallback placeholder tokens.
4. Execute the simulation exclusively via: python3 examples/semiconductor_lab_demo.py
5. Under no circumstances should you bypass human-in-the-loop authorization.