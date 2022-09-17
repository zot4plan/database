import pytest
import sys
sys.path.insert(1, '../app/models')
from Course import Course
 
@pytest.fixture
def new_course():
   return Course()


class TestSetHeaderInfo:

    def test_header_name_course(self, new_course):
        new_course.set_header_info('AC ENG 22A.  Academic English Reading and Vocabulary.  2 Units.   ')
        assert new_course.name == 'Academic English Reading and Vocabulary'
        assert new_course.course_key == 'AC ENG 22A'


    def test_header_one_digit_unit(self, new_course):
        new_course.set_header_info('AC ENG 22A.  Academic English Reading and Vocabulary.  2 Units.   ')
        assert new_course.units_str == '2 Units'
        assert new_course.units_range == [2.0, 2.0]


    def test_header_units_range(self, new_course):
        new_course.set_header_info('ANTHRO 299.  Independent Study.  4-12 Units.  ')
        assert new_course.units_str == '4-12 Units'
        assert new_course.units_range == [4.0, 12.0]


    def test_header_units_with_decimals(self, new_course):
        new_course.set_header_info('UNI AFF 1C.  Student Participation.  1.3 Unit.  ')
        assert new_course.units_str == '1.3 Unit'
        assert new_course.units_range == [1.3, 1.3]


    def test_header_range_with_decimals(self, new_course):
        new_course.set_header_info('COGS 229.  Special Topics in Human Cognition.  1.3-4 Units.  ')
        assert new_course.units_str == '1.3-4 Units'
        assert new_course.units_range == [1.3, 4.0]


    def test_header_no_units(self, new_course):
        new_course.set_header_info('BANA 211.  MSBA ProSeminar.  ')
        assert new_course.units_str == '0'
        assert new_course.units_range == [0.0, 0.0]


class TestSetDescription:

    def test_set_description(self, new_course):
        description = 'Grammar, sentence structure, paragraph and essay organization of formal written English.'
        new_course.set_description(description)
        assert new_course.description == description


class TestSetInformation:

    def test_set_prereq_only(self, new_course):
        new_course.set_information('Prerequisite: AC\xa0ENG\xa020A. Placement into AC\xa0ENG\xa020B is also accepted.\n')
        assert new_course.prerequisite == ' AC ENG 20A. Placement into AC ENG 20B is also accepted.'
    

    def test_set_pre_or_core(self, new_course):
        new_course.set_information('Prerequisite or corequisite: ANTHRO\xa0199\n')
        assert new_course.pre_or_core == ' ANTHRO 199'
        assert new_course.prerequisite == ''
        assert new_course.corequisite == ''


    def test_set_core_and_pre(self, new_course):
        new_course.set_information('Corequisite: ART\xa0262\nPrerequisite: ART\xa0210 and ART\xa0215 and ART\xa0220\n')
        assert new_course.corequisite == ' ART 262'
        assert new_course.prerequisite == ' ART 210 and ART 215 and ART 220'
        assert new_course.pre_or_core == ''


    def test_set_restriction_only(self, new_course):
        new_course.set_information('Restriction: Restricted to students whose first language is not English.')
        assert new_course.restriction == ' Restricted to students whose first language is not English.'


    def test_set_concurrent_with_only(self, new_course):
        new_course.set_information('Concurrent with ART\xa0HIS\xa0255A.')
        assert new_course.concurrent_with == 'ART HIS 255A.'


    def test_same_as_only(self, new_course):
        new_course.set_information('Same as INTL\xa0ST\xa011.\n')
        assert new_course.same_as == 'INTL ST 11.'


    def test_set_same_as_with_overlaps_with(self, new_course):
        new_course.set_information('Same as SOCIOL\xa010C.\nOverlaps with PSYCH\xa010C, SOCECOL\xa013, SOC\xa0SCI\xa010C, POL\xa0SCI\xa010C.\n')
        assert new_course.same_as == 'SOCIOL 10C.'
        assert new_course.overlaps_with == 'PSYCH 10C, SOCECOL 13, SOC SCI 10C, POL SCI 10C.'


class TestRepeatability:


    def test_unlimited_repeatablity(self, new_course):
        new_course.set_repeatability('Repeatability: Unlimited as topics vary.')
        assert new_course.repeatability == 9


    def test_limited_repeatability(self, new_course):
        new_course.set_repeatability('Repeatability: May be taken for credit 3 times.')
        assert new_course.repeatability == 3    


class TestGE:

    def test_one_ge_cat(self, new_course):
        new_course.set_ge('(Ib)')
        assert new_course.ge_list == ['IB']
        assert new_course.ge_string == '(IB)'


    def test_two_ge(self, new_course):
        new_course.set_ge('(II and VA ).')
        assert new_course.ge_list == ['II', 'VA']
        assert new_course.ge_string == '(II AND VA )'


    def test_ge_cat_with_period(self, new_course):
        new_course.set_ge('(II and V.A. ).')
        assert new_course.ge_list == ['II', 'VA']
        assert new_course.ge_string == '(II AND VA )'


class TestSetPreReqInfo:

    def test_prereq_tree(self, new_course):
        mock_info = {'tree': '{\"AND\":[\"I&C SCI 51\"]}',
                    'prereq_for': ["COMPSCI 122C","COMPSCI 131","COMPSCI 222","I&C SCI 53L"]}
        new_course.set_prereq_info(mock_info)
        assert new_course.prerequisite_tree == '{\"AND\":[\"I&C SCI 51\"]}'
        assert new_course.prerequisite_for == ["COMPSCI 122C","COMPSCI 131","COMPSCI 222","I&C SCI 53L"]


class TestSetTerms:

    def test_multiple_terms(self, new_course):
        terms = ["2019 Spring","2020 Fall","2019 Fall","2019 Winter",
                "2018 Winter","2018 Spring","2017 Winter","2017 Spring"]
        new_course.set_terms(terms)
        assert new_course.past_terms == 'Fall: 2020, 2019.Winter: 2019, 2018, 2017.Spring: 2019, 2018, 2017.'
