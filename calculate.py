import math, random;

inside = int(0)
total = int(0)

if __name__ == "__main__":
    while True:
        x = random.random()
        y = random.random()

        distance = math.sqrt(x*x + y*y)
        if distance < 1:
            inside = inside + 1

        total = total + 1
        pi = 4.0 * inside / total

        print(pi)
