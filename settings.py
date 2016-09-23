import os
from ConfigParser import ConfigParser
from gi.repository import GLib


class Settings(object):
    def __init__(self):
        self.config_dir = os.path.join(GLib.get_user_config_dir(), 'vkpl')
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)
        self.config_file = os.path.join(self.config_dir, 'settings.conf')
        if not os.path.isfile(self.config_file):
            open(self.config_file, 'w').close()

        self.cp = ConfigParser()
        self.read()

        if not self.cp.has_section('general'):
            self.cp.add_section('general')
        if not self.cp.has_section('vk'):
            self.cp.add_section('vk')

        self.write()

    def read(self):
        f = open(self.config_file, 'r')
        self.cp.readfp(f)
        f.close()
        return self.cp

    def write(self):
        f = open(self.config_file, 'w')
        self.cp.write(f)
        f.flush()
        f.close()
