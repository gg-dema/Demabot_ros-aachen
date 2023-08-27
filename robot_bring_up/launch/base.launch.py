#! /usr/bin/env python3


import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    
    usb_port = LaunchConfiguration('usb_port', default='/dev/ttyACM0')
    tb3_param_dir  = LaunchConfiguration('tb3_param_dir', default=os.path.join(
        get_package_share_directory("turtlebot3_bringup"),
        'param', 
        'waffle.yaml'    
        ))
    
    description_usb_port = "Connect USB port with OpenCr"
    description_tb3_param = "Full path to turtlebot3 param file to load"
    return LaunchDescription([
        DeclareLaunchArgument('usb_port', default_value=usb_port, description=description_usb_port), 
        DeclareLaunchArgument('tb3_param_dir', default_value=tb3_param_dir, description=description_tb3_param),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [get_package_share_directory('turtlebot3_bringup'), '/launch/turtlebot3_state_publisher.launch.py']
            )), 
        Node(
            package="turtlebot3_node", 
            executable="turtlebot3_ros", 
            parameters=[tb3_param_dir],
            arguments=['-i', usb_port],
            output='screen',
        )
    ])