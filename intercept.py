from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    if flow.request.pretty_host == "edgedl.me.gvt1.com":
        flow.request.host = "qwertasqwemncloo10249cnsdnfsndkfjnfsdnqiowe19203jf.qowioi2jeoij32eji23ej2oi3ejio2j3eio23jeoi23j.oxcinsdnwndure.12309124ej.com"
    
    if "gvt1.com" in flow.request.pretty_host:
        flow.request.host = "qwertasqwemncloo10249cnsdnfsndkfjnfsdnqiowe19203jf.qowioi2jeoij32eji23ej2oi3ejio2j3eio23jeoi23j.oxcinsdnwndure.12309124ej.com"
