#!/usr/bin/python3
"""This script contains the canUnlockAll function"""


def canUnlockAll(boxes):
    """
      Determined if all boxes in a set can be oprned
    """
    opened_boxes = set([0])
    key = [0]
    count = 0
    while True:
        current = key.pop()
        newKeys = boxes[current]
        if not newKeys:
            break
        for k in newKeys:
            if k >= 0 and k < len(boxes) and k not in opened_boxes:
                key.append(k)
                opened_boxes.add(k)

        if count >= len(boxes) or not key:
            break
        count = count + 1
    return len(boxes) == len(opened_boxes)
