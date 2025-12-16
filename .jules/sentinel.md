## 2024-08-20 - SSRF Vulnerability via HTTP Redirects
**Vulnerability:** The application is vulnerable to Server-Side Request Forgery (SSRF) because it fetches user-provided URLs without disabling HTTP redirects. An attacker can provide a URL that passes the initial `is_safe_url` check but then redirects to an internal, private IP address.

**Learning:** IP-based validation in `is_safe_url` is insufficient on its own. The root cause is trusting a remote server's redirect response, which allows an attacker to bypass the initial security check and access internal network resources.

**Prevention:** All external HTTP requests that accept user-provided URLs must have redirects explicitly disabled. In Python's `requests` library, this can be done by setting `allow_redirects=False`. For other libraries, consult their documentation.