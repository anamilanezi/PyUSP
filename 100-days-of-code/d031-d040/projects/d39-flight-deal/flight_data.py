import flight_search as fs


class FlightData:
    def __init__(self, flyfrom, flyto):
        self.ffrom = flyfrom
        self.fto = flyto

        search = fs.FlightSearch()

        self.flight = search.find_price(flyfrom, flyto)

        self.price = self.get_("price")

        # self.price = f"£ {self.flight['price']}"
        self.departure_airport_code = self.get_("flyFrom")
        self.departure_city = self.get_("cityFrom")

        self.arrival_airport_code = self.get_("flyTo")
        self.arrival_city = self.get_("cityTo")

        self.nights_in_destiny = self.get_("nightsInDest")
        self.route = self.get_("route")#[0]["utc_departure"].split("T")[0]

        self.departure_day = self.format_day("departure")
        # #self.departure_time_utc = self.format_time("departure")
        #
        self.return_day = self.format_day("return")
        # #self.return_time = self.format_time("return")

    def get_(self, key):
        if self.flight is None:
            return "No direct flights available"
        else:
            return self.flight[key]

    def format_day(self, route):
        if self.flight is not None:
            if route == "departure":
                return self.route[0]["utc_departure"].split("T")[0]
            elif route == "return":
                return self.route[1]["utc_departure"].split("T")[0]
        else:
            return "Invalid request"
    #
    # def format_time(self, route):
    #     if route == "departure":
    #         return self.route[0]["utc_departure"].split("T")[1]
    #     elif route == "return":
    #         return self.route[1]["utc_departure"].split("T")[1]


# fdata = FlightData("Sao Paulo", "Miami")
# print(fdata.flight)
# # print(fdata.price)
# # print("Depature:")
# print(fdata.get_("route"))
# # print(fdata.return_time)
# # print("Return")
# print(fdata.return_day)
# # print(fdata.return_time)
