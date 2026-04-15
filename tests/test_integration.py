"""Integration tests — do Builder's tools work together?"""
from src.hello import greet, build_report

def test_greet_then_report():
    """Greet multiple agents, then build a report."""
    agents = ["Scout", "Scribe", "Alchemist"]
    greetings = [greet(a) for a in agents]
    report = build_report(greetings)
    assert report["built"] == 3
    assert all("Built by Builder" in g for g in report["items"])
    assert report["status"] == "complete"

def test_empty_build():
    """Edge case: empty build."""
    report = build_report([])
    assert report["built"] == 0
    assert report["status"] == "complete"
