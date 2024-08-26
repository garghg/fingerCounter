# Hand Tracking and Finger Counting with MediaPipe and OpenCV

This project demonstrates hand tracking and finger counting using Python's MediaPipe and OpenCV libraries. The application captures video from the webcam, detects hand landmarks, counts fingers, and recognizes specific hand gestures.

## Prerequisites

Ensure you have the following Python libraries installed:

- `mediapipe`
- `opencv-python`

You can install these libraries using pip:

```bash
pip install mediapipe opencv-python
 ```


`## Code Overview
The script uses MediaPipe's Hands solution to detect hand landmarks and OpenCV for real-time video processing. The primary functions and components include:

- **MediaPipe Hands**: Detects hand landmarks and their positions.

- **OpenCV**: Captures video from the webcam, processes frames, and displays results.

### Key Functions

1. **`detect_gesture(hand_landmarks, hand_label)`**:

- Determines the gesture based on hand landmarks.

- Recognizes gestures such as "Thumbs Up" and "Peace Sign."


2. **Main Loop**:

- Captures video frames from the webcam.

- Processes each frame to detect hand landmarks.

- Counts fingers based on landmark positions.

- Recognizes and displays hand gestures.


### Hand Gestures Detected

- **Thumbs Up**: All fingers are curled except the thumb, which is extended.

- **Peace Sign**: The index and middle fingers are extended while other fingers are curled.


## How It Works

1. **Initialize MediaPipe and OpenCV**:

- Setup MediaPipe's Hands solution with specific detection and tracking confidence levels.

- Initialize the webcam feed using OpenCV.

2. **Capture Video Feed**:

- Open the webcam and read frames in a loop.

3. **Process Each Frame**:

- Flip the image horizontally for a mirror view.

- Convert the image to RGB for MediaPipe processing.

- Detect hand landmarks and their positions.

4. **Count Fingers**:

- Count fingers based on the position of landmarks (extended vs. curled).

5. **Detect Gestures**:

- Check landmark positions to identify predefined gestures.

6. **Display Results**:

- Draw hand landmarks and connections on the frame.

- Display the finger count and recognized gesture on the video feed.

7. **Exit**:

- Close the video window when the user presses the 'Esc' key.


## Customization

You can modify the script to recognize additional gestures or adjust detection thresholds:

- **Add New Gestures**: Update the `detect_gesture` function to include more gestures.

- **Adjust Detection Confidence**: Modify `min_detection_confidence` and `min_tracking_confidence` parameters in the MediaPipe setup.

## Troubleshooting

- **Empty Camera Frame**: Ensure your webcam is functioning and correctly connected. If you see "Ignoring empty camera frame," check your webcam drivers or connections.

- **Gesture Recognition Issues**: The detection conditions may need adjustments based on hand size and orientation. Fine-tune the gesture detection logic as needed.

- **Library Errors**: Ensure all dependencies are installed and up-to-date.


### Reference:
- This [article](https://www.geekering.com/categories/computer-vision/marcellacavalcanti/hand-tracking-and-finger-counting-in-python-with-mediapipe/#google_vignette_) was used as a basis for the logic for this project.
