import cv2
import numpy as np

def detect_edges(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges

def region_of_interest(edges):
    height, width = edges.shape
    mask = np.zeros_like(edges)

    # Define a polygon (triangle) by vertices for region of interest
    polygon = np.array([[
        (0, height),
        (width, height),
        (width, height - 200),
        (0, height - 200)
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    cropped_edges = cv2.bitwise_and(edges, mask)
    return cropped_edges

def detect_lines(cropped_edges):
    lines = cv2.HoughLinesP(cropped_edges, rho=2, theta=np.pi/180, threshold=50,
                            lines=np.array([]), minLineLength=40, maxLineGap=100)

    return lines

def average_slope_intercept(frame, lines):
    left_lines = []
    right_lines = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            if slope < 0:
                left_lines.append((slope, intercept))
            else:
                right_lines.append((slope, intercept))

    if len(left_lines) == 0 or len(right_lines) == 0:
        return None

    left_avg = np.average(left_lines, axis=0)
    right_avg = np.average(right_lines, axis=0)
    left_line = make_coordinates(frame, left_avg)
    right_line = make_coordinates(frame, right_avg)
    return np.array([left_line, right_line])

def make_coordinates(frame, line_parameters):
    slope, intercept = line_parameters
    y1 = frame.shape[0]
    y2 = int(y1 - 200)
    x1 = int((y1 - intercept) / slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])

def display_lines(frame, lines):
    line_image = np.zeros_like(frame)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
    return line_image

def find_center_point(frame, lines):
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                if x1 < frame.shape[1] / 2 and x2 < frame.shape[1] / 2:
                    # Left lane line detected
                    continue
                elif x1 > frame.shape[1] / 2 and x2 > frame.shape[1] / 2:
                    # Right lane line detected
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    return center_x, center_y
    return None

def main():
    cap = cv2.VideoCapture('road_video.mp4')  # Change this with your road video file
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        edges = detect_edges(frame)
        cropped_edges = region_of_interest(edges)
        lines = detect_lines(cropped_edges)
        averaged_lines = average_slope_intercept(frame, lines)
        line_image = display_lines(frame, averaged_lines)

        center_point = find_center_point(frame, averaged_lines)
        if center_point is not None:
            cv2.circle(frame, center_point, 5, (0, 0, 255), -1)

        combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

        cv2.imshow('Result', combo_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

