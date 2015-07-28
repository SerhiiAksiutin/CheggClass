import requests
import json


def match_majors(schoolId, domain=None, content_type=None,
                 accept=None, method=None, path=None):
    if domain is None:
        domain = 'http://thor.test3.cheggnet.com:6033'
    if content_type is None:
        content_type = 'application/json'
    if accept is None:
        accept = 'application/json'
    if method is None:
        method = 'POST'
    if path is None:
        path = '/matchSchoolMajors'

    endpoint = '/odin-external/rest/v1/school-major-match/'
    url = domain + endpoint + schoolId + path
    headers = dict()
    headers['Content-Type'] = content_type
    headers['Accept'] = accept
    data = dict()
    data['majorIds'] = ["f9666f64-0f46-462a-8150-877af842590b",
                        "9d556d90-4819-4b33-a265-6c2076bb28aa",
                        "6013b7c5-2016-4277-ac1b-57aeeaace8ac"]
    data = json.dumps(data)
    r = requests.request(
        url=url,
        headers=headers,
        data=data,
        method=method
        )
    return r
resp = match_majors(schoolId = '00051799-5a99-4d82-a7c1-180bb987ced6')
print(resp.content, resp.status_code, type(resp.content))

