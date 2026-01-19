# -*- coding: utf-8 -*-
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import privacyforms.theme


class PrivacyformsThemeLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=privacyforms.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "privacyforms.theme:default")


PRIVACYFORMS_THEME_FIXTURE = PrivacyformsThemeLayer()


PRIVACYFORMS_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRIVACYFORMS_THEME_FIXTURE,),
    name="PrivacyformsThemeLayer:IntegrationTesting",
)


PRIVACYFORMS_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRIVACYFORMS_THEME_FIXTURE,),
    name="PrivacyformsThemeLayer:FunctionalTesting",
)
