# 2019-10-21 Object Detection API 2.0 ver

## API 설명

1. run_inference_for_single_image(image)

   - input

     ```
     image : 이미지
     ```

   - return

     ```
     output_dict['num_detections'] : 찾은 객체 수
     output_dict['detection_classes'] : 찾은 객체의 종류
     output_dict['detection_boxes'] : 찾은 객체 박스 좌표
     output_dict['detection_scores'] : 찾은 객체가 클래스일 확률
     output_dict['detection_masks'] : 박스 좌표를 mask로 쓸 수 있도록 convert한 값
     ```

2. run_object_detector(image, target_class_input)

   - input

     ```
     image : 이미지
     target_class_input : String 타입
     ```

   - return

     ```
     output_dict['num_detections'] : 찾은 객체 수
     output_dict['detection_classes'] : 찾은 객체의 종류
     output_dict['detection_boxes'] : 찾은 객체 박스 좌표
     output_dict['detection_scores'] : 찾은 객체가 클래스일 확률
     output_dict['detection_masks'] : 박스 좌표를 mask로 쓸 수 있도록 convert한 값
     output_dict['image'] : 박스 그려진 이미지
     output_dict['target_finded'] : 타겟 검출 결과 (Boolean)
     ```

     

## API 사용 예시

```python
import cv2
import airsim
from drone_object_detection import object_detector

# AI 모델 클래스 객체 생성
detector = object_detector.Detector()

# Airsim 연결
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

# 드론 이륙
airsim.wait_key('Press any key to takeoff')
client.takeoffAsync().join()
time.sleep(0.5)

# 카메라 설정
CAMERA_NAME = ''
IMAGE_TYPE = airsim.ImageType.Scene

# 타겟 설정
target_class = 'person'

# 드론 조작 & 영상 처리
cv2.startWindowThread()
def frame_generator(sec):
  x = 0
  y = 0
  z = -1
  v = 0.5
  x_base = 0
  y_base = 0
  z_base = 0
  for i in range(sec):
      response_image = client.simGetImage(CAMERA_NAME, IMAGE_TYPE)
      np_response_image = np.asarray(bytearray(response_image), dtype="uint8")
      decoded_frame = imdecode(np_response_image, IMREAD_COLOR)
    
      # Object Detect API
      result = detector.start_object_detector(decoded_frame)
    
      # 이미지 출력
      cv2.imwrite('images/output{}.jpg'.format(i), result['image'])
      cv2.imshow('cam', result['image'])
        
      # 드론 이동
      client.moveToPositionAsync(x_base, y_base, z_base, v)
      time.sleep(0.1)
      x_base = x_base + x
      y_base = y_base + y
      z_base = z_base + z

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

frame_generator(10)

# 클린
client.reset()
client.enableApiControl(False)

# Closes all the frames
cv2.destroyAllWindows()
detector.closeDetector()
```

