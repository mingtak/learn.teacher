from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class WatchTeacher(base.ViewletBase):

    index = ViewPageTemplateFile('template/watch_teacher.pt')

    def render(self):
        return self.index()


class WatchCourse(base.ViewletBase):

    index = ViewPageTemplateFile('template/watch_course.pt')

    def render(self):
        return self.index()

