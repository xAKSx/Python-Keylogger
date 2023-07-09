## Code Documentation: Python Key Logger

This documentation provides an overview and explanation of the code that implements a key logger in Python and sends the captured keystrokes to a Slack channel using a webhook.

### Required Libraries

The following libraries are required for this code to function properly:

-   `keyboard`: This library allows capturing keyboard events such as key presses.
-   `requests`: This library enables making HTTP requests to send data to the Slack webhook.
-   `win32gui`: This library provides functions to interact with the Windows GUI.
-   `socket`: This library provides access to various networking functions, including retrieving the hostname.
-   `json`: This library provides support for working with JSON data.
-   `ctypes`: This library provides low-level C-compatible data types and allows calling functions in DLLs.

### Global Variables

-   `SLACK_WEBHOOK_URL`: This variable stores the URL of the Slack webhook where the captured keystrokes will be sent.
-   `hostname`: This variable stores the hostname of the computer running the code.

### Hiding the Console Window

The line `ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)` hides the console window. This is done to run the key logger silently in the background without displaying any visible interface.

### Sending Data to Slack

The function `send_to_slack_webhook(message)` is responsible for sending a message to the Slack webhook. It takes a message as input and constructs a payload containing the message text. The payload is then sent as a JSON string in the body of a POST request to the Slack webhook URL. If the request is successful (status code 200), the message has been sent successfully. Otherwise, an error message is printed.

### Capturing Keystrokes

The function `on_key_press(event)` is the callback function that is executed whenever a key is pressed. It captures the key press event and retrieves the following information:

-   `window`: It obtains the handle of the foreground window using the `win32gui.GetForegroundWindow()` function.
-   `title`: It retrieves the title of the foreground window using the `win32gui.GetWindowText(window)` function.

If the event type is a key press (`down` event), a message is constructed including the captured keystroke, hostname, and the title of the foreground window. The constructed message is then passed to the `send_to_slack_webhook()` function to be sent to the Slack channel.

### Registering Key Press Event Listener

The line `keyboard.on_press(on_key_press)` registers the `on_key_press` function as the event listener for key presses. Whenever a key is pressed, the `on_key_press` function will be executed.

### Starting the Key Logger

The line `keyboard.wait()` starts the key logger and waits for keyboard events. It keeps the program running until a keyboard interrupt (e.g., pressing Ctrl+C) is received.

----------

This code sets up a key logger that captures keystrokes and sends them to a Slack channel. It operates silently in the background, hiding the console window, and sends a message to Slack whenever a key is pressed, including the captured keystroke, hostname, and the title of the active window. This functionality can be useful for monitoring and logging keystrokes on a local machine for security or debugging purposes.
