import os

import folium
from geopy.geocoders import Nominatim
from project.models import db, Restaurant


def main(path: str=""):
    print(path)
    print(f'sqlite:///{path}restaurant.db')
    geolocator = Nominatim(user_agent='Geocoding API')


    engine = db.create_engine(f'sqlite:///{path}restaurant.db', {},  pool_pre_ping=True)



    def get_cord(address:str):
        location = geolocator.geocode(address)
        return location.latitude, location.longitude


    map = folium.Map(location=[49.81712905487126, 24.023224341662562], tiles="Cartodb Positron", zoom_start=25)

    with db.Session(autoflush=False, bind=engine) as session:
        all_user = session.query(Restaurant).all()
        for user in all_user:
            folium.Marker(location=[get_cord(user.adress)[0], get_cord(user.adress)[1]], popup=f'{user.name}',
                          icon=folium.Icon(color='green')).add_to(map)
            print(user.free_seats)
        map.save(f"{path}map.html")


if __name__ == '__main__':
    main()