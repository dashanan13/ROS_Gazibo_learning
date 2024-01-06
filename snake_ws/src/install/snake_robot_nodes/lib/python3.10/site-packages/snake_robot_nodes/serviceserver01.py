#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
# using sample interface, explore more at: ros2 interface show example_interface/srv
from example_interfaces.srv import AddTwoInts
 
class AddtwoIntServerNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("snakeserviceserver01") # MODIFY NAME
        self.server_ = self.create_service(AddTwoInts, "add_two_ints_server", self.callback_add_two_ints)
        self.get_logger().info("snakeserviceserver01 started")
 
    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " + str(request.b) + " = " + str(response.sum) )
        return response
        

def main(args=None):
    rclpy.init(args=args)
    node = AddtwoIntServerNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
