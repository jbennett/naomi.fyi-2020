import ntpath
import os
from fabric.api import env, sudo, run, local, settings
from fabric.context_managers import cd

env.roledefs = {
  # 'dev': ['r@172.16.1.106'],
  'prod': ['root@172.105.7.15']
}

root_path = '/var/www/html/naomi.fyi'



def quickDeploy():
  updateCode()
  updateAssets()
  setOwnership()

def fullDeploy():
  updateCode()
  updateDeps()
  updateAssets()
  setOwnership()

def updateCode():
  with cd(root_path):
    run('git pull')

def updateAssets():
  with cd(root_path):
    run('npm run prod')

def updateDeps():
  with cd(root_path):
    run('composer install')
    run('npm install')

def setOwnership():
  with cd(root_path):
    run('chown -R www-data:www-data .')

def hash():
  with cd(root_path):
    run("git log --pretty=format:'%h' -n 1");

def uptime():
  run('uptime')