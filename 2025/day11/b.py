from functools import cache

with open("./input.txt") as f:
    devices = f.read().splitlines()

device_map: dict[str, tuple[str, ...]] = {}

for device_line in devices:
    device, outputs = device_line.split(":")
    device_map[device.strip()] = tuple(outputs.split())

@cache
def count_paths(device: str, visited_dac: bool, visited_fft: bool) -> int:
    if device == "dac":
        visited_dac = True
    if device == "fft":
        visited_fft = True
    
    if device == "out":
        return 1 if (visited_dac and visited_fft) else 0
    
    if device not in device_map:
        return 0
    
    total = 0
    for nxt in device_map[device]:
        total += count_paths(nxt, visited_dac, visited_fft)
    
    return total

print(count_paths("svr", False, False))