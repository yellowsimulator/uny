from pathlib import Path
import requests
import sys
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from get_configs_data import get_configs_data



def get_uio_courses() -> dict:
    """Gets the list of all courses.

    Parameters
    ----------
        url : url to the payload

    Returns
    -------
        payload : dictionary with the payload
    """
    configs = get_configs_data()
    url = configs.get("uio").get("courses_url")
    if url is None:
        raise ValueError("The url is invalid.")
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


if __name__=="__main__":
    data = get_uio_courses()
    print(data)