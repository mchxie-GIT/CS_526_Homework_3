import sys


def all_ghosts_eliminated(streams):
    for i in range(len(streams)):
        x1, y1, dx1, dy1 = streams[i]
        for j in range(i + 1, len(streams)):
            x2, y2, dx2, dy2 = streams[j]

            # Nonparallel infinite lines always cross.
            if dx1 * dy2 != dy1 * dx2:
                return False

            # Parallel lines also cross if they are the same line.
            if (x2 - x1) * dy1 == (y2 - y1) * dx1:
                return False

    return True


def main():
    n = int(sys.stdin.readline())
    streams = []
    for i in range(n):
        parts = sys.stdin.readline().split()
        bx, by = int(parts[1]), int(parts[2])
        gx, gy = int(parts[4]), int(parts[5])
        streams.append((bx, by, gx - bx, gy - by))

    if all_ghosts_eliminated(streams):
        print("All Ghosts: were eliminated")
    else:
        print("All Ghosts: were not eliminated")


if __name__ == "__main__":
    main()
