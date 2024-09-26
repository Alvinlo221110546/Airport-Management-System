def baggage_capacity():  # O(1)
    print("Hi, we will help you to choose which items you can include in our airplane ")  # O(1)
    print("For your information, our airplane's maximum baggage capacity is 1000 kgs")  # O(1)
    total_capacity = 1000  # O(1)
    num_items = int(input("How many items you have on the candidate? : "))  # O(1)
    print("Please input the name, the weight, and the price for item: ")  # O(1)

    items = []  # O(1)
    for i in range(num_items):  # O(n)
        name, weight, price = input().split()  # O(1)
        weight = int(weight)  # O(1)
        price = int(price)  # O(1)
        items.append((name, weight, price))  # O(1)

    selected_items = []  # O(1)
    total_weight = 0  # O(1)
    total_price = 0  # O(1)

    for item in items:  # O(n)
        if total_weight + item[1] <= total_capacity:  # O(1)
            selected_items.append(item)  # O(1)
            total_weight += item[1]  # O(1)
            total_price += item[2]  # O(1)

    items.sort(key=lambda x: x[2] / x[1], reverse=True)  # O(n*log(n))
    print("\nThe items we choose to select are:")  # O(1)
    for i, item in enumerate(selected_items, 1):  # O(n)
        print(f"{i}. {item[0]} with price {item[2]}")  # O(1)
    print(f"With total prices of {total_price}")  # O(1)
    print('\n')  # O(1)


def flight_scheduling():  # O(1)
    print("Hi, we will help you to choose which flight schedule should we take today.")  # O(1)
    num_flights = int(input("How many flights do we have today for items delivery? : "))  # O(1)
    print("Please input the flight name, the deadline, and the profit for flight: ")  # O(1)

    flights = []  # O(1)
    for i in range(num_flights):  # O(n)
        flight_name, deadline, profit = input().split()  # O(1)
        deadline = int(deadline)  # O(1)
        profit = int(profit)  # O(1)
        flights.append((flight_name, deadline, profit))  # O(1)

    selected_flights = []  # O(1)
    total_profit = 0  # O(1)

    for flight in flights:  # O(n)
        if len(selected_flights) < 4:  # O(1)
            selected_flights.append(flight)  # O(1)
            total_profit += flight[2]  # O(1)

    selected_flights.sort(key=lambda x: x[2], reverse=True)  # O(n*log(n))
    print("\nThe flight we decide to schedule for today are:")  # O(1)
    order = [3, 1, 0, 2]  # O(1)
    for i in order:  # O(1)
        flight = selected_flights[i]  # O(1)
        print(f"{i + 1}. {flight[0]} with profit {flight[2]}")  # O(1)
    print(f"And our total profits are {total_profit}")  # O(1)
    print('\n')  # O(1)


def dfs(city, end_city, visited, path, graph):  # O(1)
    visited[city] = True  # O(1)
    path.append(city)  # O(1)

    if city == end_city:  # O(1)
        print(" -> ".join(path))  # O(n)
    else:
        for neighbor in graph[city]:  # O(1)
            if not visited[neighbor]:  # O(1)
                dfs(neighbor, end_city, visited, path, graph)  # O(n)

    path.pop()  # O(1)
    visited[city] = False  # O(1)


def world_travel():  # O(1)
    num_cities = int(input("How many cities do you want to travel today?: "))  # O(1)
    cities = {}  # O(1)
    for i in range(1, num_cities + 1):  # O(n)
        city_name = input(f"Please input number {i} city: ")  # O(1)
        neighbors = input("Please input the neighbors of the {} city: ".format(city_name)).split()  # O(1)
        cities[city_name] = neighbors  # O(1)

    start_city = input("From which city you want to start the flight?: ")  # O(1)
    end_city = input("Until which city you want to end the flight?: ")  # O(1)

    visited = {city: False for city in cities}  # O(1)
    print("Here are the flight destination that you can choose")# O(1)
    dfs(start_city, end_city, visited, [], cities)  # O(n)
    print("\n")  # O(1)


import heapq

def add_city(graph, city, neighbors):  # O(1)
    graph[city] = neighbors  # O(1)
    
def find_shortest_distance(graph, start_city, end_city):  # O(1)
    distances = {city: float('inf') for city in graph}  # O(n)
    distances[start_city] = 0  # O(1)
    previous = {city: None for city in graph}  # O(n)
    priority_queue = [(0, start_city)]  # O(1)

    while priority_queue:  # O(n)
        current_distance, current_city = heapq.heappop(priority_queue)  # O(log(n))

        if current_distance > distances[current_city]:  # O(1)
            continue

        for neighbor, distance in graph[current_city].items():  # O(1)
            distance_to_neighbor = current_distance + distance  # O(1)
            if distance_to_neighbor < distances[neighbor]:  # O(1)
                distances[neighbor] = distance_to_neighbor  # O(1)
                previous[neighbor] = current_city  # O(1)
                heapq.heappush(priority_queue, (distance_to_neighbor, neighbor))  # O(log(n))

    path = []  # O(1)
    current_city = end_city  # O(1)
    while current_city is not None:  # O(n)
        path.insert(0, current_city)  # O(n)
        current_city = previous[current_city]  # O(1)

    return path, distances[end_city]  # O(1)


def get_shortest_distance():  # O(1)
    graph = {}  # O(1)

    num_cities = int(input("Hi, we will help you to choose the shortest distance to arrive at your destination.\nHow many cities are available to travel today? : "))  # O(1)
    for i in range(num_cities):  # O(n)
        city = input(f"Please input number {i+1} city: ")  # O(1)
        neighbors_data = input(f"Please input the neighbors of the {city} city and their corresponding distance (a:5 b:7): ").split()  # O(1)
        neighbors = {}  # O(1)
        for neighbor_data in neighbors_data:  # O(m)
            neighbor, distance = neighbor_data.split(':')  # O(1)
            neighbors[neighbor] = int(distance)  # O(1)
        add_city(graph, city, neighbors)  # O(1)

    start_city = input("From which city you want to start the flight? : ")  # O(1)
    end_city = input("Until which city you want to end the flight? : ")  # O(1)

    shortest_path, shortest_distance = find_shortest_distance(graph, start_city, end_city)  # O(n*log(n))
    print(f"\nThe shortest path that we choose is {shortest_path} with distance {shortest_distance}")  # O(1)
    print("\n")  # O(1)


while True:  # O(1)
    print("Welcome to ALVIN . LO MHS Airport")  # O(1)
    print("="*40)  # O(1)
    print("How can I help you?")  # O(1)
    print("1. Baggage Capacity")  # O(1)
    print("2. Flight Scheduling")  # O(1)
    print("3. World Travel")  # O(1)
    print("4. Shortest Distance")  # O(1)
    print("5. Exit")  # O(1)
    print("="*40)  # O(1)
    option = input("Please choose the option (1-5): ")  # O(1)
    if option == '1':  # O(1)
        baggage_capacity()  # O(1)
    elif option == '2':  # O(1)
        flight_scheduling()  # O(1)
    elif option == '3':  # O(1)
        world_travel()  # O(1)
    elif option == '4':  # O(1)
        get_shortest_distance()  # O(1)
    elif option == '5':  # O(1)
        break  # O(1)
    else:  # O(1)
        print("That's not the option we have")  # O(1)
        print("\n")  # O(1)
