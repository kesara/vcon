import unittest
from datetime import datetime

from vcon import vCon


class TestVcon(unittest.TestCase):
    def test_valid_vcon(self):
        valid_data = {
            "vcon": "foobar",
            "uuid": "49a1fea3-4269-4ade-ba66-a769071ce0c0",
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "subject": "foobar",
            "group": [{"uuid": "eca536c8-a259-42f7-b6a5-3ff6ef529348"}],
        }

        vcon = vCon(**valid_data)
        self.assertEqual(vcon.vcon, valid_data["vcon"])
        self.assertEqual(vcon.uuid, valid_data["uuid"])
        self.assertEqual(vcon.created_at, valid_data["created_at"])
        self.assertEqual(vcon.updated_at, valid_data["updated_at"])
        self.assertEqual(vcon.subject, valid_data["subject"])
        self.assertEqual(vcon.uuid, valid_data["uuid"])
