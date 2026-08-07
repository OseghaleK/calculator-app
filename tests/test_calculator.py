"""Tests for parsing, history display, and the REPL loop."""

import pytest

from app.calculator import parse_number, show_history, run


def fake_input(responses):
    """Stand-in for input() that replays a list of answers in order."""
    replies = iter(responses)
    return lambda _prompt="": next(replies)


@pytest.mark.parametrize(
    "text, expected",
    [("187.5", 187.5), ("-25", -25.0), ("22.5", 22.5), ("0", 0.0)],
)
def test_parse_number_valid(text, expected):
    assert parse_number(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "3.4.5", "forty five"])
def test_parse_number_invalid(text):
    with pytest.raises(ValueError, match="is not a valid number"):
        parse_number(text)


def test_show_history_when_empty(capsys):
    show_history([])
    assert "No calculations yet." in capsys.readouterr().out


def test_show_history_lists_entries(capsys):
    show_history(["187.5 - 143.25 = 44.25", "15 * 8 = 120"])
    output = capsys.readouterr().out
    assert "1. 187.5 - 143.25 = 44.25" in output
    assert "2. 15 * 8 = 120" in output


def test_repl_exits(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["exit"]))
    run()
    assert "Goodbye." in capsys.readouterr().out


def test_repl_help(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["help", "exit"]))
    run()
    assert "Commands: help, history, exit" in capsys.readouterr().out


def test_repl_unknown_command(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["banana", "exit"]))
    run()
    assert "Unknown command" in capsys.readouterr().out


def test_repl_calculates_and_records(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        fake_input(["subtract", "187.5", "143.25", "history", "exit"]),
    )
    run()
    output = capsys.readouterr().out
    assert "Result: 44.25" in output
    assert "1. 187.5 - 143.25 = 44.25" in output


def test_repl_history_when_empty(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["history", "exit"]))
    run()
    assert "No calculations yet." in capsys.readouterr().out


def test_repl_invalid_number(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", fake_input(["add", "abc", "exit"]))
    run()
    assert "Invalid input" in capsys.readouterr().out


def test_repl_divide_by_zero(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input", fake_input(["divide", "45", "0", "exit"])
    )
    run()
    assert "Math error" in capsys.readouterr().out
