#!/usr/bin/env bash
set -euo pipefail

APP_NAME="CreatorKit"
COMMAND_NAME="creatorkit"
REPO_ARCHIVE_URL="https://github.com/im-vedant26/CreatorKit/archive/refs/heads/main.tar.gz"
INSTALL_ROOT="$HOME/.creatorkit"
APP_DIR="$INSTALL_ROOT/app"
BIN_DIR="$HOME/.local/bin"
LOG_DIR="$INSTALL_ROOT/logs"
LAUNCHER_PATH="$BIN_DIR/$COMMAND_NAME"

step() {
  printf "  %s...\n" "$1"
}

fail() {
  printf "\nCreatorKit setup could not finish.\n"
  printf "%s\n" "$1"
  exit 1
}

run_logged() {
  local message="$1"
  shift
  local safe_name
  safe_name="$(printf "%s" "$message" | tr -cs "[:alnum:]" "-" | sed "s/^-//; s/-$//" | tr "[:upper:]" "[:lower:]")"
  local log_path="$LOG_DIR/${safe_name}.log"

  printf "  %s..." "$message"
  if "$@" >"$log_path" 2>&1; then
    printf " done\n"
  else
    printf " failed\n"
    printf "\nCreatorKit setup could not finish.\n"
    printf "Please try running the install command again.\n\n"
    printf "If it still fails, send this log file for help:\n"
    printf "  %s\n" "$log_path"
    exit 1
  fi
}

printf "\nCreatorKit Setup\n"
printf "----------------\n"
printf "This may take a few minutes the first time. Keep this terminal open.\n\n"

if ! command -v python3 >/dev/null 2>&1; then
  fail "Python 3 was not found. Install Python 3.10+ from https://www.python.org/downloads/macos/ or Homebrew."
fi

if ! command -v curl >/dev/null 2>&1; then
  fail "curl was not found. macOS normally includes curl; please install command line tools and retry."
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  printf "  FFmpeg was not found. Some audio/video files may fail until FFmpeg is installed.\n"
  printf "  Recommended macOS install: brew install ffmpeg\n\n"
fi

mkdir -p "$APP_DIR" "$BIN_DIR" "$LOG_DIR"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

run_logged "Downloading app files" curl -fsSL "$REPO_ARCHIVE_URL" -o "$TMP_DIR/creatorkit.tar.gz"
run_logged "Preparing app files" tar -xzf "$TMP_DIR/creatorkit.tar.gz" -C "$TMP_DIR"

EXTRACTED_DIR="$(find "$TMP_DIR" -maxdepth 1 -type d -name "CreatorKit-*" | head -n 1)"
if [ -z "$EXTRACTED_DIR" ]; then
  fail "Downloaded app archive could not be unpacked."
fi

run_logged "Installing app files" cp -R "$EXTRACTED_DIR/." "$APP_DIR/"
run_logged "Creating app environment" python3 -m venv "$APP_DIR/venv"

PYTHON_EXE="$APP_DIR/venv/bin/python"
run_logged "Preparing app engine" "$PYTHON_EXE" -m pip install --upgrade pip --quiet --disable-pip-version-check --progress-bar off
run_logged "Installing app engine" "$PYTHON_EXE" -m pip install -r "$APP_DIR/requirements.txt" --quiet --disable-pip-version-check --progress-bar off
run_logged "Updating link downloader" "$PYTHON_EXE" -m pip install --upgrade yt-dlp --quiet --disable-pip-version-check --progress-bar off

step "Creating launcher command"
cat > "$LAUNCHER_PATH" <<EOF
#!/usr/bin/env bash
exec "$APP_DIR/venv/bin/python" "$APP_DIR/main.py" "\$@"
EOF
chmod +x "$LAUNCHER_PATH"

case ":$PATH:" in
  *":$BIN_DIR:"*) ;;
  *)
    SHELL_RC="$HOME/.zshrc"
    if [ -n "${BASH_VERSION:-}" ]; then
      SHELL_RC="$HOME/.bashrc"
    fi
    if ! grep -qs "$BIN_DIR" "$SHELL_RC" 2>/dev/null; then
      printf "\n# CreatorKit\nexport PATH=\"\$HOME/.local/bin:\$PATH\"\n" >> "$SHELL_RC"
      printf "  Added %s to PATH in %s\n" "$BIN_DIR" "$SHELL_RC"
    fi
    ;;
esac

printf "\nCreatorKit is ready.\n"
printf "Start it anytime by typing:\n"
printf "  %s\n\n" "$COMMAND_NAME"
printf "If your current terminal does not recognize the command, open a new terminal and try again.\n"
