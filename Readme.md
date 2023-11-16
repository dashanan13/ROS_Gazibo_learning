Concepts

RViz, Gazebo, and MoveIt are three distinct tools commonly used in the field of robotics, particularly for robot simulation, visualization, and motion planning. Here's a brief overview of each:

RViz (Robot Visualization):
Purpose: RViz is a 3D visualization tool that allows users to visualize sensor data, robot models, and other information from a robotic system in real-time.
Features: It provides a graphical interface to display information such as point clouds, robot models, sensor data, and more. RViz is often used for debugging, monitoring, and gaining insights into the robot's perception and state.
Use Case: RViz is commonly used during the development and testing phases of a robot to visualize and understand how the robot perceives its environment.

Gazebo:
Purpose: Gazebo is a robot simulation tool that provides a physics engine for simulating the dynamics of robots and their interactions with the environment.
Features: Gazebo simulates the physics of objects, sensors, and environmental factors, allowing users to test and validate robot behaviors in a simulated environment. It is often used to simulate robot movements, test control algorithms, and assess the robot's response to different scenarios.
Use Case: Gazebo is commonly used for testing and validating robotic algorithms before deploying them on a physical robot. It helps reduce the risk of errors and allows developers to iterate quickly.

MoveIt:
Purpose: MoveIt is a motion planning framework designed for manipulation tasks. It helps robots plan and execute complex motion sequences, especially in scenarios involving robotic arms and manipulators.
Features: MoveIt provides tools for motion planning, collision detection, inverse kinematics, and trajectory execution. It allows users to plan paths for robots in a given environment, taking into account the robot's physical constraints and the surrounding obstacles.
Use Case: MoveIt is commonly used in applications where precise and collision-free motion planning is crucial, such as in industrial automation, grasping objects, and manipulation tasks.
In summary, RViz is a visualization tool, Gazebo is a simulation tool, and MoveIt is a motion planning framework. These tools are often used together in the development and testing of robotic systems to facilitate a comprehensive approach from visualization to simulation and motion planning.


Install: 
Ubuntu desktop: https://phoenixnap.com/kb/how-to-install-a-gui-on-ubuntu
Configure Chrome desktop: https://idroot.us/install-chrome-remote-desktop-ubuntu-20-04/
Install ROS2: https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html, check version: printenv ROS_DISTRO
Install Moveit: https://docs.ros.org/en/kinetic/api/moveit_tutorials/html/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html
