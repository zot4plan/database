"""
Course is a class is responsible for storing information of each individual
UCI courses. 
"""
class Course:
    """
    Initialize all attributes needed to store a UCI course's information
    """
    def __init__(self):
        self.course_id = ''
        self.name = ''
        self.department = ''
        self.units = [0, 0]
        self.units_text = '0'
        self.description = ''
        self.prerequisite = ''
        self.prerequisite_tree = ''
        self.prerequisite_for = []
        self.corequisite = ''
        self.corequisite_tree = ''
        self.prerequisite_or_corequisite = ''
        self.prerequisite_or_corequisite_tree = ''
        self.restriction = ''
        self.same_as = ''
        self.overlaps_with = ''
        self.concurrent_with = ''
        self.repeatability = 1
        self.ge_string = ''
        self.ge_list = []
        self.terms = ''


    def set_header_info(self, header_info):
        """
        set_header takes in a string of information (Course header in UCI catalogue) 
        and split the string up by parts ('.'). Using given
        informtation, set attributes: name, course_key, and untis
        :param header_info: string that contains course key, course name, and units 
        """

        header_info = header_info.split('.  ')
        self.name = header_info[1].strip().replace('\'', '\'\'')
        self.course_id = header_info[0].replace("\u00a0", " ")

        get_dept = self.course_id.split(" ")[:-1]
        self.department = " ".join(get_dept)
        
        if header_info[2] != "":
            self.units_text = header_info[2]

        units = header_info[2].split(' ')[0]
        units = [0 if elem == '' else float(elem) if float(elem) % 1 != 0 else int(float(elem)) for elem in units.split('-')]

        if len(units) == 1:
            units.append(units[0])
            
        self.units = units


    def set_description(self, raw_description):
        """
        set_description takes in a raw text was scraped from UCI Catalogue and
        set the value to attribute description
        :param raw_description: string that contains the course description
        """
        self.description = raw_description.replace('\'', '\'\'')


    def set_information(self, raw_info):
        """
        set_information takes in a raw text was scraped from UCI Catalogue and set the
        value based on its content. The class method searches for certain key terms and
        execute accordingly. Possible class attribute changes: restriction, prerequisite,
        and corequisite
        :param raw_info: a string containing course information
        """
        raw_info = raw_info.replace('\xa0', ' ').replace('\'', '\'\'').splitlines()

        for elem in raw_info:
            if elem == '':
                continue
            if 'Restriction:' in elem:
                self.restriction = elem.replace('Restriction:', '').strip()
            elif 'Prerequisite:' in elem:
                self.prerequisite = elem.replace('Prerequisite:','').strip()
            elif 'Prerequisite or corequisite:' in elem:
                self.prerequisite_or_corequisite = elem.replace('Prerequisite or corequisite:','')
            elif 'Same as' in elem:
                self.same_as = elem.replace('Same as ', '').strip()
            elif 'Overlaps with' in elem:
                self.overlaps_with = elem.replace('Overlaps with ', '').strip()
            elif 'Concurrent with' in elem:
                self.concurrent_with = elem.replace('Concurrent with ', '').strip()
            elif 'Corequisite:' in elem:
                self.corequisite = elem.replace('Corequisite:', '').strip()


    def set_ge(self, ge_text):
        """
        set_ge takes in a string that contains information regarding course's GE category. The string
        will be saved in two format: string (display purposes) and list (checking purposes).
        :param raw_text_ge: string that contains information regarding course's GE
        """
        roman_chars = {'I', 'V', 'A', 'B'}
        ge_categories = {'IA', 'IB', 'II', 'III', 'IV',
                    'VA', 'VB', 'VI', 'VII', 'VIII'}

        ge_string = ''
        for elem in ge_text:
            if elem != '.':
                ge_string += elem.upper()
        self.ge_string = ge_string

        current = ''
        for char in self.ge_string:
            if char in roman_chars:
                current += char
            elif current != '':
                if current in ge_categories:
                    self.ge_list.append(current)
                current = ''

    
    def set_repeatability(self, raw_info):
        """
        set_repeatability takes in a raw text scraped from the UCI course catalogue and
        determines how many time a course can be taken for credit
        :param raw_info: a string that contains course's information regarding course repeatability
        """ 

        if 'Unlimited' in raw_info or 'unlimited' in raw_info:
            self.repeatability = 9
        else:
            repeat = raw_info.split(' ')
            for char in repeat:
                if char.isdigit():
                    self.repeatability = int(char)
                    break


    def set_terms(self, all_terms):
        """
        set_terms takes in a list of past terms and convert it into a string
        :param all_terms: list of past terms that offered the course
        """
        past_terms = dict()
        terms_in_order = ['Fall', 'Winter', 'Spring', 'Summer1', 'Summer10wk', 'Summer2']
        for term in all_terms:
            year, quarter = term.split(' ')
            if quarter in past_terms:
                past_terms[quarter] += ', ' + str(year)
            else:
                past_terms[quarter] = str(year)
        
        in_string = ''
        for term in terms_in_order:
            if term in past_terms:
                in_string += term + ': ' + past_terms[term] + '.'
        self.terms = in_string


    def set_prereq_info(self, prerequisite_for: str):
        self.prerequisite_for = prerequisite_for
    