import sqlite3
import math

DB_FILE = "cities.db"

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            name TEXT PRIMARY KEY,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL
        )
    ''')
    conn.commit()

def get_coordinates(conn, city):
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude FROM cities WHERE name = ?", (city,))
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None
    
def add_city(conn, city, lat, lon):
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO cities (name, latitude, longitude) VALUES (?, ?, ?)", (city, lat, lon))
    conn.commit()

def haversine(lat1, lon1, lat2, lon2):
    # Radius of Earth in kilometers
    R = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    # Haversine formula
    a = math.sin(d_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def main():
    conn = sqlite3.connect(DB_FILE)
    create_table(conn)
    
    city1 = input("Enter the name of the first city: ").strip()
    city2 = input("Enter the name of the second city: ").strip()
    
    coords1 = get_coordinates(conn, city1)
    if not coords1:
        lat1 = float(input(f"Unknown city: {city1}. Enter latitude: "))
        lon1 = float(input(f"Enter longitude for {city1}: "))
        add_city(conn, city1, lat1, lon1)
        coords1 = (lat1, lon1)
        
    coords2 = get_coordinates(conn, city2)
    if not coords2:
        lat2 = float(input(f"Unknown city: {city2}. Enter latitude: "))
        lon2 = float(input(f"Enter longitude for {city2}: "))
        add_city(conn, city2, lat2, lon2)
        coords2 = (lat2, lon2)
        
    dist = haversine(coords1[0], coords1[1], coords2[0], coords2[1])
    print(f"Distance between {city1} and {city2} is {dist:.2f} km.")
    
    conn.close()
    
if __name__ == "__main__":
    main()

