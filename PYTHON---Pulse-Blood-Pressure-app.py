import time
import serial  # For serial communication (if using Arduino or a similar device)

# Replace with the correct port and baud rate for your device
ser = serial.Serial('/dev/ttyUSB0', 9600)  

def read_pulse_sensor():
    """
    Reads pulse data from the sensor. 
    This is a placeholder function; replace with actual sensor reading logic.
    """
    try:
        ser.write(b'R')  # Command to request pulse reading (depends on your setup)
        pulse = ser.readline().strip()  # Reading the pulse data
        return int(pulse)
    except Exception as e:
        print("Error reading pulse sensor:", e)
        return None

def read_blood_pressure():
    """
    Reads blood pressure data from the monitor.
    This is a placeholder function; replace with actual blood pressure reading logic.
    """
    try:
        ser.write(b'B')  # Command to request blood pressure reading
        bp_data = ser.readline().strip()  # Reading the blood pressure data
        return bp_data.decode()  # Return the string representation of blood pressure
    except Exception as e:
        print("Error reading blood pressure:", e)
        return None

def main():
    while True:
        pulse = read_pulse_sensor()
        bp = read_blood_pressure()
        
        if pulse is not None:
            print(f"Pulse: {pulse} bpm")
        if bp is not None:
            print(f"Blood Pressure: {bp}")
        
        time.sleep(1)  # Delay between readings

if __name__ == "__main__":
    main()
