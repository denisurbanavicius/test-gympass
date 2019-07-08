from datetime import datetime
from decimal import Decimal

from gympass.model import Driver, LapRecord, DriverResults


# Constants
FINAL_LAP = 4


def load_data(filename):
    """
    Read a race log and return every record as list of objects
    :param filename: file relative path or full file path
    :return: list of LapRecord
    """
    file = open(filename, 'r')
    contents = file.readlines()

    laps = []
    for idx, line in enumerate(contents):
        if idx == 0:
            continue

        # Set fields boundaries
        total_time = line[0:18]
        driver_number = line[18:21]
        driver_name = line[24:58]
        lap = line[58:72]
        lap_time = line[72:104]
        speed = line[104:-1]

        # Data correction
        driver_number = driver_number.rstrip()
        driver_name = driver_name.rstrip()
        total_time = datetime.strptime(total_time.rstrip(), '%H:%M:%S.%f')
        lap = int(lap)
        lap_time = datetime.strptime(lap_time.rstrip(), '%M:%S.%f')
        speed = Decimal(speed.rstrip().replace(',', '.'))  # Decimal avoids precision errors

        # Puts values into objects
        driver = Driver(driver_number, driver_name)
        lap_record = LapRecord(total_time, driver, lap, lap_time, speed)
        laps.append(lap_record)
    return laps


def sort_laps(laps):
    """
    Sorts laps using the total time
    :param laps: list of LapRecord
    :return: list of LapRecord
    """
    return sorted(laps, key=lambda lap: lap.total_time)


def build_results(laps):
    """
    Build a list of driver results from a list of laps
    :param laps: list of LapRecord (sorted)
    :return: list of DriverResults
    """
    # Set race start time, so que can calculate total race time
    first_lap = laps[0]
    race_start = first_lap.total_time - first_lap.lap_time

    # Control variables
    skip = True
    position = 1
    results = []
    drivers_finished = []

    for lap_record in laps:
        # Skips all laps until we reach the final lap
        if lap_record.lap == FINAL_LAP:
            skip = False
        if skip:
            continue

        # If the driver already finished, we should stop counting his laps
        if lap_record.driver.name in drivers_finished:
            continue

        # Calculates total time, puts results into an object
        total_time = lap_record.total_time - race_start
        driver_result = DriverResults(driver=lap_record.driver,
                                      position=position,
                                      total_laps=lap_record.lap,
                                      total_time=total_time)
        results.append(driver_result)
        drivers_finished.append(lap_record.driver.name)

        # Adjusts position of the next finishing driver
        position += 1
    return results


def print_results(results):
    """
    Prints all results on screen
    :param results: list of DriverResults
    :return: None
    """
    # Uses the object's own printing method (__repr__)
    for driver_result in results:
        print(driver_result)


def run(filename):
    """
    Read a race log file, build the race results and print them on screen
    :param filename: file relative path or full file path
    :return: list of DriverResults
    """
    lap_records = load_data(filename)
    sorted_laps = sort_laps(lap_records)
    race_results = build_results(sorted_laps)
    print_results(race_results)
    return race_results


if __name__ == '__main__':
    run('input.txt')
