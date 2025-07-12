# Airport-Management-System
# 🛫 ALVIN . LO MHS Airport – Simulasi Interaktif Bandara

Aplikasi ini merupakan simulasi sistem bandara berbasis Python yang memiliki empat fitur utama: **pengelolaan bagasi**, **penjadwalan penerbangan**, **rute world travel (DFS)**, dan **pencarian jarak terpendek antar kota (Dijkstra's algorithm)**.

---

## ✨ Fitur Utama

1. **Baggage Capacity**
   - Menentukan barang-barang mana yang dapat dimuat berdasarkan kapasitas maksimal pesawat (1000 kg).
   - Pemilihan item berdasarkan total berat dan nilai ekonomis (price-to-weight ratio).

2. **Flight Scheduling**
   - Menentukan penjadwalan penerbangan berdasarkan deadline dan profit.
   - Menyortir flight berdasarkan profit tertinggi.

3. **World Travel**
   - Menggunakan algoritma **DFS (Depth-First Search)** untuk menampilkan semua rute dari kota asal ke kota tujuan.

4. **Shortest Distance**
   - Menggunakan **Dijkstra’s algorithm** untuk menemukan jarak terpendek antar dua kota.
   - Mendukung input tetangga dan jarak masing-masing.

---

## 🧠 Algoritma & Struktur

| Fitur               | Algoritma            |
|---------------------|----------------------|
| Baggage Capacity    | Greedy (by weight) + Price-to-weight ratio |
| Flight Scheduling   | Greedy based on profit |
| World Travel        | Depth-First Search (DFS) |
| Shortest Distance   | Dijkstra's Algorithm (priority queue with heapq) |

---

## 🚀 Cara Menjalankan Aplikasi

1. **Pastikan Python 3 sudah terinstal**
2. Jalankan file Python:

```bash
python airport_simulator.py
3.Pilih opsi yang tersedia melalui terminal:

plaintext
Copy
Edit
Welcome to ALVIN . LO MHS Airport
========================================
How can I help you?
1. Baggage Capacity
2. Flight Scheduling
3. World Travel
4. Shortest Distance
5. Exit
========================================
🛅 Contoh Input & Output: Baggage
Input:

graphql
Copy
Edit
How many items you have on the candidate? : 3
Please input the name, the weight, and the price for item:
Laptop 4 500
Book 10 100
Gold 20 1500
Output:

sql
Copy
Edit
The items we choose to select are:
1. Laptop with price 500
2. Book with price 100
3. Gold with price 1500
With total prices of 2100
🌍 Contoh Input & Output: Shortest Distance
Input:

less
Copy
Edit
Please input the neighbors of the Jakarta city and their corresponding distance (a:5 b:7): Surabaya:5 Bandung:4
Output:

pgsql
Copy
Edit
The shortest path that we choose is ['Jakarta', 'Bandung', 'Bali'] with distance 12
📁 Struktur Fungsi Utama
Fungsi	Deskripsi Singkat
baggage_capacity()	Pemilihan item bagasi berdasarkan batas berat
flight_scheduling()	Penjadwalan penerbangan berdasarkan profit
world_travel()	Menampilkan semua jalur dengan DFS
get_shortest_distance()	Menampilkan jarak terpendek antar kota dengan Dijkstra
dfs()	DFS rekursif untuk rute world travel
find_shortest_distance()	Implementasi Dijkstra menggunakan heapq
