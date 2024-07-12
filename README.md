# bme680 + pizerow + prometheus_client

Gather temperature, pressure, humidity and air resistance and expose metrics in prometheus format at HTTP port `8000`.

## getting started

```shell
python -m .venv venv
. .venv/bin/activate
pip install -r requirements.txt
python script.py
```

## Notes

* use a "lite" raspberry OS 
* ensure I2C is enabled using `raspi-config` command
* tested with a rapberry pi zero W v1.1 and a bme680 sensor from [pimoroni](https://shop.pimoroni.com/products/bme680-breakout)
