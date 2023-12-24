from ament_index_python.packages import get_package_share_path
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from launch import LaunchDescription
from launch_ros.actions import Node
import os


def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path('snake_robot_description'), 'urdf', 'snake.urdf')

    robot_description = ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="snake_robot_description",
        executable="snake_robot_description",
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_gui_node = Node(
        package= "joint_state_publisher_gui",
        executable= "joint_state_publisher_gui"
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2"
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])