#!/bin/bash
# Launch the Math Research Pipeline
# Usage: ./run.sh [thinker|extractor|dashboard|all]

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$SCRIPT_DIR/venv/bin/activate"

# Clean up previous run logs
cleanup() {
    echo "Cleaning up previous logs..."
    rm -f "$SCRIPT_DIR/thinking_log.jsonl"
    rm -f "$SCRIPT_DIR/live_stream.txt"
    rm -f "$SCRIPT_DIR/novel_results.jsonl"
    rm -f "$SCRIPT_DIR/novel_results.txt"
}

run_thinker() {
    echo "Starting Thinker Agent..."
    source "$VENV"
    python "$SCRIPT_DIR/thinker.py"
}

run_extractor() {
    echo "Starting Extractor Agent..."
    source "$VENV"
    python "$SCRIPT_DIR/extractor.py"
}

run_dashboard() {
    echo "Starting Dashboard..."
    source "$VENV"
    python "$SCRIPT_DIR/dashboard.py"
}

case "${1:-all}" in
    thinker)
        run_thinker
        ;;
    extractor)
        run_extractor
        ;;
    dashboard)
        run_dashboard
        ;;
    all)
        cleanup
        echo ""
        echo "============================================"
        echo "  Math Research Pipeline"
        echo "============================================"
        echo ""
        echo "Starting all components..."
        echo "  1. Thinker  (background) — generates derivations"
        echo "  2. Extractor (background) — finds novel results"
        echo "  3. Dashboard (foreground) — live TUI display"
        echo ""

        # Start thinker and extractor in background
        run_thinker &
        THINKER_PID=$!
        sleep 2
        run_extractor &
        EXTRACTOR_PID=$!

        # Trap to clean up background processes on exit
        trap "echo 'Shutting down...'; kill $THINKER_PID $EXTRACTOR_PID 2>/dev/null; exit 0" INT TERM EXIT

        sleep 1
        run_dashboard

        # If dashboard exits, kill background processes
        kill $THINKER_PID $EXTRACTOR_PID 2>/dev/null
        echo "Pipeline stopped."
        ;;
    *)
        echo "Usage: $0 [thinker|extractor|dashboard|all]"
        exit 1
        ;;
esac
