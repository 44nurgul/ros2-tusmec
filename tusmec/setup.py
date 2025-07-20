from setuptools import find_packages, setup

package_name = 'tusmec'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nurgul',
    maintainer_email='nurgul@todo.todo',
    description='TODO: ROS2 Publisher-Subscriber',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'talker = tusmec.talker:main',
                'listener = tusmec.listener:main',
        ],
    },
)
