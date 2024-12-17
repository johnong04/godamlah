import cv2
import streamlit as st
import mediapipe as mp
import time
import random

def show():
    st.title("Hand Sign Login")

    # List of hand signs and their corresponding emojis
    hand_signs = {
        'Thumbs Up': '👍',
        'Peace': '✌️',
    }

    # Randomly select a hand sign
    selected_sign_name, selected_sign_emoji = random.choice(list(hand_signs.items()))
    st.subheader(f"Show the '{selected_sign_name}' hand sign to login {selected_sign_emoji}")

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils

    # Placeholder for video frames
    frame_window = st.image([])

    # Open the webcam
    cap = cv2.VideoCapture(0)

    login_success = False
    start_detection = st.button("Start Camera")

    while start_detection and cap.isOpened():
        success, frame = cap.read()
        if not success:
            st.error("Failed to capture image")
            break

        # Flip the frame to make it a mirror view
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract landmark coordinates
                landmarks = hand_landmarks.landmark

                if selected_sign_name == 'Thumbs Up':
                    # Logic for detecting 'Thumbs Up'
                    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
                    thumb_ip = landmarks[mp_hands.HandLandmark.THUMB_IP].y
                    index_mcp = landmarks[mp_hands.HandLandmark.INDEX_FINGER_MCP].y

                    if thumb_tip < thumb_ip < index_mcp:
                        login_success = True

                elif selected_sign_name == 'Peace':
                    # Logic for detecting 'Peace' sign
                    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
                    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y

                    # Check if index and middle fingers are up and other fingers are down
                    if (index_tip < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
                        middle_tip < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
                        ring_tip > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y and
                        pinky_tip > landmarks[mp_hands.HandLandmark.PINKY_PIP].y):
                        login_success = True

                # Draw hand landmarks
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        frame_window.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if login_success:
            st.success("Login Successfully!")
            cap.release()
            cv2.destroyAllWindows()
            st.session_state.page = "loginSuccess" 
            time.sleep(1)
            st.rerun()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show()