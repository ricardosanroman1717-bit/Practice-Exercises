from pathlib import Path


class OutOfRangeError(Exception):
    pass


def validate(temp, humidity):
    if not -40 <= temp <= 85:
        raise OutOfRangeError(f"Temp {temp} C outside -40 to 85")
    if not 0 <= humidity <= 100:
        raise OutOfRangeError(f"Humidity {humidity}% outside 0 to 100")


def parse_record(raw):
    if not isinstance(raw, str):
        raise TypeError(f"Expected text record, received {type(raw).__name__}")

    fields = raw.split(",")
    if len(fields) != 3:
        raise ValueError(f"Expected 3 fields, got {len(fields)}: {raw!r}")

    temp = float(fields[0])
    humidity = float(fields[1])
    sensor = fields[2].strip()
    if not sensor:
        raise ValueError("Missing sensor name")

    validate(temp, humidity)
    return {"sensor": sensor, "temp": temp, "humidity": humidity}


def main():
    data_dir = Path(__file__).resolve().parent
    try:
        with open(data_dir / "raw_sensor_data.csv", "r", encoding="utf-8") as source:
            raw_records = source.read().splitlines()
    except FileNotFoundError:
        print("Missing input file: raw_sensor_data.csv")
        raise SystemExit(1)

    clean_records = []
    error_count = 0
    error_log = open(data_dir / "error_log.txt", "a", encoding="utf-8")

    try:
        for index, raw in enumerate(raw_records, start=1):
            try:
                result = parse_record(raw)
            except ValueError as error:
                message = f"Record {index} [ValueError]: {error}"
                print(message)
                error_log.write(message + "\n")
                error_count += 1
                continue
            except TypeError as error:
                message = f"Record {index} [TypeError]: {error}"
                print(message)
                error_log.write(message + "\n")
                error_count += 1
                continue
            except OutOfRangeError as error:
                message = f"Record {index} [OutOfRangeError]: {error}"
                print(message)
                error_log.write(message + "\n")
                error_count += 1
                continue
            else:
                clean_records.append(result)
    except Exception as error:
        print(f"Unexpected batch error: {error}")
    else:
        print("Batch completed with no unexpected errors.")
    finally:
        error_log.close()
        print("Error log closed.")

    print(f"""\n======= Sensor Validation Report =======
Total records   : {len(raw_records)}
Clean records   : {len(clean_records)}
Errors detected : {error_count}
----------------------------------------
Clean Readings:""")
    for record in clean_records:
        print(
            f"{record['sensor']:<10} Temp: {record['temp']:>5.1f} C  "
            f"Humidity: {record['humidity']:>5.1f}%"
        )

    with open(data_dir / "clean_readings.txt", "w", encoding="utf-8") as clean_file:
        clean_file.write("Sensor     | Temp (C) | Humidity (%)\n")
        clean_file.write("-" * 39 + "\n")
        for record in clean_records:
            clean_file.write(
                f"{record['sensor']:<10} | {record['temp']:>8.1f} | "
                f"{record['humidity']:>12.1f}\n"
            )
    print("\nClean readings saved to clean_readings.txt")


if __name__ == "__main__":
    main()
