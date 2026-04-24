import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    package_name = 'articubot_one'
    package_share = get_package_share_directory(package_name)

    world = LaunchConfiguration('world')
    use_ros2_control = LaunchConfiguration('use_ros2_control')
    use_rviz = LaunchConfiguration('use_rviz')
    use_slam = LaunchConfiguration('use_slam')
    use_navigation = LaunchConfiguration('use_navigation')
    use_localization = LaunchConfiguration('use_localization')
    rviz_config = LaunchConfiguration('rviz_config')

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(package_share, 'launch', 'launch_sim.launch.py')),
        launch_arguments={
            'world': world,
            'use_ros2_control': use_ros2_control,
            'use_rviz': use_rviz,
            'use_slam': use_slam,
            'rviz_config': rviz_config,
        }.items(),
    )

    navigation_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(package_share, 'launch', 'navigation_launch.py')),
        launch_arguments={'use_sim_time': 'true'}.items(),
        condition=IfCondition(use_navigation),
    )

    localization_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(package_share, 'launch', 'localization_launch.py')),
        launch_arguments={'use_sim_time': 'true'}.items(),
        condition=IfCondition(use_localization),
    )

    ld = LaunchDescription()

    ld.add_action(DeclareLaunchArgument('world', default_value='empty.world', description='World file from the package worlds directory to load in gz sim'))
    ld.add_action(DeclareLaunchArgument('use_ros2_control', default_value='true', description='Enable gz_ros2_control and controller spawners in simulation'))
    ld.add_action(DeclareLaunchArgument('use_rviz', default_value='true', description='Launch RViz alongside Gazebo'))
    ld.add_action(DeclareLaunchArgument('use_slam', default_value='true', description='Launch slam_toolbox for live map building'))
    ld.add_action(DeclareLaunchArgument('use_navigation', default_value='true', description='Launch navigation (Nav2) stack'))
    ld.add_action(DeclareLaunchArgument('use_localization', default_value='true', description='Launch localization (AMCL)'))
    ld.add_action(DeclareLaunchArgument('rviz_config', default_value=os.path.join(package_share, 'config', 'map.rviz'), description='RViz config file to load'))

    ld.add_action(SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', package_share))

    ld.add_action(sim_launch)
    ld.add_action(navigation_launch)
    ld.add_action(localization_launch)

    return ld
