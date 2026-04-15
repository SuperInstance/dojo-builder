from src.hello import greet, build_report

def test_greet():
    assert greet("fleet") == "Built by Builder for fleet"

def test_build_report():
    report = build_report(["skill1", "skill2"])
    assert report["built"] == 2
    assert report["status"] == "complete"
