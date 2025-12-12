from __future__ import annotations

from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import DefaultDict, Iterable


def _normalize_segment(
    a: tuple[int, int], b: tuple[int, int]
) -> tuple[int, int, int, int]:
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:
        if y2 < y1:
            y1, y2 = y2, y1
        return x1, y1, x2, y2
    if y1 == y2:
        if x2 < x1:
            x1, x2 = x2, x1
        return x1, y1, x2, y2
    raise ValueError(f"Non-axis-aligned segment: {a} -> {b}")


def _point_on_intervals(intervals: list[tuple[int, int]], v: int) -> bool:
    """Intervals are inclusive on both ends and sorted by start."""
    # Find rightmost interval with start <= v
    i = bisect_right(intervals, (v, 10**30)) - 1
    if i < 0:
        return False
    start, end = intervals[i]
    return start <= v <= end


def _build_interval_index(segments: list[tuple[int, int, int, int]]):
    horiz: DefaultDict[int, list[tuple[int, int]]] = defaultdict(list)
    vert: DefaultDict[int, list[tuple[int, int]]] = defaultdict(list)
    vertical_edges: list[tuple[int, int, int]] = []  # (x, y_low, y_high)

    for x1, y1, x2, y2 in segments:
        if y1 == y2:
            horiz[y1].append((x1, x2))
        else:
            vert[x1].append((y1, y2))
            vertical_edges.append((x1, y1, y2))

    for y, intervals in horiz.items():
        intervals.sort()
    for x, intervals in vert.items():
        intervals.sort()

    return horiz, vert, vertical_edges


def _build_crossings_by_y(
    vertical_edges: list[tuple[int, int, int]], ys: Iterable[int]
):
    """For a horizontal ray-cast at integer y, use the half-open rule [y_low, y_high)."""
    crossings: dict[int, list[int]] = {}
    for y in ys:
        xs: list[int] = []
        for x, y_low, y_high in vertical_edges:
            if y_low <= y < y_high:
                xs.append(x)
        xs.sort()
        crossings[y] = xs
    return crossings


def solve(path: str = "./input.txt") -> int:
    with open(path) as f:
        coords_s = f.read().split()

    # Red tiles (vertices) in given cyclic order.
    verts: list[tuple[int, int]] = []
    for c in coords_s:
        x_str, y_str = c.split(",")
        x, y = int(x_str), int(y_str)
        verts.append((x, y))

    if len(verts) < 2:
        return 0

    # Build polygon boundary segments.
    segments: list[tuple[int, int, int, int]] = []
    for i in range(len(verts)):
        a = verts[i]
        b = verts[(i + 1) % len(verts)]
        segments.append(_normalize_segment(a, b))

    horiz_by_y, vert_by_x, vertical_edges = _build_interval_index(segments)
    unique_ys = sorted({y for _, y in verts})
    crossings_by_y = _build_crossings_by_y(vertical_edges, unique_ys)

    def on_boundary(x: int, y: int) -> bool:
        intervals = horiz_by_y.get(y)
        if intervals and _point_on_intervals(intervals, x):
            return True
        intervals = vert_by_x.get(x)
        if intervals and _point_on_intervals(intervals, y):
            return True
        return False

    def inside_or_on(x: int, y: int) -> bool:
        if on_boundary(x, y):
            return True
        xs = crossings_by_y.get(y)
        if xs is None:
            # y not present in vertex set: compute crossings on-demand.
            xs = []
            for x_edge, y_low, y_high in vertical_edges:
                if y_low <= y < y_high:
                    xs.append(x_edge)
            xs.sort()
            crossings_by_y[y] = xs
        # Count crossings strictly to the left of x.
        return (bisect_left(xs, x) % 2) == 1

    def boundary_crosses_rect_interior(
        xmin: int, xmax: int, ymin: int, ymax: int
    ) -> bool:
        # Any boundary segment with a point strictly inside the open rectangle implies
        # the rectangle contains both inside & outside regions.
        for x1, y1, x2, y2 in segments:
            if y1 == y2:
                y = y1
                if ymin < y < ymax:
                    seg_xmin = x1
                    seg_xmax = x2
                    if max(seg_xmin, xmin) < min(seg_xmax, xmax):
                        return True
            else:
                x = x1
                if xmin < x < xmax:
                    seg_ymin = y1
                    seg_ymax = y2
                    if max(seg_ymin, ymin) < min(seg_ymax, ymax):
                        return True
        return False

    max_area = 0
    n = len(verts)
    for i in range(n):
        x1, y1 = verts[i]
        for j in range(i + 1, n):
            x2, y2 = verts[j]

            xmin, xmax = (x1, x2) if x1 <= x2 else (x2, x1)
            ymin, ymax = (y1, y2) if y1 <= y2 else (y2, y1)
            area = (xmax - xmin + 1) * (ymax - ymin + 1)
            if area <= max_area:
                continue

            # Other corners must be red/green (inside or on boundary).
            if not inside_or_on(xmin, ymax):
                continue
            if not inside_or_on(xmax, ymin):
                continue

            # And the polygon boundary must not pass through the interior.
            if boundary_crosses_rect_interior(xmin, xmax, ymin, ymax):
                continue

            max_area = area

    return max_area


if __name__ == "__main__":
    print(solve())
