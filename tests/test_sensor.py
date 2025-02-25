"""Test the ViCare config flow."""

from unittest.mock import MagicMock

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import ATTR_DEVICE_CLASS, ATTR_FRIENDLY_NAME
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry


async def test_outside_temperature(
    hass: HomeAssistant,
    mock_vicare_gas_boiler: MagicMock,
    init_integration: MockConfigEntry,
) -> None:
    """Test Outside temperature sensor."""
    state = hass.states.get("sensor.vicare_outside_temperature")
    assert state
    assert state.attributes.get(ATTR_DEVICE_CLASS) == SensorDeviceClass.TEMPERATURE
    assert state.attributes.get(ATTR_FRIENDLY_NAME) == "ViCare Outside Temperature"
