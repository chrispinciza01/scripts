import pyautogui
import random
import time
import keyboard
import win32gui
import win32con

def is_user_active():
    """Detects if the user is typing or manually moving the mouse."""
    if keyboard._pressed_events:  # Detects any pressed key (including space & special characters)
        return True  

    current_mouse_pos = pyautogui.position()
    if current_mouse_pos != is_user_active.last_mouse_pos:
        is_user_active.last_mouse_pos = current_mouse_pos
        return True  # Detects manual mouse movement

    return False

# Initialize last known mouse position
is_user_active.last_mouse_pos = pyautogui.position()

def get_window_under_cursor():
    """Returns the window handle and title of the window under the mouse."""
    x, y = pyautogui.position()
    hwnd = win32gui.WindowFromPoint((x, y))
    return hwnd, win32gui.GetWindowText(hwnd)

def activate_window(hwnd):
    """Activates a window without minimizing or closing it."""
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized
        win32gui.SetForegroundWindow(hwnd)  # Bring it to focus

def move_mouse_naturally():
    screen_width, screen_height = pyautogui.size()
    
    while True:
        if is_user_active():
            print("User is typing or using the mouse, pausing...")
            time.sleep(random.uniform(3, 6))  # Shorter pause, more human-like
            continue  # Skip movement while user is active

        # Check the window under the cursor
        hwnd, window_title = get_window_under_cursor()
        if hwnd and window_title.strip():
            print(f"Window under cursor: {window_title}")
            activate_window(hwnd)  # Ensure the window is active before moving

        # Pick a random target within the screen (avoiding edges)
        target_x = random.randint(100, screen_width - 100)
        target_y = random.randint(100, screen_height - 100)

        # Smooth movement using small, non-uniform step increments
        steps = random.randint(15, 40)  # More steps for smoother curves
        current_x, current_y = pyautogui.position()
        offset_x = [(target_x - current_x) / steps + random.uniform(-8, 8) for _ in range(steps)]
        offset_y = [(target_y - current_y) / steps + random.uniform(-8, 8) for _ in range(steps)]

        print(f"Moving from ({current_x}, {current_y}) to ({target_x}, {target_y}) in {steps} steps.")

        for i in range(steps):
            if is_user_active():
                print("User became active, stopping movement.")
                break  # Stop movement if the user is active
            
            move_duration = random.uniform(0.01, 0.12)  # More varied speed
            pyautogui.moveRel(offset_x[i], offset_y[i], duration=move_duration)

            if random.random() < 0.3:  # 30% chance of a tiny pause
                time.sleep(random.uniform(0.1, 0.3))

        pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.1, 0.3))

        # Occasionally scroll if the window is active
        if random.random() < 0.4:
            scroll_amount = random.randint(-5, 5) * 10  # Smaller, more natural scrolls
            print(f"Scrolling {'up' if scroll_amount > 0 else 'down'} by {abs(scroll_amount)} lines.")
            pyautogui.scroll(scroll_amount)

        # Wait a random time before the next action
        sleep_time = random.randint(20, 60)  # Increased randomness
        print(f"Waiting for {sleep_time} seconds before next move...\n")
        time.sleep(sleep_time)

if __name__ == "__main__":
    move_mouse_naturally()
