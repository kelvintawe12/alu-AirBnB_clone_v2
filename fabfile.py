from fabric import task
import os
from datetime import datetime

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of web_static"""
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{time_stamp}.tgz"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = c.run(f"tar -cvzf {archive_path} web_static", hide=False)

    if result.ok:
        return archive_path
    else:
        return None
