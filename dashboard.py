"""
Live Dashboard — Displays thinker output and extracted results side by side
using the Textual TUI framework with live-updating panels.
"""

import json
import os
import time

from textual.app import App, ComposeWidget
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, RichLog
from textual.reactive import reactive
from textual import work

STREAM_FILE = os.path.join(os.path.dirname(__file__), "live_stream.txt")
RESULTS_DISPLAY = os.path.join(os.path.dirname(__file__), "novel_results.txt")
LOG_FILE = os.path.join(os.path.dirname(__file__), "thinking_log.jsonl")


class ThinkingPanel(RichLog):
    """Left panel: live thinker output."""
    BORDER_TITLE = "Thinker — Live Derivations"


class ResultsPanel(RichLog):
    """Right panel: extracted novel results."""
    BORDER_TITLE = "Extractor — Novel Results"


class StatsBar(Static):
    """Bottom stats bar."""
    pass


class MathDashboard(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    Horizontal {
        height: 1fr;
    }
    ThinkingPanel {
        width: 1fr;
        border: solid green;
        border-title-color: green;
        padding: 0 1;
    }
    ResultsPanel {
        width: 1fr;
        border: solid cyan;
        border-title-color: cyan;
        padding: 0 1;
    }
    StatsBar {
        height: 3;
        padding: 0 2;
        background: $surface;
        color: $text;
        border-top: solid $primary;
    }
    """

    TITLE = "Math Research Dashboard"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("c", "clear_panels", "Clear"),
    ]

    def compose(self):
        yield Header()
        with Horizontal():
            yield ThinkingPanel(id="thinker", wrap=True, highlight=True, markup=True)
            yield ResultsPanel(id="results", wrap=True, highlight=True, markup=True)
        yield StatsBar(id="stats")
        yield Footer()

    def on_mount(self):
        self._stream_pos = 0
        self._results_pos = 0
        self._round_count = 0
        self._start_time = time.time()

        self.query_one("#thinker", RichLog).write("[bold green]Waiting for thinker to start...[/]")
        self.query_one("#results", RichLog).write("[bold cyan]Waiting for extractor results...[/]")

        self._update_stats()
        self.set_interval(0.5, self._poll_stream)
        self.set_interval(2.0, self._poll_results)
        self.set_interval(1.0, self._update_stats)

    def _poll_stream(self):
        """Poll the live stream file for new thinker output."""
        if not os.path.exists(STREAM_FILE):
            return
        try:
            with open(STREAM_FILE, "r") as f:
                f.seek(self._stream_pos)
                new_text = f.read()
                self._stream_pos = f.tell()

            if new_text:
                panel = self.query_one("#thinker", RichLog)
                # Split into lines for better display
                for line in new_text.split("\n"):
                    if line.strip():
                        panel.write(line)
        except Exception:
            pass

    def _poll_results(self):
        """Poll the results file for new extractions."""
        if not os.path.exists(RESULTS_DISPLAY):
            return
        try:
            with open(RESULTS_DISPLAY, "r") as f:
                f.seek(self._results_pos)
                new_text = f.read()
                self._results_pos = f.tell()

            if new_text:
                panel = self.query_one("#results", RichLog)
                for line in new_text.split("\n"):
                    if line.strip():
                        panel.write(line)
        except Exception:
            pass

    def _update_stats(self):
        """Update the stats bar."""
        elapsed = time.time() - self._start_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)

        # Count rounds from log
        rounds = 0
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r") as f:
                    for line in f:
                        try:
                            entry = json.loads(line.strip())
                            if entry.get("type") == "complete":
                                rounds += 1
                        except (json.JSONDecodeError, KeyError):
                            pass
            except Exception:
                pass

        # Count extracted results
        extractions = 0
        if os.path.exists(RESULTS_DISPLAY):
            try:
                with open(RESULTS_DISPLAY, "r") as f:
                    extractions = f.read().count("Round ")
            except Exception:
                pass

        stats = self.query_one("#stats", StatsBar)
        stats.update(
            f"  Elapsed: {mins:02d}:{secs:02d}  |  "
            f"Derivation Rounds: {rounds}  |  "
            f"Extractions: {extractions}  |  "
            f"Model: gpt-oss-120b  |  "
            f"Press [bold]q[/] to quit, [bold]c[/] to clear"
        )

    def action_clear_panels(self):
        self.query_one("#thinker", RichLog).clear()
        self.query_one("#results", RichLog).clear()


if __name__ == "__main__":
    app = MathDashboard()
    app.run()
