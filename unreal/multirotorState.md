# 드론의 state 정보

``` json
<MultirotorState> 
{
    'collision': <CollisionInfo> {
        'has_collided': False,
        'impact_point': <Vector3r> {
            'x_val': 0.0,
            'y_val': 0.0,
            'z_val': 0.0
            },
        'normal': <Vector3r> {
            'x_val': 0.0,
            'y_val': 0.0,
            'z_val': 0.0
            },
        'object_id': -1,
        'object_name': '',
        'penetration_depth': 0.0,
        'position': <Vector3r> {
            'x_val': 0.0,
            'y_val': 0.0,
            'z_val': 0.0
            },
        'time_stamp': 0
    },
    'gps_location': <GeoPoint> {
        'altitude': 247.18338012695312,
        'latitude': 47.64686237009147,
        'longitude': -122.13992192162098},
        'kinematics_estimated': <KinematicsState> {
            'angular_acceleration': <Vector3r> {
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 0.0
                },
            'angular_velocity': <Vector3r> {
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 0.0
                },
            'linear_acceleration': <Vector3r> {
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 0.0
                },
            'linear_velocity': <Vector3r> {
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 0.0
                },
            'orientation': <Quaternionr> {
                'w_val': 1.0,
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 0.0
                },
            'position': <Vector3r> {
                'x_val': 0.0,
                'y_val': 0.0,
                'z_val': 6.59033203125
                }
            },
        'landed_state': 0,
        'rc_data': <RCData> {
            'is_initialized': False,
            'is_valid': False,
            'left_z': 0.0,
            'pitch': 0.0,
            'right_z': 0.0,
            'roll': 0.0,
            'switches': 0,
            'throttle': 0.0,
            'timestamp': 0,
            'vendor_id': '',
            'yaw': 0.0
        },
    'timestamp': 1571296991983239680
}
```
```json
<MultirotorState> {   'collision': <CollisionInfo> {   'has_collided': False,
    'impact_point': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'normal': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'object_id': -1,
    'object_name': '',
    'penetration_depth': 0.0,
    'position': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'time_stamp': 0},
    'gps_location': <GeoPoint> {   'altitude': 249.18112182617188,
    'latitude': 47.64686237009147,
    'longitude': -122.13992192162098},
    'kinematics_estimated': <KinematicsState> {   'angular_acceleration': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'angular_velocity': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'linear_acceleration': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0001087188720703125},
    'linear_velocity': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': -7.417903543682769e-05},
    'orientation': <Quaternionr> {   'w_val': 1.0,
    'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 0.0},
    'position': <Vector3r> {   'x_val': 0.0,
    'y_val': 0.0,
    'z_val': 4.592596054077148}},
    'landed_state': 1,
    'rc_data': <RCData> {   'is_initialized': False,
    'is_valid': False,
    'left_z': 0.0,
    'pitch': 0.0,
    'right_z': 0.0,
    'roll': 0.0,
    'switches': 0,
    'throttle': 0.0,
    'timestamp': 0,
    'vendor_id': '',
    'yaw': 0.0},
    'timestamp': 1571297325940775680}
```