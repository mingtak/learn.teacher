# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from learn.teacher.testing import LEARN_TEACHER_INTEGRATION_TESTING  # noqa
from learn.teacher.interfaces import ITeacher

import unittest2 as unittest


class TeacherIntegrationTest(unittest.TestCase):

    layer = LEARN_TEACHER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Teacher')
        schema = fti.lookupSchema()
        self.assertEqual(ITeacher, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Teacher')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Teacher')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITeacher.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Teacher', 'Teacher')
        self.assertTrue(
            ITeacher.providedBy(self.portal['Teacher'])
        )
