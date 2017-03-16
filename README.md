# Viewer
[fman](https://fman.io) plugin for viewing files and images.

This plugin is meant to be as simple as possible with minimal feature set. If you want add advanced features, like
audio/video players, syntax highlighters or HTML renderer - you can fork the code and modify it however you want.

## Issues (help needed)
- better window management - currently windows are stored in list and not removed on close
- use threads to prevent main process from freezing, while opening big files
- read and display big files in smaller chunks

## Usage
### In fman main view
* <kbd>F3</kbd> - view single file under cursor

### In viewer window
* <kbd>V</kbd> - toggle fixed/variable font
* <kbd>W</kbd> - toggle word wrapping

## Installation
Download and extract it to fman Plugins directory. Restart fman.
