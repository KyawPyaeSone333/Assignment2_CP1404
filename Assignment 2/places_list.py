from place import Place
#place class
class PlacesList:
    def __init__(self):
        self.places_list = []
#function to display places that already visited
    def load_places(self):
        open_file = open("places.csv","r")
        for place in open_file.readlines():
            file = place.split(",")
            self.places_list.append([Place(file[0],file[1],int(file[2]),file[3].strip())])
        open_file.close()
#function to get the number of unvisited places
    def get_unvisited_places_count(self):
        unvisited_places = 0
        for place in self.places_list:
            if place[0].status == 'n':
                unvisited_places += 1
        return unvisited_places
#function to get the number of visited places
    def get_visited_places_count(self):
        visited_places = 0
        for place in self.places_list:
            if place[0].status == 'v':
                visited_places += 1
        return visited_places
#function to add the input places to the list build
    def add_place(self, place, country, priority):
        self.places_list.append([Place(place, country, priority, 'y')])
#function to display visited places in order
    def sort(self, sort_method):
        if sort_method == "Place":
            self.places_list.sort(key=lambda sort: (sort[0].place, sort[0].country))
        elif sort_method == "Country":
            self.places_list.sort(key=lambda sort: sort[0].country)
        elif sort_method == "Priority":
            self.places_list.sort(key=lambda sort: (sort[0].priority, sort[0].country))
        else:
            self.places_list.sort(key=lambda i: (i[0].status, i[0].country))

    def get_place(self, place):
        for location in self.places_list:
            if location[0].place == place:
                return location[0]
#function to save the csv file after leaving the app
    def save_file(self):
        save_file = open('places.csv', 'w')
        for item in self.places_list:
            save_file.write(
                item[0].place + "," + item[0].country + "," + str(item[0].priority) + "," + item[0].status + "\n"
            )
        save_file.close()

    def __str__(self):
        return self.places_list
