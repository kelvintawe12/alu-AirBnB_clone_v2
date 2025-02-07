#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""

from fabric.api import env, put, run
import os

# Set the remote server IP addresses
env.hosts = ['75.101.223.254', '54.236.22.76']
env.user = "ubuntu"

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Args:
        archive_path (str): The path to the archive to deploy.
    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the archive filename and the folder name
        file_name = os.path.basename(archive_path)
        folder_name = file_name.replace(".tgz", "")
        remote_folder = f"/data/web_static/releases/{folder_name}"

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Create the folder where the archive will be uncompressed
        run(f"mkdir -p {remote_folder}")

        # Uncompress the archive to the folder
        run(f"tar -xzf /tmp/{file_name} -C {remote_folder}")

        # Remove the archive from the remote server
        run(f"rm /tmp/{file_name}")

        # Move the contents from web_static to the proper directory
        run(f"mv {remote_folder}/web_static/* {remote_folder}/")

        # Remove the now-empty web_static folder
        run(f"rm -rf {remote_folder}/web_static")

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link linked to the new version
        run(f"ln -s {remote_folder} /data/web_static/current")

        return True
    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
