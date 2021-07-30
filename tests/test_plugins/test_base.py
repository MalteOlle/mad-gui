from pathlib import Path

import pytest

from mad_gui.plugins.base import BaseImporter
from mad_gui.plugins.example import ExampleImporter

EXAMPLE_DATA_PATH = Path(__file__).parent.parent.parent / "example_data"


class TestBaseImporter:

    def test_instantiation(self):
        ExampleImporter()

    def test_not_implemented(self):
        with pytest.raises(NotImplementedError):
            importer = BaseImporter()
            importer.load_annotations("bad_path")

    def test_bad_path(self):
        with pytest.raises(FileNotFoundError):
            importer = ExampleImporter()
            importer.load_sensor_data("bad_path")

    def test_load_data(self):
        importer = ExampleImporter()
        sensor_data, sampling_rate_hz = importer.load_sensor_data(EXAMPLE_DATA_PATH / "smartphone" / "acceleration.csv")
        assert len(sensor_data["Acceleration"] == 1691)
