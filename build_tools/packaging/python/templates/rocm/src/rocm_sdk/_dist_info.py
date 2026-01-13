import os

def get_distro_id():
    """Detects if we are running on Fedora."""
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                content = f.read()
                if "ID=fedora" in content:
                    return "fedora"
                if "ID=ubuntu" in content:
                    return "ubuntu"
    except Exception:
        pass
    return "unknown"
