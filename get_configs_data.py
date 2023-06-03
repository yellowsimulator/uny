import yaml

def get_configs_data(config_path: str="configs.yaml") -> dict:
    """Reads the config file and returns a dictionary with the courses.

    Parameters
    ----------
        config_path : path to the config file

    Returns
    -------
        courses : dictionary with the courses
    """
    with open(config_path, 'r') as f:
        courses = yaml.load(f, Loader=yaml.FullLoader)
    return courses