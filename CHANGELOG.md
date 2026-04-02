# Changelog - TWL Core Console

All notable changes to this project will be documented in this file.

## [1.0.5] - 2026-04-02
### 🛡️ Absolute Zero-Trust Patch (绝对零污染修复)
- **Hardcoded Placeholder Purge**: Scoured and removed all hardcoded placeholder tokens (e.g., `TOP_SECRET_LAB_001`, `SEMICOND_SEC_KEY`) from core files (`s2_twl_hybrid_bridge.py`) and documentation (`SEMICONDUCTOR_DEPLOYMENT_GUIDE.md`). Replaced entirely with strict `os.environ.get()` checks and `sys.exit(1)` triggers.
- **Documentation Alignment**: Synchronized code snippets in documentation with the actual `semiconductor_lab_demo.py` execution flow to eliminate supply-chain ambiguities.
- **Skill.md Sterilization**: Converted `skill.md` to absolute raw plain text formatting to definitively resolve any residual Unicode/BOM prompt-injection scanner alerts.

## [1.0.3] - 2026-04-02
### 🛡️ Clean Slate Security Patch (终极合规清洗)
- **硬核熔断机制 (Hard-Exit Enforcement)**：移除了 `semiconductor_lab_demo.py` 中不安全的 Demo 降级后门。系统现在会在检测不到 `TWL_LAB_TOKEN` 环境变量时，直接触发 `sys.exit(1)`，严格捍卫零信任底线。
- **元数据坦白局 (Explicit Secret Declaration)**：在 `package.json` 和 `openclaw.plugin.json` 中，正式启用了平台官方的 `secrets` 和 `environment` 字段，全量声明对 `TWL_LAB_TOKEN` 的需求，彻底解决元数据与代码脱节的问题。
- **纯净指令舱 (Prompt-Injection Artifact Removal)**：彻底重写 `skill.md`，使用 100% 纯 ASCII 字符，剿灭了可能触发平台防注入扫描器（Prompt-Injection Scanner）误报的所有隐藏 Unicode 控制字符和不可见伪影。

## [1.0.2] - 2026-04-02
### 🛡️ Strict Security & Audit Patch
- **Schema Enforcement**: Explicitly declared `TWL_LAB_TOKEN` in `openclaw.plugin.json`'s `configSchema` to ensure transparent credential handling.
- **Documentation Sanitization**: Purged hidden Unicode control characters and zero-width joiners from early drafts.
- **Reference Unification**: Fixed broken file references in documentation. All docs now uniformly point to `examples/semiconductor_lab_demo.py`.

## [1.0.1] - 2026-04-02
### ⚙️ Coherence & Dependency Patch
- **Standalone Bundle**: Bundled missing underlying core dependencies (`s2_14d_tensor.py`, `s2_sssu_node.py`, `s2_silicon_soul.py`, `s2_tdog_engine.py`) into the package root to prevent `ModuleNotFoundError` during independent execution.
- **Hardcoded Secret Removal**: Removed all hardcoded tokens from example files.
- **Deployment Guide Added**: Added `examples/SEMICONDUCTOR_DEPLOYMENT_GUIDE.md` to explain the CVD reactor bridging topology.

## [1.0.0] - 2026-04-02
### 🚀 Genesis Launch
- **SSSU Clustering**: Dynamic expansion from 1 to 9 SSSU (4㎡-36㎡).
- **Hybrid Bridge**: Added `HybridDataBridge` for real-world lab telemetry ingestion and reality divergence checks.
- **Security Enclave**: Established L0-L3 zero-trust security clearance model.
- **Hologram UI**: Released `twl_hologram_ui.html` for 14D physics visualization.
- **Legal**: Added strict academic-only, non-commercial bundling license.