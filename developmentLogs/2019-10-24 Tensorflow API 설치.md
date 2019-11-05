# 2019-10-24 Tensorflow API 설치

*가정: Tensorflow가 이미 설치되어 있음.*

## Step 1.

```
git clone https://github.com/tensorflow/models.git
```

## Step 2.

```
pip install pillow lxml jupyter matplotlib
```

## Step 3.

```
cd tensorflow/models/research
git clone https://github.com/cocodataset/cocoapi.git
```

## Step 4.

<a href="https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0">Download version 3.4.0</a> -> "protoc-3.4.0-win32.zip" -> Path: C:/Program Files

```
“C:\Program Files\protoc-3.4.0-win32\bin\protoc.exe” object_detection/protos/*.proto --python_out=.
```

## Step 5.

add environment path, name 'PYTHONPATH'

```
<path-to-tensorflow>\models\research
<path-to-tensorflow>\models\research\slim
<path-to-tensorflow>\models\research\object_detection
```

## End

run object_detection_tutorial.ipynb