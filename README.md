## Articubot One

This package is set up for ROS 2 Jazzy Jalisco with Gazebo Ionic.

Simulation now uses:

- `ros_gz_sim` to launch Gazebo and spawn the robot from `robot_description`
- `gz_ros2_control` for simulated ros2_control hardware
- `ros_gz_bridge` and `ros_gz_image` to bridge `/clock`, lidar, and camera topics into ROS 2

Run the simulator with:

```bash
ros2 launch articubot_one launch_sim.launch.py
```

If `gz_ros2_control` or `controller_manager` is not installed in your ROS environment yet, you can still bring up Gazebo, sensors, and the robot model without control by running:

```bash
ros2 launch articubot_one launch_sim.launch.py use_ros2_control:=false
```

To load a different packaged world:

```bash
ros2 launch articubot_one launch_sim.launch.py world:=obstacles.world
```
