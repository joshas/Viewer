# Viewer
[fman](https://fman.io) plugin for viewing files and images.

This plugin is meant to be as simple as possible with minimal feature set. If you want add advanced features, like
audio/video players, syntax highlighters or HTML renderer - you can fork the code and modify it however you want.

## Installation
Download and extract it to fman Plugins directory. Restart fman.

## Usage
### In fman main view
* <kbd>F3</kbd> - view single file under cursor

### In text viewer window
* <kbd>V</kbd> - toggle fixed/variable font
* <kbd>W</kbd> - toggle word wrapping

## Issues (help needed)
- use threads to prevent main process from freezing, while opening big files
- better window management - currently windows are stored in list and not removed on close
- read and display big files in smaller chunks (to prevent long loads and have no limit to file size)

## Planned features
- reload current file (F2)
- status bar (lines, encoding in text mode; image resolution, depth in image mode)
- toggle between text and image view (for images only)
- find in file (text search, text mode only)
- hex view

## Future
- look into HTML rendering with QtWebkit (if it is a part of default Qt lib)
- look into playing audio/video, what are limitations? codec support?
