# Multithreaded Port Scanner

## Description
A simple and efficient multithreaded port scanner written in Python that checks the open ports on a local system (`localhost`). The program scans the ports within the range 1 to 1024.

## Features
- Utilizes Python's `ThreadPoolExecutor` for concurrent port scanning.
- Has a timeout feature to avoid hanging while scanning.
- Prints open ports in real-time as they are discovered.
- Provides a summary of open ports after scanning.

## Requirements
- Python 3.6 or above
## Usage

To run the port scanner:

```bash
$ python3 multithreaded_port_scanner.py
```
If any open ports are found within the range 1-1024, they will be printed to the console. If none are found, a corresponding message will be displayed.
## Functions

### `scan_local_ports()`

This function initiates the scanning of ports on the local machine in the range 1 to 1024. It returns a list of open ports.

### `scan_port(target, port)`

This function attempts to create a connection to the specified `target` on the specified `port`. If the connection succeeds, it indicates that the port is open, and the function returns `True`. Otherwise, it returns `False`.
## Limitations

- Currently, the tool is set to scan only the localhost. You can modify the `target` variable inside the `scan_local_ports()` function to any other IP if you wish to scan a different host.
- The range is fixed to ports 1-1024. Adjust the `ports` list in the `scan_local_ports()` function to scan a different range.
## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is free and open-source. You can use, modify, and distribute it under the terms of the MIT License. Check the `LICENSE` file for more details.

## Author

[rgerjeki](https://github.com/rgerjeki)

Feel free to reach out if you have any questions or feedback!
