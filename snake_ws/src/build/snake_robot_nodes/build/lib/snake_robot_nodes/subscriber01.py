#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
 # using sample interface, exploe more at: ros2 interface show example_interface/msg/String
from example_interfaces.msg import String
 
class SnakeSubscriber01(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("snakesubnode01") # MODIFY NAME
        self.subscriber_ = self.create_subscription(String, "pubtopic1", self.subscribe_msg, 10)
        self.get_logger().info("subnode01 started")
    
    def subscribe_msg(self, msg):
        self.get_logger().info(msg.data)

 
def main(args=None):
    rclpy.init(args=args)
    node = SnakeSubscriber01() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
