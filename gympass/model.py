

class LapRecord:
    def __init__(self, total_time, driver, lap, lap_time, speed):
        self.total_time = total_time
        self.driver = driver
        self.lap = lap
        self.lap_time = lap_time
        self.speed = speed


class Driver:
    def __init__(self, number, name):
        self.number = number
        self.name = name


class DriverResults:
    def __init__(self, driver, position, total_laps, total_time):
        self.driver = driver
        self.position = position
        self.total_laps = total_laps
        self.total_time = total_time

    def __repr__(self):
        total_time = self.total_time.strftime('%H:%M:%S.%f')
        return f'{self.position} - {self.driver.number} {self.driver.name.ljust(20)} ' \
            f' {self.total_laps} laps - {total_time}'
