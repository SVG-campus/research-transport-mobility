"""Smoke: HF domain charter stream schema for research-transport-mobility."""

from __future__ import annotations

from datasets import load_dataset


def test_transport_ag_news_stream_schema() -> None:
    rows = list(
        load_dataset("fancyzhx/ag_news", split="train", streaming=True).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "label" in r
