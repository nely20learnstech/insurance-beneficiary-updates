import graphene 
from graphene_django import DjangoObjectType
from .models import Employee, HR

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = "__all__"
        
class HRType(DjangoObjectType):
    class Meta:
        model = HR
        fields = "__all__"

class CreateEmployee(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        employee_id = graphene.String(required=True)
        department = graphene.String(required=True)
        position = graphene.String(required=True)
        date_of_birth = graphene.Date(required=True)
        insurance_policy_number = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, username, email, first_name, last_name, phone_number, employee_id, department, position, date_of_birth, insurance_policy_number):
        employee = Employee(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            employee_id=employee_id,
            department=department,
            position=position,
            date_of_birth=date_of_birth,
            insurance_policy_number=insurance_policy_number
        )
        employee.save()
        return CreateEmployee(employee=employee)
    

class CreateHR(graphene.Mutation):  
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        employee_id = graphene.String(required=True)
        department = graphene.String(required=True)
        position = graphene.String(required=True)
        date_of_birth = graphene.Date(required=True)
        insurance_policy_number = graphene.String(required=True)
        hr_id = graphene.String(required=True)
        is_advisor = graphene.Boolean()
    hr = graphene.Field(HRType)

    def mutate(self, info, username, email, first_name, last_name, phone_number, employee_id, department, position, date_of_birth, insurance_policy_number, hr_id, is_advisor):
        hr = HR(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            employee_id=employee_id,
            department=department,
            position=position,
            date_of_birth=date_of_birth,
            insurance_policy_number=insurance_policy_number,
            hr_id=hr_id,
            is_advisor=is_advisor
        )
        hr.save()
        return CreateHR(hr=hr)
    
class UpdateEmployee(graphene.Mutation):
    class Arguments:
        employee_id = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone_number = graphene.String(required=True)
        department = graphene.String(required=True)
        position = graphene.String(required=True)
        date_of_birth = graphene.Date(required=True)
       

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, employee_id, department=None, position=None, date_of_birth=None, first_name=None, last_name=None, email=None, phone_number=None):
        try:
        # Fetch the employee instance using the provided employee_id
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            raise Exception("Employee not found")
        
        # Update the employee instance with the provided data
        if department:
            employee.department = department
        if position:
            employee.position = position    
        if first_name:
            employee.first_name = first_name
        if last_name:
            employee.last_name = last_name
        if email:
            employee.email = email
        if phone_number:
            employee.phone_number = phone_number
        if date_of_birth:
            employee.date_of_birth = date_of_birth

        # Save the updated employee instance
        employee.save()
        return UpdateEmployee(employee=employee)

class DeleteEmployee(graphene.Mutation):
    class Arguments:
        employee_id = graphene.String(required=True)

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, employee_id):
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            employee.delete()
            return DeleteEmployee(employee=employee)
        except Employee.DoesNotExist:
            raise Exception("Employee not found")
        
class DeleteHR(graphene.Mutation):
    class Arguments:
        hr_id = graphene.String(required=True)

    hr = graphene.Field(HRType)

    def mutate(self, info, hr_id):
        try:
            hr = HR.objects.get(hr_id=hr_id)
            hr.delete()
            return DeleteHR(hr=hr)
        except HR.DoesNotExist:
            raise Exception("HR not found")

class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    create_hr = CreateHR.Field()