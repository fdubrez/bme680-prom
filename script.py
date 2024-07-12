from prometheus_client import start_http_server, Gauge
import time
import bme680

DATA = {}
t = Gauge('temperature', 'Température (°C)')
p = Gauge('pressure', 'Pression atmosphérique (hPa)')
h = Gauge('humidity', 'Humidité (%RH)')
g = Gauge('gaz_resistance', "Résistance de l'air (Ohms)")

def get_sensor_data() -> dict:
    try:
        sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
    except (RuntimeError, IOError):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)

    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)
    sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
    sensor.set_gas_heater_temperature(320)
    sensor.set_gas_heater_duration(150)
    sensor.select_gas_heater_profile(0)

    data = {
        "temperature": 21.0,
        "pressure": 21.0,
        "humidity": 21.0,
        "gas_resistance": 21.0
    }

    # we wait for data to be available
    while sensor.get_sensor_data() is False or sensor.data.heat_stable is False:
        time.sleep(1)

    data["temperature"] = float(format(sensor.data.temperature, "0.2f"))
    data["pressure"] = float(format(sensor.data.pressure, "0.2f"))
    data["humidity"] = float(format(sensor.data.humidity, "0.2f"))
    data["gas_resistance"] = float(int(sensor.data.gas_resistance))
    print(f"{data['temperature']} C, {data['pressure']} hPa, {data['humidity']} %RH, {data['gas_resistance']} Ohms")

    return data

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # refresh gauges every 60 seconds
    while True:
        data = get_sensor_data()
        t.set(data['temperature'])
        p.set(data['pressure'])
        h.set(data['humidity'])
        g.set(data['gas_resistance'])
        time.sleep(60)
