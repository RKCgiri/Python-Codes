import math

def getFare(Source, Destination):
    # Given data
    bus_stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]
    path_distances = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

    # Convert input stops to uppercase for case insensitivity
    source = Source.upper()
    destination = Destination.upper()

    # Validate input stops
    if source not in bus_stops or destination not in bus_stops:
        return "INVALID OUTPUT"

    # Find the index of source and destination stops
    source_index = bus_stops.index(source)
    destination_index = bus_stops.index(destination)

    # Calculate total distance and fare
    total_distance = 0
    for i in range(source_index, destination_index):
        total_distance += path_distances[i % len(bus_stops)]

    fare = math.ceil(total_distance / 1000) * 5
    return f"{float(fare)} INR"

# Example usage:
source_stop = input("Enter the source stop: ")
destination_stop = input("Enter the destination stop: ")

result = getFare(source_stop, destination_stop)
print("Output Values")
print(result)
