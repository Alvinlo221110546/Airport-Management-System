def baggage_capacity():  
    print("Hi, we will help you to choose which items you can include in our airplane ")  
    print("For your information, our airplane's maximum baggage capacity is 1000 kgs")  
    total_capacity = 1000  
    num_items = int(input("How many items you have on the candidate? : "))  
    print("Please input the name, the weight, and the price for item: ")  

    items = []  
    for i in range(num_items):  
        name, weight, price = input().split()  
        weight = int(weight)  
        price = int(price)  
        items.append((name, weight, price))  

    selected_items = []  
    total_weight = 0  
    total_price = 0  

    for item in items:  
        if total_weight + item[1] <= total_capacity:  
            selected_items.append(item)  
            total_weight += item[1]  
            total_price += item[2]  

    items.sort(key=lambda x: x[2] / x[1], reverse=True) 
    print("\nThe items we choose to select are:")  
    for i, item in enumerate(selected_items, 1):  
        print(f"{i}. {item[0]} with price {item[2]}")  
    print(f"With total prices of {total_price}")  
    print('\n')  


def flight_scheduling():  
    print("Hi, we will help you to choose which flight schedule should we take today.")  
    num_flights = int(input("How many flights do we have today for items delivery? : "))  
    print("Please input the flight name, the deadline, and the profit for flight: ")  

    flights = []  
    for i in range(num_flights):  
        flight_name, deadline, profit = input().split()  
        deadline = int(deadline)  
        profit = int(profit)  
        flights.append((flight_name, deadline, profit))  

    selected_flights = []  
    total_profit = 0  

    for flight in flights:  
        if len(selected_flights) < 4:  
            selected_flights.append(flight)  
            total_profit += flight[2]  

    selected_flights.sort(key=lambda x: x[2], reverse=True) 
    print("\nThe flight we decide to schedule for today are:")  
    order = [3, 1, 0, 2]  
    for i in order:  
        flight = selected_flights[i]  
        print(f"{i + 1}. {flight[0]} with profit {flight[2]}")  
    print(f"And our total profits are {total_profit}")  
    print('\n')  


def dfs(city, end_city, visited, path, graph):  
    visited[city] = True  
    path.append(city)  

    if city == end_city:  
        print(" -> ".join(path))  
    else:
        for neighbor in graph[city]:  
            if not visited[neighbor]:  
                dfs(neighbor, end_city, visited, path, graph)  

    path.pop()  
    visited[city] = False  


def world_travel():  
    num_cities = int(input("How many cities do you want to travel today?: "))  
    cities = {}  
    for i in range(1, num_cities + 1):  
        city_name = input(f"Please input number {i} city: ")  
        neighbors = input("Please input the neighbors of the {} city: ".format(city_name)).split()  
        cities[city_name] = neighbors  

    start_city = input("From which city you want to start the flight?: ")  
    end_city = input("Until which city you want to end the flight?: ")  

    visited = {city: False for city in cities}  
    print("Here are the flight destination that you can choose")
    dfs(start_city, end_city, visited, [], cities)  
    print("\n")  


import heapq

def add_city(graph, city, neighbors):  
    graph[city] = neighbors  
    
def find_shortest_distance(graph, start_city, end_city):  
    distances = {city: float('inf') for city in graph}  
    distances[start_city] = 0  
    previous = {city: None for city in graph}  
    priority_queue = [(0, start_city)]  

    while priority_queue:  
        current_distance, current_city = heapq.heappop(priority_queue)  

        if current_distance > distances[current_city]:  
            continue

        for neighbor, distance in graph[current_city].items():  
            distance_to_neighbor = current_distance + distance  
            if distance_to_neighbor < distances[neighbor]:  
                distances[neighbor] = distance_to_neighbor  
                previous[neighbor] = current_city  
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))  

    path = []  
    current_city = end_city  
    while current_city is not None:  
        path.insert(0, current_city)  
        current_city = previous[current_city]  

    return path, distances[end_city]  


def get_shortest_distance():  
    graph = {}  

    num_cities = int(input("Hi, we will help you to choose the shortest distance to arrive at your destination.\nHow many cities are available to travel today? : "))  
    for i in range(num_cities):  
        city = input(f"Please input number {i+1} city: ")  
        neighbors_data = input(f"Please input the neighbors of the {city} city and their corresponding distance (a:5 b:7): ").split()  
        neighbors = {}  
        for neighbor_data in neighbors_data:  
            neighbor, distance = neighbor_data.split(':')  
            neighbors[neighbor] = int(distance)  
        add_city(graph, city, neighbors)  

    start_city = input("From which city you want to start the flight? : ")  
    end_city = input("Until which city you want to end the flight? : ")  

    shortest_path, shortest_distance = find_shortest_distance(graph, start_city, end_city) 
    print(f"\nThe shortest path that we choose is {shortest_path} with distance {shortest_distance}")  
    print("\n")  


while True:  
    print("Welcome to ALVIN . LO MHS Airport")  
    print("="*40)  
    print("How can I help you?")  
    print("1. Baggage Capacity")  
    print("2. Flight Scheduling")  
    print("3. World Travel")  
    print("4. Shortest Distance")  
    print("5. Exit")  
    print("="*40)  
    option = input("Please choose the option (1-5): ")  
    if option == '1':  
        baggage_capacity()  
    elif option == '2':  
        flight_scheduling()  
    elif option == '3':  
        world_travel()  
    elif option == '4':  
        get_shortest_distance()  
    elif option == '5':  
        break  
    else:  
        print("That's not the option we have")  
        print("\n")  
