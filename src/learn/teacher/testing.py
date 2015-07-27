# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig

import learn.teacher


class LearnTeacherLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.file(
            'configure.zcml',
            learn.teacher,
            context=configurationContext
        )

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'learn.teacher:default')


LEARN_TEACHER_FIXTURE = LearnTeacherLayer()


LEARN_TEACHER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LEARN_TEACHER_FIXTURE,),
    name='LearnTeacherLayer:IntegrationTesting'
)


LEARN_TEACHER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LEARN_TEACHER_FIXTURE,),
    name='LearnTeacherLayer:FunctionalTesting'
)


LEARN_TEACHER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        LEARN_TEACHER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='LearnTeacherLayer:AcceptanceTesting'
)
