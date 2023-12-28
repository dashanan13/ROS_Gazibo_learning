#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode01(Node):

    def __init__(self):
        super().__init__("Node01")
        self.get_logger().info("Node 01: Executing")
        self.counter_ = 0
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        
        strings = ["Node01: Timer callbacks ", str(self.counter_)]
        result = ''.join(strings)

        self.get_logger().info(result)



def main(args=None):
    rclpy.init(args=args)

    node = MyNode01()
    rclpy.spin(node)
    rclpy.shutdown()



if __name__ == "__main__":
    main()