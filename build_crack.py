#!/usr/bin/env python
import os 
import sys
__dir__name__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__name__ + '/scripts')
import base

def make():
  server_dir = base.get_script_dir() + "/../../server"
  web_apps_dir = base.get_script_dir() + "/../../web-apps"
  oobuild_dir="/home/jacky/project/oobuild/oo-alt"
  if "windows" == base.host_platform():
    oobuild_dir="c:/alt"
  print("patched constants.js")
  base.replaceInFile(server_dir + "/Common/sources/constants.js", "exports.LICENSE_CONNECTIONS = 20", "exports.LICENSE_CONNECTIONS = 500")
  base.replaceInFile(server_dir + "/Common/sources/constants.js", "exports.LICENSE_USERS = 3", "exports.LICENSE_USERS = 300")
  base.replaceInFile(server_dir + "/Common/sources/constants.js", "exports.TEMPLATES_DEFAULT_LOCALE = 'en-US'", "exports.TEMPLATES_DEFAULT_LOCALE = 'zh-CH'")
  base.copy_file(oobuild_dir+"/logo_s.svg",web_apps_dir+"/apps/common/main/resources/img/about/logo_s.svg")
  base.copy_file(oobuild_dir+"/logo_s.svg",web_apps_dir+"/apps/common/main/resources/img/about/logo-white_s.svg")
  base.copy_file(oobuild_dir+"/header-logo_s.svg",web_apps_dir+"/apps/common/main/resources/img/header/header-logo_s.svg")
  base.copy_file(oobuild_dir+"/header-logo_s.svg",web_apps_dir+"/apps/common/main/resources/img/header/dark-logo_s.svg")
  print("logo replaced!")
