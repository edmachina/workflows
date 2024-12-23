from enum import Enum
from pydantic import BaseModel


def to_list(enum):
    return [e.value for e in enum]


class Status(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class ValueType(Enum):
    STRING = "string"
    INT = "int"
    FLOAT = "float"
    UUID = "uuid"
    STATUS = to_list(Status)


class EqualityOperators(str, Enum):
    EQUAL = "is Equal to"
    NOT_EQUAL = "is Not Equal to"


class ComparisonOperators(str, Enum):
    EQUAL = "is Equal to"
    NOT_EQUAL = "is Not Equal to"
    GREATER_THAN = "is Greater than"
    LESS_THAN = "is Less than"
    GREATER_THAN_OR_EQUAL = "is Greater than or Equal to"
    LESS_THAN_OR_EQUAL = "is Less than or Equal to"


class Filter(BaseModel):
    name: str
    operators: list
    value_type: ValueType


class Category(BaseModel):
    name: str
    filters: list[Filter]


## Student Filters  ##


class StudentGeneralInformationFilters(Enum):
    NAME = Filter(
        name="Student Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    STATUS = Filter(
        name="Student Status",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STATUS,
    )
    EMAIL = Filter(
        name="Student Email",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    TAGS = Filter(
        name="Tags",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )


class StudentRiskFilters(Enum):
    RISK = Filter(
        name="Risk Percentage",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )


class StudentActivityFilters(Enum):
    ACTIVITY_PERCENTAGE = Filter(
        name="Student Activity Percentage",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    LAST_LOGIN = Filter(
        name="Student Last Login",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )
    LAST_CONTACT = Filter(
        name="Student Last Contact",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )


class StudentAcademicDataFilters(Enum):
    PERCENTAGE_OF_ASSIGNMENT_DELIVERED = Filter(
        name="Percentage of Assignment Delivered",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    PERCENTAGE_OF_ASSIGNMENT_PENDING = Filter(
        name="Percentage of Assignment Pending",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    FINAL_GRADE = Filter(
        name="Final Grade",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    NUMBER_OF_COURSES = Filter(
        name="Number of Courses per Student",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )


class StudentFilterCategories(Enum):
    GENERAL_INFORMATION = Category(
        name="General Information", filters=to_list(StudentGeneralInformationFilters)
    )
    ACTIVITY = Category(name="Activity", filters=to_list(StudentActivityFilters))
    RISK = Category(name="Risk", filters=to_list(StudentRiskFilters))
    ACADEMIC_DATA = Category(
        name="Academic Data", filters=to_list(StudentAcademicDataFilters)
    )


## Professor Filters  ##


class ProfessorGeneralInformationFilters(Enum):
    NAME = Filter(
        name="Professor Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    COURSE_NAME = Filter(
        name="Course Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    STATUS = Filter(
        name="Professor Status",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STATUS,
    )
    TAGS = Filter(
        name="Tags", operators=to_list(EqualityOperators), value_type=ValueType.STRING
    )


class ProfessorActivityFilters(Enum):
    LAST_LOGIN = Filter(
        name="Professor Last Login",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )


class ProfessorAcademicDataFilters(Enum):
    NUMBER_OF_COURSES_TAUGHT = Filter(
        name="Number of Courses Taught by Professor",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )
    NUMBER_OF_SECTIONS_TAUGHT = Filter(
        name="Number of Sections Taught by Professor",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )
    NUMBER_OF_STUDENTS_TAUGHT = Filter(
        name="Number of Students Taught by Professor",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )


class ProfessorFilterCategories(Enum):
    GENERAL_INFORMATION = Category(
        name="General Information", filters=to_list(ProfessorGeneralInformationFilters)
    )
    ACTIVITY = Category(name="Activity", filters=to_list(ProfessorActivityFilters))
    ACADEMIC_DATA = Category(
        name="Academic Data", filters=to_list(ProfessorAcademicDataFilters)
    )


## Course Filters  ##


class CourseGeneralInformationFilters(Enum):
    NAME = Filter(
        name="Course Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    SECTION = Filter(
        name="Section Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )
    TAGS = Filter(
        name="Tags", operators=to_list(EqualityOperators), value_type=ValueType.STRING
    )
    STATUS = Filter(
        name="Course Status",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STATUS,
    )
    ASSIGNMENT = Filter(
        name="Assignment Name",
        operators=to_list(EqualityOperators),
        value_type=ValueType.STRING,
    )


class CourseActivityFilters(Enum):
    STUDENT_ACTIVITY = Filter(
        name="Student Activity Percentage",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )


class CourseRiskFilters(Enum):
    RISK = Filter(
        name="Overall Course Risk Percentage",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )


class CourseAcademicDataFilters(Enum):
    FINAL_GRADE = Filter(
        name="Final Grade",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    ASSIGNMENTS_GRADE = Filter(
        name="Assignments Grade",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    PERCENTAGE_OF_ASSIGNMENTS_DELIVERED = Filter(
        name="Percentage of Assignments Delivered",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    PERCENTAGE_OF_ASSIGNMENTS_PENDING = Filter(
        name="Percentage of Assignments Pending",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.FLOAT,
    )
    ASSIGNMENT_DUE_DATE = Filter(
        name="Assignment Due Date",
        operators=to_list(ComparisonOperators),
        value_type=ValueType.INT,
    )


class CourseFilterCategories(Enum):
    GENERAL_INFORMATION = Category(
        name="General Information",
        filters=to_list(CourseGeneralInformationFilters),
    )
    ACTIVITY = Category(name="Activity", filters=to_list(CourseActivityFilters))
    RISK = Category(name="Risk", filters=to_list(CourseRiskFilters))
    ACADEMIC_DATA = Category(
        name="Academic Data", filters=to_list(CourseAcademicDataFilters)
    )


class Filters(BaseModel):
    student: list[Category] = to_list(StudentFilterCategories)
    professor: list[Category] = to_list(ProfessorFilterCategories)
    course: list[Category] = to_list(CourseFilterCategories)
