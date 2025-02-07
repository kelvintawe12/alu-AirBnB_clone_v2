#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['75.101.223.254', '54.236.22.76']

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['75.101.223.254', '54.236.22.76']

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
    
from datetime import datetime 
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['75.101.223.254', '54.236.22.76']

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
from fabric.api import env, local
from datetime import datetime
from os.path import exists
from 2-do_deploy_web_static import do_deploy

env.hosts = ['<IP web-01>', '<IP web-02>']  # Replace with actual server IPs

def do_pack():
    """Generate a .tgz archive from the web_static folder"""
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("Packing failed: {}".format(e))
        return None

def deploy():
    """Create and distribute an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)