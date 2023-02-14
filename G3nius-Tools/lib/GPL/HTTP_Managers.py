# libs
from requests import get, post


# http get
#
# external:
# from requests import get
#
# note:
# don't manage CTRL+C CTRL+D
#
# version
# 2
def gpl_http_get(URL, params={}, retry_on_503=True, session=None, retry_to_get_valid_response_and_status_code=True, ok_http_codes=[], timeout=None, cookies={}, headers={}, json=None, on_timeout_text=None, on_invalid_http_code_retry_text=None):
    while retry_to_get_valid_response_and_status_code:
        # once get
        try:
            if session:
                if len(headers) > 0:
                    response = session.get(URL, params=params, timeout=timeout, cookies=cookies, headers=headers, json=json)
                else:
                    response = session.get(URL, params=params, timeout=timeout, cookies=cookies, json=json)
            else:
                if len(headers) > 0:
                    response = get(URL, params=params, timeout=timeout, cookies=cookies, headers=headers, json=json)
                else:
                    response = get(URL, params=params, timeout=timeout, cookies=cookies, json=json)
        except TimeoutError:
            if on_timeout_text:
                print(on_timeout_text)
            if not retry_to_get_valid_response_and_status_code:
                return False
        except:
            return None
        else:
            if len(ok_http_codes) == 0 or response.status_code in ok_http_codes:
                # on 502 retry
                if retry_on_503 and response.status_code != 503:
                    return response
                elif not retry_on_503:
                    return response
            elif on_invalid_http_code_retry_text:
                print(on_invalid_http_code_retry_text)

# http post
#
# external:
# from requests import post
#
# note:
# don't manage CTRL+C CTRL+D
#
# version
# 2
def gpl_http_post(URL, payload={}, retry_on_503=True, session=None, retry_to_get_valid_response_and_status_code=True, ok_http_codes=[], timeout=None, cookies={}, headers={}, json=None, on_timeout_text=None, on_invalid_http_code_retry_text=None):
    while retry_to_get_valid_response_and_status_code:
        # once get
        try:
            if session:
                if len(headers) > 0:
                    response = session.post(URL, data=payload, timeout=timeout, cookies=cookies, headers=headers, json=json)
                else:
                    response = session.post(URL, data=payload, timeout=timeout, cookies=cookies, json=json)
            else:
                if len(headers) > 0:
                    response = post(URL, data=payload, timeout=timeout, cookies=cookies, headers=headers, json=json)
                else:
                    response = post(URL, data=payload, timeout=timeout, cookies=cookies, json=json)
        except TimeoutError:
            if on_timeout_text:
                print(on_timeout_text)
            if retry_to_get_valid_response_and_status_code:
                return False
        except Exception as ex:
            print(ex)
            return None
        else:
            if len(ok_http_codes) == 0 or response.status_code in ok_http_codes:
                # on 502 retry
                if retry_on_503 and response.status_code != 503:
                    return response
                elif not retry_on_503:
                    return response
            elif on_invalid_http_code_retry_text:
                print(on_invalid_http_code_retry_text)
