import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/student/AdR/ros2Marcos_ws/p2_kf_adr/install/p2_kf_adr'
