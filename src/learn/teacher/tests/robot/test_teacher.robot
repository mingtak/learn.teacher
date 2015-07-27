# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s learn.teacher -t test_teacher.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src learn.teacher.testing.LEARN_TEACHER_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_teacher.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Teacher
  Given a logged-in site administrator
    and an add teacher form
   When I type 'My Teacher' into the title field
    and I submit the form
   Then a teacher with the title 'My Teacher' has been created

Scenario: As a site administrator I can view a Teacher
  Given a logged-in site administrator
    and a teacher 'My Teacher'
   When I go to the teacher view
   Then I can see the teacher title 'My Teacher'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add teacher form
  Go To  ${PLONE_URL}/++add++Teacher

a teacher 'My Teacher'
  Create content  type=Teacher  id=my-teacher  title=My Teacher


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the teacher view
  Go To  ${PLONE_URL}/my-teacher
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a teacher with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the teacher title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
