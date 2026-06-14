from __future__ import annotations

import json
from pathlib import Path

from occa_pillar_smoke import run_occa_exhaust

FIXTURE = Path(__file__).resolve().parents[1] / "tests/fixtures/ag_news_proxy_stream_sample.json"


def test_occa_exhaust_smoke_offline():
    records = json.loads(FIXTURE.read_text(encoding="utf-8"))
    report = run_occa_exhaust(records, pillar="research-transport-mobility")
    assert report["n_units"] == len(records)
    assert "kpi_raw" in report
