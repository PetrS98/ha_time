"""Platform for sensor integration."""
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import SensorEntity

""" External Imports """
import logging
import requests
import datetime

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""

    add_entities([CustomTime()], update_before_add=True)

class CustomTime(SensorEntity):

    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        self._value = None
        self._available = None

    @property
    def unique_id(self):
        """Return the unique id of the sensor."""
        return "Custom time by PS"

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Time Sensor"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self._value

    @property
    def available(self):
        """Return True if entity is available."""
        return self._available

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        try:
            self._value = datetime.datetime.now()
            self._available = True
        except:
            _LOGGER.exception("Error occured.")
            self._available = False 