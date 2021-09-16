from sys import stdin, maxsize

def main():
    stdin = open('Problem\grm_2F\input.txt', 'r')
    num_of_planets = int(stdin.readline())

    planet_positions = []
    for _ in range(num_of_planets):
        x, y = map(int, stdin.readline().split())
        planet_positions.append((x, y))
    
    min_dist = maxsize
    pair = 0

    for i in range(num_of_planets):
        for j in range(i + 1, num_of_planets):
            distance = round((((planet_positions[i][0] - planet_positions[j][0]) ** 2) + ((planet_positions[i][1] - planet_positions[j][1]) ** 2)) ** 0.5, 1)

            if min_dist > distance:
                min_dist = distance
                pair = 1
            elif min_dist == distance:
                pair += 1

    print(min_dist)
    print(pair)

if __name__ == "__main__":
    main()