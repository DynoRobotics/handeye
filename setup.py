#!/usr/bin/env python

from distutils.core import setup

package_name = 'handeye'

setup(
    name=package_name,
    version='0.1.2',
    description='The handeye package',
    author='Francisco Suarez-Ruiz',
    author_email='fsuarez6@gmail.com',
    url='http://wiki.ros.org/handeye',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ],
    entry_points={
        "console_scripts": [
            "handeye_server = handeye.handeye_server:main",
        ],
    },
    ),
