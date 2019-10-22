# Airsim Multirotor setting

## 1대
```json
{
    "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor"
}
```

## 여러 대
```json
{
    "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor",
    "Vehicles": {
        "Drone1": {
            "VehicleType": "SimpleFlight",
            "X": 4, "Y": 0, "Z": -2, "Yaw": -180
        },
        "Drone2": {
            "VehicleType": "SimpleFlight",
            "X": 8, "Y": 0, "Z": -2
        }
    }
}
```

## 카메라 이미지 처리
```json
{
    "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
    "SettingsVersion": 1.2,
    "CameraDefaults": {
        "CaptureSettings": [
            {
                "ImageType": 0,
                "Width": 640,
                "Height": 480
            }
        ]
    }
}
```

## distance 정보 가져오기
> \Unreal\Plugins\AirSim\Source\UnrealSensors\UnrealDistanceSensor.cpp
```cpp
msr::airlib::real_T UnrealDistanceSensor::getRayLength(const msr::airlib::Pose& pose)
{
    //update ray tracing
    Vector3r start = pose.position;
    Vector3r end = start + VectorMath::rotateVector(VectorMath::front(), pose.orientation, true) * getParams().max_distance;
    //front() 를 down() 으로 바꿈
    //...
    //...
}
```
> \AirLib\include\sensors\distance\DistanceSimpleParams.hpp
```cpp
real_T max_distance = 4000.0f / 100;
real_T max_distance = 4000.0f / 1;
// 100을 1로 바꿔서 최대 4m 가능하게 하기
// 이게 조절이 된건지 아닌지 모르겠으나... 된거로 믿겠음 
```
```json
{
    "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
    "SettingsVersion": 1.2,
    "SimMode": "Multirotor",
    "Vehicles": {
        "Drone1": {
            "VehicleType": "simpleflight",
            "AutoCreate": true,
            "Sensors": {
                "Distance1": {
                    "SensorType": 5,
                    "Enabled" : true
                }
            }
        }
    }
}
```

