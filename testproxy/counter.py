from  mitmproxy  import  http
class Counter:
    def __init__(self):
        self.num=0


def request(flow: http.HTTPFlow) -> None:
    if f"v5/stock/batch/quote.json" in  flow.request.pretty_url:
     with open(r'C:\/Users\guili\Desktop\11.json',"r",encoding="utf-8") as f:
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            f.read(),  # (optional) content
            {"Content-Type": "application/json"}  # (optional) headers
        )

addons=[
    Counter()
]