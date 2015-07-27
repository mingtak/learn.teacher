# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from learn.teacher import _
from zope import schema
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationList, RelationChoice
from zope.interface import Interface
#from zope.interface import provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.autoform import directives
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.supermodel import model
#from plone.autoform.interfaces import IFormFieldProvider


class ILearnTeacherLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITeacher(Interface):

    model.fieldset(
        'Basic',
        label=_(u'Basic_Information', default=u'Basic Information'),
        fields=['title',
                'description',
                'text',
                'image',
                'subjects'],
    )

    title = schema.TextLine(
        title=_(u"Teacher's name"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Short description"),
        required=False,
    )

    text = RichText(
        title=_(u"Detail Description"),
        description=_(u"Detail introduction"),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Lead image"),
        required=False,
    )

    subjects = schema.Tuple(
        title=_(u'Specialty'),
        description=_(
            u'help_specialty',
            default=u'Please select your specialty or direct fill new one.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'subjects',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )

    model.fieldset(
        'Social',
        description=_("help_social",
            default="We support multi social media, you fill in , we promote it. / Must be include http://"),
        label=_(u'Social_Network', default=u'Social Network'),
        fields=['facebook',
                'googlePlus',
                'youtube',
                'twitter',
                'linkedIn',
                'instagram'],
    )

    facebook = schema.URI(
        title=_(u"Facebook"),
        required=False,
    )

    googlePlus = schema.URI(
        title=_(u"Google+"),
        required=False,
    )

    youtube = schema.URI(
        title=_(u"Youtube"),
        required=False,
    )

    twitter = schema.URI(
        title=_(u"Twitter"),
        required=False,
    )

    linkedIn = schema.URI(
        title=_(u"Linked In"),
        required=False,
    )

    instagram = schema.URI(
        title=_(u"Instagram"),
        required=False,
    )


class ICourse(Interface):

    model.fieldset(
        'Course',
        label=_(u'Course_Information', default=u'Course Information'),
        fields=['title',
                'description',
                'subjects',
                'start',
                'end',
                'image',
                'classroom',
                'place',
                'quota',
                'fee',
                'text'],
    )

    title = schema.TextLine(
        title=_(u"Course title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Short description"),
        required=False,
    )

    text = RichText(
        title=_(u"Detail Description"),
        description=_(u"Detail introduction"),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Lead image"),
        description=_(u"help_image", default="Recommended image size aspect ratio of 3:1"),
        required=False,
    )

    classroom = schema.Bool(
        title=_(u"Provide classroom"),
        description=_(u"Have provide classroom?"),
        default=False,
        required=True,
    )

    place = schema.TextLine(
        title=_(u"Classroom place"),
        description=_(u"If provide classroom, please fill this field."),
        required=False,
    )

    quota = schema.Int(
        title=_(u"Quota"),
        description=_(u"Expected quota of student."),
        required=True,
    )

    fee = schema.TextLine(
        title=_(u"Learning Fee"),
        required=False,
    )

    start = schema.Datetime(
        title=_(u"Course Start Date/Time"),
        required=False,
    )

    end = schema.Datetime(
        title=_(u"Course End Date/Time"),
        required=False,
    )

    subjects = schema.Tuple(
        title=_(u'Categories'),
        description=_(
            u'help_Categories',
            default=u"Please select this course's Categories or direct fill new one."
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'subjects',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )


class IOutline(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"About course outline"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Short description"),
        required=False,
    )

    text = RichText(
        title=_(u"Detail Description"),
        description=_(u"Detail Course outline"),
        required=False,
    )


class IStudent(Interface):

    title = schema.TextLine(
        title=_(u"Name"),
        description=_(u"Your name, or nickname."),
        required=True,
    )

    description = schema.Text(
        title=_(u"Introduction"),
        required=False,
    )

    watchedTeacher = RelationList(
        title=_(u"Watched teacher"),
        default=[],
        value_type=RelationChoice(
            title=_(u"Related"),
            vocabulary="plone.app.vocabularies.Catalog",
            required=False
        ),
        required=False,
    )

    watchedCourse = RelationList(
        title=_(u"Related course"),
        value_type=RelationChoice(
            title=_(u"Related"),
            vocabulary="plone.app.vocabularies.Catalog",
            required=False
        ),
        required=False
    )


class IChild(Interface):

    title = schema.TextLine(
        title=_(u"Name"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Introduction"),
        required=False,
    )
