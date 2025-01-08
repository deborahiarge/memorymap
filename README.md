# MemoryMap

MemoryMap is a Python program designed to visualize and manage memory usage in Windows systems. It helps users identify memory-intensive processes and provides an option to clear memory cache to improve system performance.

## Features

- Visualizes memory usage by displaying a bar chart of the top 10 memory-consuming processes.
- Option to clear memory cache to free up unused memory, potentially improving system performance.

## Requirements

- Python 3.x
- `psutil` library: Used to fetch process-related information.
- `matplotlib` library: Used for visualizing memory usage.

## Installation

First, ensure you have Python installed. Then, you can install the required libraries using pip:

```shell
pip install psutil matplotlib
```

## Usage

Run the `memory_map.py` script in a Python environment. The script will display a bar chart of the top 10 memory-consuming processes and prompt you to clear the memory cache.

```shell
python memory_map.py
```

## Note

- The program is designed to work on Windows operating systems.
- Clearing memory cache requires administrative privileges. Ensure you run the script with the necessary permissions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.