"""Tests for competition tracking."""
from src.competition import record_build, get_stats
import os, json

def test_record_build():
    # Clean slate
    if os.path.exists("build_log.json"):
        os.remove("build_log.json")
    count = record_build("hello.py", "module")
    assert count == 1
    stats = get_stats()
    assert stats["total"] == 1
    assert stats["categories"]["module"] == 1
    os.remove("build_log.json")
