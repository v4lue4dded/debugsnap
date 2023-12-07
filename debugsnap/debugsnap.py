import os
import warnings
from typing import Dict, List, Optional, Tuple

import dill


def check_default_storage_path(storage_path: Optional[str] = None) -> str:
    """Check and create a default storage path for saving variables.

    Parameters:
        storage_path (Optional[str]): The specified storage path. Defaults to None.

    Returns:
        str: The storage path, either the one provided or the default one.
    """
    if storage_path is None:
        home_path = os.path.expanduser("~")
        storage_path = os.path.join(home_path, "tmp_save_snapshot")
        os.makedirs(storage_path, exist_ok=True)
    return storage_path


def pretty_print_dict(d: Dict, indent: int = 4) -> None:
    """Pretty print a dictionary, nested dictionaries will also be indented.

    Parameters:
        d (Dict): The dictionary to print.
        indent (int): The indentation level. Defaults to 4.
    """
    for key, value in d.items():
        print("  " * indent + str(key), end=": ")
        if isinstance(value, dict):
            print()
            pretty_print_dict(value, indent + 1)
        else:
            print(value)


def filter_and_check_picklable(
    vars_dict: Dict, exclude: List[str], strict: bool = False
) -> Tuple[Dict, Dict[str, List[str]]]:
    filtered_vars = {}
    not_saved_info: Dict[str, List[str]] = {"excluded": [], "could_not_save": []}
    for name, var in vars_dict.items():
        if name not in exclude:
            try:
                dill.dumps(var)
                filtered_vars[name] = var
            except Exception:
                if strict:
                    raise Exception(f"Error pickling variable {name}: {var}")
                else:
                    warnings.warn(f"Variable {name} could not be saved.")
                    not_saved_info["could_not_save"].append(name)
        else:
            not_saved_info["excluded"].append(name)
    return filtered_vars, not_saved_info

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
        not_saved_info_file (str): Filename for variables that couldn't be saved. Defaults to 'not_saved_info.pkl'.
        exclude (List): List of variable names to exclude from saving. Defaults to [].
        strict (bool): Raise exceptions for unpicklable variables if True. Defaults to False.
        print_location (bool): Prints the location where the files where saved

    Returns:
        None
    """
    if global_vars is None:
        global_vars = {}
    if local_vars is None:
        local_vars = {}
    if exclude is None:
        exclude = []

    storage_path = check_default_storage_path(storage_path)

    global_vars_to_save, global_vars_not_saved_info = filter_and_check_picklable(
        global_vars, exclude, strict
    )
    local_vars_to_save, local_vars_not_saved_info = filter_and_check_picklable(
        local_vars, exclude, strict
    )

    not_saved_info = {
        "global_vars_not_saved": global_vars_not_saved_info,
        "local_vars_not_saved": local_vars_not_saved_info,
    }


    global_vars_path = os.path.join(storage_path, global_vars_file)
    local_vars_path = os.path.join(storage_path, local_vars_file)
    not_saved_info_path = os.path.join(storage_path, not_saved_info_file)
    with open(global_vars_path, "wb") as f:
        dill.dump(global_vars_to_save, f)
    with open(local_vars_path, "wb") as f:
        dill.dump(local_vars_to_save, f)
    with open(not_saved_info_path, "wb") as f:
        dill.dump(not_saved_info, f)
    if print_location:
        print(f"the snapshot was saved here: {storage_path}")
        print(f"{global_vars_file}")
        print(f"{local_vars_file}")
        print(f"{not_saved_info_file}")


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
    storage_path = check_default_storage_path(storage_path)

    def load_file(file_path):
        try:
            with open(file_path, "rb") as f:
                return dill.load(f)
        except FileNotFoundError:
            warnings.warn(f"No file found at {file_path}")
        except Exception as e:
            warnings.warn(f"An error occurred: {e}")
            raise e
        return {}

    global_vars = load_file(os.path.join(storage_path, global_vars_file))
    local_vars = load_file(os.path.join(storage_path, local_vars_file))
    not_saved_info = load_file(os.path.join(storage_path, not_saved_info_file))

    print("Variables that were not saved by save_snapshot:")
    pretty_print_dict(not_saved_info)

    return global_vars, local_vars


def print_usage_example():
    """Print a usage example for the save_snapshot and load_snapshot functions."""
    print(
        """from debugsnap import save_snapshot\n"""
        + """save_snapshot(local_vars=locals(), global_vars=globals(), exclude=["exit", "quit", "engine", "globals"])\n"""
        + """\n"""
        + """from debugsnap import load_snapshot\n"""
        + """global_vars, local_vars = load_snapshot()\n"""
        + """globals().update(global_vars)\n"""
        + """locals().update(local_vars)\n"""
    )
