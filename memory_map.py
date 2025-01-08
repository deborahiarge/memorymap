import psutil
import matplotlib.pyplot as plt
import ctypes
import sys

class MemoryMap:
    def __init__(self):
        self.processes = []

    def fetch_memory_info(self):
        """Fetches memory information about all running processes."""
        self.processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                process_info = proc.info
                process_info['memory_percent'] = proc.memory_percent()
                self.processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def display_memory_usage(self):
        """Displays a bar chart of memory usage by process."""
        self.fetch_memory_info()
        processes_sorted = sorted(self.processes, key=lambda x: x['memory_percent'], reverse=True)[:10]

        names = [proc['name'] for proc in processes_sorted]
        memory_percent = [proc['memory_percent'] for proc in processes_sorted]

        plt.figure(figsize=(10, 6))
        plt.barh(names, memory_percent, color='skyblue')
        plt.xlabel('Memory Usage (%)')
        plt.title('Top 10 Memory-Consuming Processes')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()

    def clear_memory_cache(self):
        """Clears memory cache on Windows."""
        # This requires administrative privileges
        try:
            ctypes.windll.kernel32.SetProcessWorkingSetSize(-1, -1, -1)
            print("Memory cache cleared successfully.")
        except Exception as e:
            print(f"Failed to clear memory cache: {e}")

if __name__ == "__main__":
    if not sys.platform.startswith('win'):
        print("MemoryMap is designed to work on Windows.")
        sys.exit(1)

    memory_map = MemoryMap()
    print("Fetching and displaying memory usage...")
    memory_map.display_memory_usage()

    if input("Do you wish to clear memory cache? (y/n): ").strip().lower() == 'y':
        memory_map.clear_memory_cache()