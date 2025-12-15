from urllib.parse import urlparse
import socket
import ipaddress

def is_safe_url(url):
    """
    Checks if a URL is safe to request.
    It is unsafe if the hostname resolves to a private, reserved, or loopback IP address.
    """
    try:
        hostname = urlparse(url).hostname
        if not hostname:
            return False

        ip_address = socket.gethostbyname(hostname)
        ip = ipaddress.ip_address(ip_address)

        # Check if the IP address is private, reserved, or loopback.
        if ip.is_private or ip.is_reserved or ip.is_loopback:
            return False

        return True
    except (socket.gaierror, ValueError):
        # Could not resolve hostname or invalid IP address
        return False
