# -*- coding: utf-8 -*-
"""Setup tests for this package."""

from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from privacyforms.theme.testing import (  # noqa: E501
    PRIVACYFORMS_THEME_INTEGRATION_TESTING,
)

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that privacyforms.theme is properly installed."""

    layer = PRIVACYFORMS_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if privacyforms.theme is installed."""
        self.assertTrue(self.installer.is_product_installed("privacyforms.theme"))

    def test_browserlayer(self):
        """Test that IPrivacyformsThemeLayer is registered."""
        from plone.browserlayer import utils
        from privacyforms.theme.interfaces import IPrivacyformsThemeLayer

        self.assertIn(IPrivacyformsThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = PRIVACYFORMS_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("privacyforms.theme")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if privacyforms.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("privacyforms.theme"))

    def test_browserlayer_removed(self):
        """Test that IPrivacyformsThemeLayer is removed."""
        from plone.browserlayer import utils
        from privacyforms.theme.interfaces import IPrivacyformsThemeLayer

        self.assertNotIn(IPrivacyformsThemeLayer, utils.registered_layers())
