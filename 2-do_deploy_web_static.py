#!/usr/bin/python3
from fabric.api import env, put, run
import os

# Define the web servers
env.hosts = ['75.101.223.254', '54.236.22.76']  # Replace with the correct IPs if needed
env.user = 'ubuntu'  # Replace with your username if it's different

def do_deploy(archive_path):
    """
    Deploys the archive to the web servers.
    Args:
        archive_path (str): The path to the archive file to be deployed.
    Returns:
        bool: True if the deployment was successful, False otherwise.
    The function performs the following steps:
    1. Checks if the archive file exists.
    2. Uploads the archive to the /tmp directory on the web server.
    3. Extracts the archive to a target directory.
    4. Deletes the archive from the /tmp directory.
    5. Moves the extracted content to the correct directory.
    6. Removes the now unnecessary directory.
    7. Removes the current symbolic link.
    8. Creates a new symbolic link pointing to the new release.
    If any step fails, the function prints an error message and returns False.
    """
    """Deploys the archive to the web servers."""
    
    if not os.path.exists(archive_path):
        print("Archive does not exist")
        return False
    
    try:
        # Upload the archive to /tmp
        put(archive_path, '/tmp/')
        
        # Extract the archive
        filename = archive_path.split("/")[-1]
        file_no_extension = filename.split(".")[0]
        
        # Create the target directory for the extracted files
        run(f"mkdir -p /data/web_static/releases/{file_no_extension}/")
        
        # Uncompress the archive
        run(f"tar -xzf /tmp/{filename} -C /data/web_static/releases/{file_no_extension}/")
        
        # Delete the archive from the web server
        run(f"rm /tmp/{filename}")
        
        # Move the extracted content to the correct directory
        run(f"mv /data/web_static/releases/{file_no_extension}/web_static/* /data/web_static/releases/{file_no_extension}/")
        
        # Remove the now unnecessary directory
        run(f"rm -rf /data/web_static/releases/{file_no_extension}/web_static")
        
        # Remove the current symbolic link
        run(f"rm -rf /data/web_static/current")
        
        # Create a new symbolic link pointing to the new release
        run(f"ln -s /data/web_static/releases/{file_no_extension}/ /data/web_static/current")
        
        print("New version deployed!")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False
