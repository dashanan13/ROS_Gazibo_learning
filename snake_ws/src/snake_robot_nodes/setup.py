from setuptools import find_packages, setup

package_name = 'snake_robot_nodes'

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
    maintainer='mohit',
    maintainer_email='mohit13@outlook.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "py_node01 = snake_robot_nodes.node01:main",
            "py_snakepubnode01 = snake_robot_nodes.publisher01:main",
            "py_snakesubnode01 = snake_robot_nodes.subscriber01:main", 
            "py_snakeserviceserver01 = snake_robot_nodes.serviceserver01:main",
            "py_snakeserviceclient01 = snake_robot_nodes.serviceclient01:main",
        ],
    },
)
