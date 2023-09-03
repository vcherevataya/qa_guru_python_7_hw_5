import os

from selene import browser, be, have


def test_demoqa_registration_form(setup_browser):
    browser.open('/automation-practice-form')
    # Заполнение полей
    browser.element('#firstName').type('Lera').press_tab()
    browser.element('#lastName').type('Cherevataya').press_tab()
    browser.element('#userEmail').type('chlera@mail.ru').press_tab()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type(8925354578).press_tab()
    browser.element('.react-datepicker__month-select>option[value="3"]').click()
    browser.element('.react-datepicker__year-select>option[value="1998"]').click()
    browser.element('.react-datepicker__day--007').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/1.jpg'))
    browser.element('#currentAddress').type('Nakhimova, bld. 6/А, appt. 166').press_tab()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Gurgaon').press_enter().press_tab().press_enter()

    #Проверки
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Lera Cherevataya'))
    browser.element('.table').should(have.text('chlera@mail.ru'))
    browser.element('.table').should(have.text('7 April,1998'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('8925354578'))
    browser.element('.table').should(have.text('Maths'))
    browser.element('.table').should(have.text('Reading'))
    browser.element('.table').should(have.text('1.jpg'))
    browser.element('.table').should(have.text('Nakhimova, bld. 6/А, appt. 166'))
    browser.element('.table').should(have.text('NCR Gurgaon'))

