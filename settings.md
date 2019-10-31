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
> C:\Users\multicampus\AppData\Local\Programs\Python\Python36\lib\site-packages\airsim  
airsim 1.2.4 version의 문제
```py
# client.py의 getDistanceSensorData의 lidar_name을
# distance_sensor_name으로 수정!
    def getDistanceSensorData(self, lidar_name = '', vehicle_name = ''):
        return DistanceSensorData.from_msgpack(self.client.call('getDistanceSensorData', distance_sensor_name, vehicle_name))
```
```py
# types.py 맨 아래에 추가
class DistanceSensorData(MsgpackMixin):
    time_stamp = np.uint64(0)
    distance = Quaternionr()
    min_distance = Quaternionr()
    max_distance = Quaternionr()
    relative_pose = Pose()
```

# Last 셋팅
```json
{
  "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
  "SettingsVersion": 1.2,
  "SimMode": "Multirotor",
  "CameraDefaults": {
      "CaptureSettings": [
          {
              "ImageType": 0,
              "Width": 640,
              "Height": 480
          }
      ],
      "Gimbal":{
        "Stabilization":0,
        "Pitch": 0, "Roll":0, "Yaw":0
    }
  },
  "Vehicles": {
      "Drone1": {
          "VehicleType": "simpleflight",
          "X": 0, "Y": 0, "Z": 0, "Yaw": 0,
          "AutoCreate": true,
          "Sensors": {
              "Distance1": {
                  "SensorType": 5,
                  "Enabled" : true
              }
          }
      },
      "Drone2": {
          "VehicleType": "simpleflight",
          "X": 160, "Y": 0, "Z": 0, "Yaw": 0,
          "AutoCreate": true,
          "Sensors": {
              "Distance1": {
                  "SensorType": 5,
                  "Enabled" : true
              }
          }
      },
      "Drone3": {
          "VehicleType": "simpleflight",
          "X": 160, "Y": 160, "Z": 0, "Yaw": 0,
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