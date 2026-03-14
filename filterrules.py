def is_ad_request(url):
    for domain in blocked_domains:
        if domain in url:
            return True
    return False


def handle_request(url):
    if is_ad_request(url):
        print("Blocked ad request:", url)
        return None
    else:
        print("Allowed:", url)
        return url

for r in requests:
    handle_request(r)
