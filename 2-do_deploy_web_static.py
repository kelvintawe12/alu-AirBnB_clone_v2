#!/usr/bin/python3
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['75.101.223.254', '54.236.22.76']

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
                return False
        from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return Falsefrom fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        remote_path = "/tmp/{}".format(file_name)
        release_dir = "/data/web_static/releases/{}/".format(base_name)

        # Upload the archive to /tmp/
        put(archive_path, remote_path)

        # Create release directory
        run("mkdir -p {}".format(release_dir))

        # Extract the archive to the release directory
        run("tar -xzf {} -C {}".format(remote_path, release_dir))

        # Remove the uploaded archive
        run("rm {}".format(remote_path))

        # Move contents from web_static to the release directory
        run("mv {0}/web_static/* {0}/".format(release_dir))

        # Remove the web_static directory
        run("rm -rf {}/web_static".format(release_dir))

        # Remove the current symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(release_dir))

        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False