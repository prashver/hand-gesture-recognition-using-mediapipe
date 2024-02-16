# Hand Landmark Recognition using MediaPipe

This project is an implementation of hand landmark recognition using the MediaPipe library in Python. The project allows users to perform hand landmark recognition on input images, input videos, and webcam streams.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

Install the required dependencies using the following command:

```bash
pip install opencv-python mediapipe
```

## Usage

### 1. Hand Landmark Recognition on Input Image

To perform hand landmark recognition on an input image, run the following command:

```bash
python hand_tracking_static.py --image_path <path_to_input_image>
```

Replace `<path_to_input_image>` with the path to the input image you want to analyze.

*Demo :-*

Input : <br>
<img src="https://github.com/prashver/hand-landmark-recognition-using-mediapipe/assets/84378440/251b94b2-489d-47a3-80d8-80790b74417c" alt="Hand Landmark Recognition" width="200" height="280"/>

Output : <br>
<img src="https://github.com/prashver/hand-landmark-recognition-using-mediapipe/assets/84378440/fd77514e-5ee5-407e-84fb-df9f83189045" alt="Hand Landmark Recognition" width="300" height="300"/><img src="https://github.com/prashver/hand-landmark-recognition-using-mediapipe/assets/84378440/709a6e60-3277-4446-8827-188f21990701" alt="Hand Landmark Recognition" width="300" height="300"/>


### 2. Hand Landmark Recognition on Input Video

To perform hand landmark recognition on an input video, run the following command:

```bash
python hand_tracking_video.py --video_path <path_to_input_video>
```

Replace `<path_to_input_video>` with the path to the input video you want to analyze.

*Demo :-*

https://github.com/prashver/hand-landmark-recognition-using-mediapipe/assets/84378440/120cff33-71df-4975-bbff-b7bf17243ede


### 3. Hand Landmark Recognition using Webcam

To perform hand landmark recognition using the webcam, run the following command:

```bash
python hand_tracking_cam.py
```

This will start the webcam and perform hand landmark recognition in real-time.

*Demo :-*

https://github.com/prashver/hand-landmark-recognition-using-mediapipe/assets/84378440/8d7d2255-dc9c-4f20-b48d-63dd6550db5b


## How it Works

The project utilizes the MediaPipe library, which provides pre-trained machine learning models for various tasks, including hand landmark recognition. The hand landmark model detects and localizes 21 key points (landmarks) on the hand, including fingertips, joints, and the palm.

The project processes input images or frames from videos/webcam using the hand landmark model provided by MediaPipe. It then draws the detected landmarks on the input image or frame, providing a visual representation of the hand's key points.

## Acknowledgements

This project utilizes the following libraries:

- [MediaPipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)

## License

This project is licensed under the [MIT License](LICENSE).
