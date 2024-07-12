# bme680 + pizerow + prometheus_client

Gather temperature, pressure, humidity and air resistance and expose metrics in prometheus format at HTTP port `8000`.

## getting started

```shell
python -m .venv venv
. .venv/bin/activate
pip install -r requirements.txt
python script.py
```

Make it a daemon using systemd

```
# /etc/systemd/system/bme680.service
[Unit]
Description="bme680"

[Service]
ExecStart=<project_dir>/.venv/bin/python script.py
WorkingDirectory=<project_dir>
Restart=always
RestartSec=10
StandardOutput=file:/var/log/bme680.log
StandardError=file:/var/log/bme680.err.log

[Install]
WantedBy=multi-user.target
```

Activate the service and start it

```shell
sudo systemctl enable bme680.service
sudo systemctl start bme680.service
sudo systemctl status bme680.service
```

## Notes

* use a "lite" raspberry OS 
* ensure I2C is enabled using `raspi-config` command
* tested with a rapberry pi zero W v1.1 and a bme680 sensor from [pimoroni](https://shop.pimoroni.com/products/bme680-breakout)
