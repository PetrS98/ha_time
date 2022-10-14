# Time Date for Home Assistant

This is an integration providing time/date or timedate sensor.

### Installation

If you're using HACS - feel free to add https://github.com/PetrS98/ha_time as custom repository.

### Settings fromat

```yaml
0 = 14.10.2022 16:07:23 
1 = 14.října 2022 16:07:23 
2 = 14.10.2022 
3 = 14.října 2022 
4 = 16:07:23 

```

Once you've installed the custom integration, add the following to your `configuration.yaml` file:

```yaml
sensor:
  - platform: ha_time       # Name of Addon folder
    settings: 0             # Settings for time or date format. From 0 to 4.
    scan_interval: 1        # Scan interval.
```
