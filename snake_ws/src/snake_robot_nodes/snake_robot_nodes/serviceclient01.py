#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
 # using sample interface, explore more at: ros2 interface show example_interface/srv
from example_interfaces.srv import AddTwoInts
 
class AddtwoIntClientNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints_client") # MODIFY NAME
        self.call_add_two_ints_server(1,7)
        self.call_add_two_ints_server(2,8)
        self.call_add_two_ints_server(3,79)
        self.call_add_two_ints_server(4,71)
        self.call_add_two_ints_server(5,72)
        self.call_add_two_ints_server(6,73)
        self.call_add_two_ints_server(7,74)

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints_server")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server Add 2 ints...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b
 
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_ints, a=a, b=b))  #python does not allow futures to have call on arguments and so using, from functools import partial


    def callback_call_add_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r", (e,))


 
def main(args=None):
    rclpy.init(args=args)
    node = AddtwoIntClientNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()