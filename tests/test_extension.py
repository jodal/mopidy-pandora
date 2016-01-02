from __future__ import unicode_literals

import unittest

import mock

from mopidy_pandora import Extension

from mopidy_pandora import backend as backend_lib
from mopidy_pandora import frontend as frontend_lib


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = Extension()

        config = ext.get_default_config()

        self.assertIn('[pandora]', config)
        self.assertIn('enabled = true', config)
        self.assertIn('api_host = tuner.pandora.com/services/json/', config)
        self.assertIn('partner_encryption_key =', config)
        self.assertIn('partner_decryption_key =', config)
        self.assertIn('partner_username =', config)
        self.assertIn('partner_password =', config)
        self.assertIn('partner_device =', config)
        self.assertIn('username =', config)
        self.assertIn('password =', config)
        self.assertIn('preferred_audio_quality = highQuality', config)
        self.assertIn('sort_order = date', config)
        self.assertIn('auto_setup = true', config)
        self.assertIn('cache_time_to_live = 1800', config)
        self.assertIn('event_support_enabled = true', config)
        self.assertIn('double_click_interval = 2.00', config)
        self.assertIn('on_pause_resume_click = thumbs_up', config)
        self.assertIn('on_pause_next_click = thumbs_down', config)
        self.assertIn('on_pause_previous_click = sleep', config)
        self.assertIn('on_pause_stop_click = delete_station', config)

    def test_get_config_schema(self):
        ext = Extension()

        schema = ext.get_config_schema()

        self.assertIn('enabled', schema)
        self.assertIn('api_host', schema)
        self.assertIn('partner_encryption_key', schema)
        self.assertIn('partner_decryption_key', schema)
        self.assertIn('partner_username', schema)
        self.assertIn('partner_password', schema)
        self.assertIn('partner_device', schema)
        self.assertIn('username', schema)
        self.assertIn('password', schema)
        self.assertIn('preferred_audio_quality', schema)
        self.assertIn('sort_order', schema)
        self.assertIn('auto_setup', schema)
        self.assertIn('cache_time_to_live', schema)
        self.assertIn('event_support_enabled', schema)
        self.assertIn('double_click_interval', schema)
        self.assertIn('on_pause_resume_click', schema)
        self.assertIn('on_pause_next_click', schema)
        self.assertIn('on_pause_previous_click', schema)
        self.assertIn('on_pause_stop_click', schema)

    def test_setup(self):
        registry = mock.Mock()

        ext = Extension()
        ext.setup(registry)
        calls = [mock.call('frontend', frontend_lib.PandoraFrontendFactory),
                 mock.call('backend',  backend_lib.PandoraBackend)]
        registry.add.assert_has_calls(calls, any_order=True)
