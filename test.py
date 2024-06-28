import pandas as pd
import folium

# Function to convert the coordinates from string to tuple
def parse_coordinates(coord_str):
    coord_str = coord_str.strip('"')
    lat, lon = map(float, coord_str.split(','))
    return lat, lon

# Read the CSV file
cities = pd.read_csv('cities.csv')

# Create a map centered on Europe
europe_map = folium.Map(location=[54.5260, 15.2551], zoom_start=5)

# Adjustable variable for circle size scaling
population_scale = 0.03

while True:
    # Get user input for the city name
    city_name = input("Enter the name of the city (or type 'exit' to finish): ")

    if city_name.lower() == 'exit':
        break

    # Check if the city exists in the DataFrame
    city_row = cities[cities['Name'].str.lower() == city_name.lower()]

    if not city_row.empty:
        # Extract city details
        city = city_row.iloc[0]
        lat, lon = parse_coordinates(city['Coordinates'])

        # Add marker and circle to the map
        folium.Marker(
            location=[lat, lon],
            popup=f"{city['Name']} (Population: {city['Population']})"
        ).add_to(europe_map)
        folium.Circle(
            location=[lat, lon],
            radius=city['Population'] * population_scale,
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(europe_map)

        print(f"{city['Name']} added to the map.")
        europe_map.save('europe_map.html')
    else:
        print("City not found in the CSV file.")

# Save the map to an HTML file
europe_map.save('europe_map.html')
print("Map created. Open 'europe_map.html' to view it.")


