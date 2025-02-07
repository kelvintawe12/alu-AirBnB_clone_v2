from fabric.api import local

def do_pack():
    """Create a tar.gz archive from the web_static folder"""
    print("Packaging web_static")
    result = local("tar -cvzf web_static.tgz web_static")
    return result
