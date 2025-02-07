from fabric import task
import os

@task
def do_deploy(c, archive_path):
    """Distributes an archive to your web server"""

    if not os.path.exists(archive_path):
        return False
    
    # Extract filename from path
    file_name = archive_path.split("/")[-1]
    no_ext = file_name.split(".")[0]
    
    remote_path = f"/tmp/{file_name}"
    release_path = f"/data/web_static/releases/{no_ext}"

    try:
        # Upload the archive to the server
        c.put(archive_path, remote_path)

        # Create the directory for deployment
        c.run(f"mkdir -p {release_path}")

        # Uncompress the archive
        c.run(f"tar -xzf {remote_path} -C {release_path}")

        # Remove the archive from the server
        c.run(f"rm {remote_path}")

        # Move files to correct location
        c.run(f"mv {release_path}/web_static/* {release_path}/")

        # Remove empty web_static folder
        c.run(f"rm -rf {release_path}/web_static")

        # Update the symbolic link
        c.run("rm -rf /data/web_static/current")
        c.run(f"ln -s {release_path} /data/web_static/current")

        return True
    except Exception:
        return False
