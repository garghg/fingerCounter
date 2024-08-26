import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

def detect_gesture(hand_landmarks, hand_label):
    gesture = "Unknown"
    if hand_label == "Right" or hand_label == "Left":
        # Detect thumbs-up gesture
        if hand_landmarks[4][1] < hand_landmarks[3][1] and \
           hand_landmarks[8][1] > hand_landmarks[6][1] and \
           hand_landmarks[12][1] > hand_landmarks[10][1] and \
           hand_landmarks[16][1] > hand_landmarks[14][1] and \
           hand_landmarks[20][1] > hand_landmarks[18][1] and \
            fingerCount == 1:
            gesture = "Thumbs Up"
        # Detect peace sign gesture
        elif hand_landmarks[8][1] < hand_landmarks[6][1] and \
             hand_landmarks[12][1] < hand_landmarks[10][1] and \
             hand_landmarks[16][1] > hand_landmarks[14][1] and \
             hand_landmarks[20][1] > hand_landmarks[18][1] and \
              fingerCount == 2:
            gesture = "Peace Sign"
    return gesture

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        image = cv2.flip(image, 1)
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # To improve performance, optionally mark the image as not writeable to pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Initialize finger count and gesture
        fingerCount = 0
        gesture = "Unknown"

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(hand_landmarks)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                handLandmarks = [[lm.x, lm.y] for lm in hand_landmarks.landmark]

                # Count fingers
                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount += 1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount += 1

                if handLandmarks[8][1] < handLandmarks[6][1]:  # Index finger
                    fingerCount += 1
                if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
                    fingerCount += 1
                if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
                    fingerCount += 1
                if handLandmarks[20][1] < handLandmarks[18][1]:  # Pinky
                    fingerCount += 1

                # Detect gesture
                gesture = detect_gesture(handLandmarks, handLabel)

                # Draw hand landmarks
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

        # Display finger count and gesture
        cv2.putText(image, f'Fingers: {fingerCount}', (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if gesture=="Unknown":
            pass
        else:
          cv2.putText(image, f'Gesture: {gesture}', (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display image
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
