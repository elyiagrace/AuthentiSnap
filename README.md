# AuthentiSnap
Tamper-proof Screenshot Verification - know what you're looking at

# Screenshot Snipping Tool with IPFS Hash Storage

This is a desktop application built using **Python** and **Qt**, which allows users to take screenshots, detect the website behind the screenshot (without using optical recognition), and store the screenshot along with a date-time stamp in a resizable, aesthetically pleasing window. The screenshot can be approved by the user, and a hash is generated and stored using IPFS.

## Features

- **Snipping Tool**: Users can snip an area of the screen, and the screenshot is displayed in an aesthetic window.
- **Website Detection**: Automatically detect the website behind the screenshot without using traditional optical recognition methods.
- **IPFS Integration**: Store the screenshot along with its hash in a decentralized manner using IPFS.
- **User Approval**: After taking a screenshot, the user is prompted to approve whether they want to store the screenshot.
- **Resizable Window**: Display the screenshot in a window that can be resized for better viewability.
- **Date-Time Stamp**: Each screenshot is saved with a visible timestamp.
- **Simple UI**: A user-friendly welcome screen with a "Start Snipping" button and an "About" section.

Usage
  Launch the application, and you will be greeted with a small welcome screen.
  Click Start Snipping to begin capturing a portion of the screen.
  Once the screenshot is taken, it will display in a resizable window.
  The website URL behind the screenshot will be detected automatically and shown in the UI.
  A hash will be generated for the screenshot, and it will be stored via IPFS.
  Access stored screenshots and their hashes for reference.
