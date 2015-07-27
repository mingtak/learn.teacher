# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from learn.teacher.testing import LEARN_TEACHER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that learn.teacher is properly installed."""

    layer = LEARN_TEACHER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if learn.teacher is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('learn.teacher'))

    def test_uninstall(self):
        """Test if learn.teacher is cleanly uninstalled."""
        self.installer.uninstallProducts(['learn.teacher'])
        self.assertFalse(self.installer.isProductInstalled('learn.teacher'))

    def test_browserlayer(self):
        """Test that ILearnTeacherLayer is registered."""
        from learn.teacher.interfaces import ILearnTeacherLayer
        from plone.browserlayer import utils
        self.assertIn(ILearnTeacherLayer, utils.registered_layers())
