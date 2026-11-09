"""YAML config loader for ORB experiments.

Each experiment is a separately named, versioned YAML that overrides the
frozen ORBConfig defaults. This module is intentionally thin: it maps YAML
keys onto ORBConfig fields and records the provenance of every override so a
diff against the frozen baseline is always reconstructable.
"""
import os
from dataclasses import fields
from typing import Any, Dict

import yaml

from .orb_logic import ORBConfig


def _parse_time(value):
    if value is None:
        return None
    if hasattr(value, "hour"):
        return value
    from datetime import time as _time
    parts = str(value).split(":")
    return _time(int(parts[0]), int(parts[1]), int(parts[2]) if len(parts) > 2 else 0)


def load_config(path: str) -> ORBConfig:
    """Load an ORBConfig from a YAML experiment file.

    The YAML may contain a top-level ``config`` mapping of overrides. Unknown
    keys are rejected so a typo cannot silently become a no-op.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path) as f:
        raw = yaml.safe_load(f) or {}

    overrides = raw.get("config") or {}
    if not isinstance(overrides, dict):
        raise ValueError(f"{path}: 'config' must be a mapping")

    valid = {f.name for f in fields(ORBConfig)}
    unknown = set(overrides) - valid
    if unknown:
        raise ValueError(
            f"{path}: unknown config keys {sorted(unknown)}; valid: {sorted(valid)}"
        )

    cfg = ORBConfig()
    for k, v in overrides.items():
        if k in ("or_start", "or_end", "no_new_entry_after", "forced_flatten"):
            v = _parse_time(v)
        setattr(cfg, k, v)
    cfg._source_path = path
    cfg._source_yaml = raw
    return cfg


def config_diff(base: ORBConfig, other: ORBConfig) -> Dict[str, Any]:
    """Return {field: (base_value, other_value)} for every differing field."""
    diff = {}
    for f in fields(ORBConfig):
        bv = getattr(base, f.name, None)
        ov = getattr(other, f.name, None)
        if bv != ov:
            diff[f.name] = {"baseline": bv, "experiment": ov}
    return diff