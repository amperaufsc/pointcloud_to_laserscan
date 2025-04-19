import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanFilter(Node):
    def __init__(self):
        super().__init__('scan_filter')
        self.pub = self.create_publisher(LaserScan, '/scan_filtered', 10)
        self.sub = self.create_subscription(LaserScan, '/scan', self.callback, 10)
        
    def callback(self, msg):
        # Remove leituras inválidas
        msg.ranges = [
            r if (msg.range_min < r < msg.range_max) else msg.range_max 
            for r in msg.ranges
        ]
        self.pub.publish(msg)