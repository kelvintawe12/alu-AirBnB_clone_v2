from fabric import task
import os
from datetime import datetime

@task
def do_pack(c):
    """Generates a .tgz archive from the web_static folder"""
    
    if not os.path.exists("versions"):
        os.makedirs("versions")
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"
    
    c.run(f"tar -cvzf {archive_path} web_static")
    
    return archive_path if os.path.exists(archive_path) else None
