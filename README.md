# IntruderShield - Webcam Intruder Detection and Screen Lock

![banner](assets/banner.png)

This Python script captures an image from your webcam when executed and saves it in the `data/intruder` directory with a timestamp in the filename. Additionally, it simulates keyboard actions to lock the screen after capturing the image.

## Requirements

- Python 3
- OpenCV (cv2) library
- PyAutoGUI library

## Installation

1. Clone this repository to your local machine.

```
git clone https://github.com/arpy8/Laptop_Protection_Trojan.git
cd Laptop_Protection_Trojan
```

2. Install the required Python libraries.

```
pip install opencv-python pyautogui
```

## Usage

1. Run the executable script.

```
start main.exe
```

2. The script will capture an image using your webcam and save it in the `data/intruder` directory.

3. After capturing the image, the script will simulate keyboard actions to lock the screen.

**Note**: Locking the screen with the provided method might not work reliably on all operating systems or configurations. Consider using the alternative locking commands based on your system (Windows, macOS, or Linux) as mentioned in the comments within the script.

## Contributions

Contributions are welcome! If you find any issues or have ideas to improve this project, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).