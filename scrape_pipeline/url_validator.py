import urllib.request 
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError


def validate_url(url):
    """
    Validate if the provided URL is properly formatted and reachable.

    Parameters:
        url (str): The URL to validate.

    Returns:
        dict: A dictionary containing:
            - 'valid' (bool): Whether the URL is valid and reachable.
            - 'error_message' (str): An error message or status description.
    """
    response = {
        "valid": False,
        "error_message": ""
    }

    parsed_url = urlparse(url)
    if not parsed_url.scheme or not parsed_url.netloc:
        response["error_message"]="Invalid URL: missing scheme or hostname/domain"
        return response
    
    # # Attempt to send a request to the URL to check if it's reachable
    try:
        urllib.request.urlopen(url)
        response["valid"]=True
        response["error_message"]="URL is valid and reachable."
    except HTTPError as e:
         response["error_message"] = f"HTTP error occurred: {e.code} - {e.reason}"
    except URLError as e:
        response["error_message"] = f"URL error occurred: {e.reason}"

    return response