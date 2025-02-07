#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""

from fabric import task
from datetime import datetime
import os

@task


def do_pack(c):
    """
    Generates a .tgz archive from th
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create an archive filename using the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"

    # Run the tar command to create the archive
    result = c.local(f"tar -cvzf {archive_path} web_static", hide=False)

    # Check if the command failed
    if result.failed:
        print("Packaging failed.")
        return None

    print(f"Archive created: {archive_path}")
    return archive_path