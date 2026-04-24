## Articubot One

This package is set up for ROS 2 Kilted Kaiju with Gazebo Ionic.

Simulation now uses:

- `ros_gz_sim` to launch Gazebo and spawn the robot from `robot_description`
- `gz_ros2_control` for simulated ros2_control hardware
- `ros_gz_bridge` and `ros_gz_image` to bridge `/clock`, lidar, and camera topics into ROS 2

Run the simulator with:

```bash
ros2 launch articubot_one launch_sim.launch.py
```

To load a different packaged world:

```bash
ros2 launch articubot_one launch_sim.launch.py world:=obstacles.world
```
