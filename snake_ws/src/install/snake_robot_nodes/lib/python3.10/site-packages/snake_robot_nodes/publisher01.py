#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# using sample interface, exploe more at: ros2 interface show example_interface/msg/String
from example_interfaces.msg import String
 
class SnakePublisher01(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("snakepubnode01") # MODIFY NAME
        self.robot_name = "Snake_robot"

        self.publishers_ = self.create_publisher(String, "pubtopic1", 10)
        self.timer_ = self.create_timer(0.5, self.publish_msg)
        self.get_logger().info("pubtopic1 started")

 
    def publish_msg(self):
        msg = String()

        strings = ["pubtopic1: Hello from ", str(self.robot_name)]
        msg.data = ''.join(strings)

        self.publishers_.publish(msg)
 
def main(args=None):
    rclpy.init(args=args)
    node = SnakePublisher01() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
