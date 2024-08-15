# import requests
# from utils.logging import request_logging, response_logging
#
# url = 'https://demowebshop.tricentis.com'
#
#
# def api_request(
#         base_api_url, endpoint, method, data=None, params=None, allow_redirects=False
# ):
#     url = f"{base_api_url}{endpoint}"
#     response = requests.request(
#         method, url, data=data, params=params, allow_redirects=allow_redirects
#     )
#     request_logging(response)
#
#     response_logging(response)
#
#     return response
