# Debug Snapshot

## Overview

**Debug Snapshot** is a Python package designed to facilitate debugging by enabling the saving and loading of a snapshot of a Python debugging environment. This tool is especially useful when you would like to use the functionally interactive python for debugging, making it easier to analyze and understand complex code behaviors.

## Installation

To install Debug Snapshot, simply run the following command:

```bash
pip install debug_snapshot
```

## Usage

To use Debug Snapshot, follow these steps:

> ** Warning:** By default a new folder named `tmp_save_snapshot` will be created in your `~` directory and the shapshot files will be saved there. To avoid this behaviour you have to provide a `storage_path`.

1. **Saving the Debugging Snapshot**:
   In your debug session, use the appropriate function to save the current snapshot. For example:
   ```python
    from debug_snapshot import save_snapshot
    save_snapshot(local_vars=locals(), global_vars=globals())
   ```

2. **Loading the Debugging Snapshot**:
   In a new Python session or an interactive environment, load the saved snapshot:
   ```python
    from debug_snapshot import load_snapshot
    global_vars, local_vars = load_snapshot()
    globals().update(global_vars)
    locals().update(local_vars)
   ```

# Snippets

In order to make the use of this package easier we suggest adding the following snippets to your VScode, by adding them to `/snippets/python.json` 
```json
    "Save Debug Snapshot": {
        "prefix": "save_snapshot",
        "body": [
            "from debug_snapshot import save_snapshot",
            "save_snapshot(local_vars=locals(), global_vars=globals())"
        ],
        "description": "Save the current state of local and global variables, excluding specific ones."
    },
    "Load Debug Snapshot": {
        "prefix": "load_snapshot",
        "body": [
            "from debug_snapshot import load_snapshot",
            "global_vars, local_vars = load_snapshot()",
            "globals().update(global_vars)",
            "locals().update(local_vars)"
        ],
        "description": "Load a saved state into the current global and local variables."
    }
```

- **Snapshot Saving**: Captures the current snapshot of your Python environment, including variables and their values.
- **Snapshot Loading**: Restores the saved snapshot in a new Python session, allowing for continued exploration and debugging.
- **Non-Picklable Object Handling**: Gracefully manages non-picklable objects, ensuring a robust saving process.

## Requirements

Debug Snapshot requires Python 3.6 or later. Dependencies include:
- dill >= 0.3.0

## Contributing

Contributions to Debug Snapshot are welcome!

## License

Debug Snapshot is released under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or feedback, please contact v4lue4dded@gmail.com.

## Author

Developed by v4lue4dded. Visit the [GitHub repository](https://github.com/v4lue4dded/debug_snapshot) for more information and updates.
