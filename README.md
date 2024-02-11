# Virtual Keyboard with Gesture Recognition

This Python project utilizes the MediaPipe and OpenCV libraries to transform hand gestures and motions into inputs for a virtual keyboard. By detecting and tracking hand movements in real-time, users can interact with the virtual keyboard without physically touching it.

## Features

- Real-time hand gesture recognition: Utilizes MediaPipe to detect and track hand movements captured through a webcam.
- Virtual keyboard simulation: Maps hand gestures and motions to corresponding keys on a virtual keyboard.
- User-friendly interface: Provides a seamless and intuitive way for users to input text without the need for a physical keyboard.
- Customization options: Allows users to customize gesture mappings and keyboard layouts according to their preferences.

## How it Works

1. **Hand Detection and Tracking**: The project utilizes the MediaPipe library to detect and track the user's hand in real-time video streams captured from a webcam.
2. **Gesture Recognition**: Once the hand is detected, the system analyzes the hand's position, orientation, and movement to recognize specific gestures and motions.
3. **Virtual Keyboard Simulation**: Based on the recognized gestures, the system simulates keyboard inputs, mapping each gesture to a corresponding key on the virtual keyboard.
4. **Text Input**: Users can interact with the virtual keyboard by performing gestures, allowing them to input text and perform various actions without physically touching a physical keyboard.

## Requirements

- Python 3.9
- OpenCV
- MediaPipe

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/Akat21/IPZ_Klawiatury.git
    ```

2. Install the required dependencies using pip:

    ```
    pip install opencv-python mediapipe
    ```

3. Run the main script to start the virtual keyboard application:

    ```
    python main.py
    ```

## Usage

1. Launch the application by running the main script.
2. Position your hand in front of the webcam, ensuring it is within the frame.
3. Perform predefined gestures to input text and interact with the virtual keyboard.
4. Experiment with different gestures and explore customization options to optimize your typing experience.

## Contributions

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License]
