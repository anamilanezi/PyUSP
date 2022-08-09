import data_manager as dm
import flight_data as fd
import flight_search as fs
import notification_manager as nm
data = dm.DataManager()

sheet_data = data.get_data()
email = nm.NotificationManager()

# search = fs.FlightSearch()
# for row in sheet_data:
#     if row["iataCode"] == "":
#         city = row["city"]
#         code = search.find_code(city)
#         data.put_data(city=city, iata=code)

departure_city = "SSA"

for row in sheet_data:
    if row["city"] == departure_city or row['iataCode'] == departure_city:
        continue
    else:
        arrival_city = row["city"]
        flight = fd.FlightData(departure_city, arrival_city)
        print(f"{arrival_city}: {flight.price}")
        if flight.flight is None:
            continue
        elif flight.price < row["lowestPrice"]:
            message = f"""Price: R$ {flight.price}
Departure: {flight.departure_city}
DepCode: {flight.departure_airport_code}
Arrival: {flight.arrival_city}
ArrCode: {flight.arrival_airport_code}
Nights in destiny: {flight.nights_in_destiny}
Departure Day: {flight.departure_day}
Return Day: {flight.return_day}"""
            print(message)
            # email.send_notification(message)
