import os
import ssl
import sys
import urllib.request

port = os.environ.get("API_PORT", "9000")
use_tls = bool(os.environ.get("TLS_CERTIFICATE_PATH")) and bool(os.environ.get("TLS_PRIVATE_KEY_PATH"))
url = f"{'https' if use_tls else 'http'}://127.0.0.1:{port}/api/app/about"

# The TLS certificate is likely not issued for 127.0.0.1, so don't verify it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ignore HTTP_PROXY/HTTPS_PROXY, a proxy cannot reach our 127.0.0.1
opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), urllib.request.HTTPSHandler(context=ctx))

try:
    with opener.open(url):
        pass
except Exception:
    sys.exit(1)
