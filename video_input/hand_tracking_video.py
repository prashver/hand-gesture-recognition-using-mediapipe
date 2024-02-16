import cv2 as cv
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,  # Set to False for video processing
    max_num_hands=2,
    min_detection_confidence=0.5)

# Open the video file
VIDEO_FILE = 'input_video.mp4'  # Replace 'video.mp4' with the path to your video file
cap = cv.VideoCapture(VIDEO_FILE)

# Get the video frame width and height
frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Codec for saving the video
out = cv.VideoWriter('output_video.mp4', fourcc, 15.0, (frame_width, frame_height))

while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to fit the display window
    frame = cv.resize(frame, (1280, 720))  # Adjust the dimensions as needed

    # Convert the frame to RGB format
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    # Print handedness and draw hand landmarks on the frame.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style(),
            )

    # Display the annotated frame
    cv.imshow('Hand Tracking', frame)

    # Press 'q' to exit the loop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv.destroyAllWindows()
