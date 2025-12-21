XNAT-NYUAD Documentation repo
=============================

This is a Sphinx-based documentation project for NYUAD XNAT User Documentation.

## Building and Testing Locally

### Prerequisites

- **Python 3.8 or higher** (required for Sphinx 7.2.6)
- pip (Python package manager)

**Note:** If you're on macOS and don't have Python 3.8+, you can install it using:
```bash
# Using Homebrew (recommended)
brew install python@3.11

# Or download from python.org
# https://www.python.org/downloads/
```

### Setup Instructions

1. **Navigate to the docs directory:**
   ```bash
   cd docs
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Building the Documentation

From the `docs/` directory, you can build the documentation using:

```bash
# Build HTML documentation
make html

# Or using sphinx-build directly:
sphinx-build -b html source build/html
```

The built documentation will be in `docs/build/html/`.

### Viewing the Documentation Locally

After building, you can view the documentation by opening `docs/build/html/index.html` in your web browser:

```bash
# On macOS:
open build/html/index.html

# On Linux:
xdg-open build/html/index.html

# On Windows:
start build/html/index.html
```

### Live Reload Development (Recommended)

For a better development experience with auto-reload on file changes, use `sphinx-autobuild`:

```bash
# From the docs/ directory
sphinx-autobuild source build/html
```

This will start a local server (usually at http://127.0.0.1:8000) that automatically rebuilds and reloads when you make changes to the source files.

### Other Build Options

```bash
# Build PDF (requires LaTeX)
make latexpdf

# Clean build directory
make clean

# Show all available build targets
make help
```

### Project Structure

- `docs/source/` - Source RST files and configuration
- `docs/build/` - Generated documentation (created after building)
- `docs/requirements.txt` - Python dependencies
- `docs/Makefile` - Build automation