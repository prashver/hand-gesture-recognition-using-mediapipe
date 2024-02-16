import cv2 as cv
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5)

# Set the desired resolution (e.g., 1280x720)
width, height = 1280, 720

cam = cv.VideoCapture(0)
cam.set(3, width)  # Set the width
cam.set(4, height)  # Set the height

while cam.isOpened():
    success, img_rgb = cam.read()
    if not success:
        print("Camera Frame not available")
        continue

    # Convert image to RGB format
    img_rgb = cv.cvtColor(img_rgb, cv.COLOR_BGR2RGB)
    hands_detected = hands.process(img_rgb)

    # Convert image to RGB format
    img_rgb = cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR)

    if hands_detected.multi_hand_landmarks:
        for hand_landmarks in hands_detected.multi_hand_landmarks:
            drawing.draw_landmarks(
                img_rgb,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style(),
            )

    cv.imshow("Show Video", cv.flip(img_rgb, 1))

    if cv.waitKey(20) & 0xff == ord('q'):
        break

cam.release()
