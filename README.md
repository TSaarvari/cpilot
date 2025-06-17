# cpilot

A cross-platform Python script to display the system uptime on Windows, Linux, and macOS.

## Overview

This project provides a utility to report the amount of time the system has been running (uptime), with support for:

- **Windows** (using native APIs)
- **Linux** (reading `/proc/uptime`)
- **macOS** (using `sysctl` command)

The script is written in Python and demonstrates best practices such as exception handling and subprocess usage.

## Features

- Detects the operating system automatically.
- Handles errors gracefully for unsupported or unexpected conditions.
- Outputs uptime in hours, minutes, and seconds.

## Usage

### Prerequisites

- Python 3.x

### Run the Script

```bash
python copilot_test.py
```

You will see output similar to:

```
System uptime: 4 hours, 32 minutes, 15 seconds
```

## Project Structure

```
copilot_test.py   # Main script to display system uptime
```

## Code Highlights

- Uses `subprocess.run` for executing system commands securely.
- Encapsulates OS-specific logic in separate functions with exception handling.

## License

This project is provided for educational purposes. Please adapt and use according to your needs.

## Contributing

Contributions are welcome! Please fork the repository and open a pull request.

## Author

- [TSaarvari](https://github.com/TSaarvari)
