# debugsnap

## Overview

**debugsnap** is a Python package designed to facilitate debugging by enabling the saving and loading of a **snapshot of the state of the local and global variables** that can then be used for debugging.

This tool is especially useful when you would like to use the functionally of **interactive python for debugging**.

For example in order to itterate on code in a function that is in a state that takes a long time to achieve.

Just **save a snapshot** using the debug console when you are in that state then load the snapshot whenever and as often as you want and itterate.

## Installation

To install debugsnap, run the following command:

```bash
pip install debugsnap
```

## Usage

To use debugsnap, follow these steps:

> ** Warning:** By default a new folder named `tmp_save_snapshot` will be created in your `~` directory and the shapshot files (containing the **global variables**, **local variables** and **information** about any **variable that could not be saved** for any reason) will be saved there. To change the storage location you have to provide a `storage_path`.

1. **Saving the Debugging Snapshot**:
   In your debug session, use the appropriate function to save the current snapshot. For example:
   ```python
    from debugsnap import save_snapshot
    save_snapshot(local_vars=locals(), global_vars=globals())
   ```

2. **Loading the Debugging Snapshot**:
   In a new Python session or an interactive environment, load the saved snapshot:
   ```python
    from debugsnap import load_snapshot
    global_vars, local_vars = load_snapshot()
    globals().update(global_vars)
    locals().update(local_vars)
   ```

## Snippets

In order to make the use of this package easier we suggest adding the following snippets to your VScode, by adding them to `/snippets/python.json` 
```json
    "Save Debug Snapshot": {
        "prefix": "save_snapshot",
        "body": [
            "from debugsnap import save_snapshot",
            "save_snapshot(local_vars=locals(), global_vars=globals())"
        ],
        "description": "Save the current state of local and global variables, excluding specific ones."
    },
    "Load Debug Snapshot": {
        "prefix": "load_snapshot",
        "body": [
            "from debugsnap import load_snapshot",
            "global_vars, local_vars = load_snapshot()",
            "globals().update(global_vars)",
            "locals().update(local_vars)"
        ],
        "description": "Load a saved state into the current global and local variables."
    }
```

## Parameters

Here is an overview over the parameters that the save_snapshot and load_snapshot functions can accept.

In particular the `storage_path` parameter might be releveant to you if you don't want to always save to the same location in your `~` directory.

Varying the `storage_path` is also the easiest way to save multiple different snapshots, as by default each snapshot overwrites the files of the previous snapshot.

```python
def save_snapshot(
    storage_path: Optional[str] = None,
    global_vars: Optional[Dict] = None,
    local_vars: Optional[Dict] = None,
    global_vars_file: str = "global_vars.pkl",
    local_vars_file: str = "local_vars.pkl",
    not_saved_info_file: str = "not_saved_info.pkl",
    exclude: Optional[List] = None,
    strict: bool = False,
    print_location: bool = True,
) -> None:
    """Save the snapshot of local and global variables to disk.

    Parameters:
        storage_path (Optional[str]): The storage path. Defaults to None.
        global_vars (Dict): Global variables to save. Defaults to {}.
        local_vars (Dict): Local variables to save. Defaults to {}.
        global_vars_file (str): Filename for global variables. Defaults to 'global_vars.pkl'.
        local_vars_file (str): Filename for local variables. Defaults to 'local_vars.pkl'.
        not_saved_info_file (str): Filename for the information about variables that couldn't be saved. Defaults to 'not_saved_info.pkl'.
        exclude (List): List of variable names to exclude from saving. Defaults to [].
        strict (bool): Raise exceptions for unpicklable variables if True. Defaults to False.
        print_location (bool): Prints the location where the files where saved. Defaults to True.

    Returns:
        None
    """

def load_snapshot(
    storage_path: Optional[str] = None,
    global_vars_file: str = "global_vars.pkl",
    local_vars_file: str = "local_vars.pkl",
    not_saved_info_file: str = "not_saved_info.pkl",
) -> Tuple[Dict, Dict]:
    """Load the saved snapshot of local and global variables from disk.

    Parameters:
        storage_path (Optional[str]): The storage path. Defaults to None.
        global_vars_file (str): Filename for global variables. Defaults to 'global_vars.pkl'.
        local_vars_file (str): Filename for local variables. Defaults to 'local_vars.pkl'.
        not_saved_info_file (str): Filename for variables that couldn't be saved. Defaults to 'not_saved_info.pkl'.

    Returns:
        Tuple[Dict, Dict]: A tuple containing dictionaries for global and local variables.
    """
```

## Requirements

debugsnap requires Python 3.6 or later. Dependencies include:
- dill >= 0.3.0

## Contributing

Contributions to debugsnap are welcome!

## License

debugsnap is released under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or feedback, please contact v4lue4dded@gmail.com.

## Author

Developed by v4lue4dded. Visit the [GitHub repository](https://github.com/v4lue4dded/debugsnap) for more information and updates.
