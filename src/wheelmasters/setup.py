from setuptools import setup
import os
from glob import glob

package_name = 'wheelmasters'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,'launch'),glob('launch/*.py')),
        (os.path.join('share', package_name,'meshes'),glob('meshes/*.STL')),
        (os.path.join('share', package_name,'urdf'),glob('urdf/*.xacro')),
        (os.path.join('share', package_name,'config'),glob('config/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='osinachi',
    maintainer_email='osinachi99@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
