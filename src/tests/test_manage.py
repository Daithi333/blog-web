import os
import sys
from unittest import mock

import pytest

from manage import main


def test_main_raises_on_missing_ENV(monkeypatch) -> None:
    if "ENV" in os.environ:
        monkeypatch.delenv("ENV")
    with pytest.raises(RuntimeError, match="ENV environment variable must be set"):
        main()


def test_main_raises_on_invalid_ENV(monkeypatch) -> None:
    monkeypatch.setenv("ENV", "nonexistent")
    with pytest.raises(ImportError, match="Unable to import settings"):
        main()


def test_django_settings_module_set(monkeypatch):
    monkeypatch.setenv("ENV", "development")
    monkeypatch.delenv("DJANGO_SETTINGS_MODULE", raising=False)

    with mock.patch("django.core.management.execute_from_command_line"):
        main()

    expected = "blogweb.settings.development"
    assert os.environ["DJANGO_SETTINGS_MODULE"] == expected


def test_execute_from_command_line_called(monkeypatch):
    monkeypatch.setenv("ENV", "development")

    with mock.patch("django.core.management.execute_from_command_line") as mock_exec:
        main()
        mock_exec.assert_called_once_with(sys.argv)
