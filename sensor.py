"""Platform for sensor integration."""
from sqlite3 import Date
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import SensorEntity

""" External Imports """
import logging
import datetime

""" Constants """
CONF_SETTINGS = "settings"

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_SETTINGS): cv.positive_int
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    MainValNumber = config.get(CONF_SETTINGS)

    add_entities([CustomTime(MainValNumber)], update_before_add=True)

class CustomTime(SensorEntity):

    """Representation of a Sensor."""

    CZMonthName = {
                1: "ledna",
                2: "února",
                3: "března",
                4: "dubna",
                5: "května",
                6: "června",
                7: "července",
                8: "srpna",
                9: "září",
                10: "října",
                11: "listopadu",
                12: "prosince"
            }
    DateTimes = []

    def __init__(self, MainValNumber):
        """Initialize the sensor."""

        self._available = None

        if MainValNumber < 0 or MainValNumber > 4:
            self._mainValNumber = 0
        else:
            self._mainValNumber = MainValNumber

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
        return self.DateTimes[self._mainValNumber]

    @property
    def available(self):
        """Return True if entity is available."""
        return self._available

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        try:
            ActualDateTime = datetime.datetime.now()
            self.DateTimes.clear()

            self.DateTimes.append(ActualDateTime.strftime("%d.%m.%Y %H:%M:%S"))
            self.DateTimes.append(ActualDateTime.strftime("%d." + self.CZMonthName[ActualDateTime.month] + " %Y %H:%M:%S"))
            self.DateTimes.append(ActualDateTime.strftime("%d.%m.%Y"))
            self.DateTimes.append(ActualDateTime.strftime("%d." + self.CZMonthName[ActualDateTime.month] + " %Y"))
            self.DateTimes.append(ActualDateTime.strftime("%H:%M:%S"))
            self._available = True
        except:
            _LOGGER.exception("Error occured.")
            self._available = False 