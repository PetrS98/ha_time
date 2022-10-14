# Time Date for Home Assistant

This is an integration providing time/date or timedate sensor.

### Installation

If you're using HACS - feel free to add https://github.com/PetrS98/ha_time as custom repository.

Once you've installed the custom integration, add the following to your `configuration.yaml` file:

```yaml
sensor:
  - platform: ha_time       # # Name of Addon folder
    settings: 0             # Settings for time or date format. From 0 to 4.
    scan_interval: 1        # Scan interval.
```
