# test_linkquick.py
"""
Tests for LinkQuick module.
"""

import unittest
from linkquick import LinkQuick

class TestLinkQuick(unittest.TestCase):
    """Test cases for LinkQuick class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinkQuick()
        self.assertIsInstance(instance, LinkQuick)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinkQuick()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
