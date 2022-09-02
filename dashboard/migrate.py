from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from employees.models import Employee, Salary
from django.contrib.auth.models import User


# https://stackoverflow.com/questions/6791911/execute-code-when-django-starts-once-only
def add_superuser():
    # Add Superuser
    try:
        superuser = User.objects.get(email='mahdi7ab@gmail.com')
    except User.DoesNotExist:
        User.objects.create_superuser(
            username='mahdi7ab', email='mahdi7ab@gmail.com', password="P@ss23??")


# https://stackoverflow.com/questions/22250352/programmatically-create-a-django-group-with-permissions
def add_permissions_and_group():  # Permissions
    employee_ct = ContentType.objects.get_for_model(Employee)
    salary_ct = ContentType.objects.get_for_model(Salary)
    can_change_employee, ic1 = Permission.objects.get_or_create(codename='can_change_employee',
                                                                name='Can change employee',
                                                                content_type=employee_ct)

    can_view_employee, ic2 = Permission.objects.get_or_create(codename='can_view_employee',
                                                              name='Can view employee',
                                                              content_type=employee_ct)

    can_view_salary, ic3 = Permission.objects.get_or_create(codename='can_view_salary',
                                                            name='Can view salary',
                                                            content_type=salary_ct)
    can_add_salary, ic4 = Permission.objects.get_or_create(codename='can_add_salary',
                                                           name='Can add salary',
                                                           content_type=salary_ct)
    can_change_salary, ic5 = Permission.objects.get_or_create(codename='can_change_salary',
                                                              name='Can change salary',
                                                              content_type=salary_ct)
    can_delete_salary, ic6 = Permission.objects.get_or_create(codename='can_delete_salary',
                                                              name='Can delete salary',
                                                              content_type=salary_ct)
    # HrManager
    HrManagerGroup, hr_created = Group.objects.get_or_create(
        name='HrManagers')
    if hr_created:
        HrManagerGroup.permissions.add(can_change_employee)
        HrManagerGroup.permissions.add(can_view_employee)
        HrManagerGroup.permissions.add(can_view_salary)
    # PayrollManager
    PayrollManagerGroup, pr_created = Group.objects.get_or_create(
        name='PayrollManagers')
    if pr_created:
        PayrollManagerGroup.permissions.add(can_view_employee)
        PayrollManagerGroup.permissions.add(can_view_salary)
        PayrollManagerGroup.permissions.add(can_add_salary)
        PayrollManagerGroup.permissions.add(can_change_salary)
        PayrollManagerGroup.permissions.add(can_delete_salary)


# https://stackoverflow.com/questions/6288661/adding-a-user-to-a-group-in-django
# https://stackoverflow.com/questions/39164249/django-authenticate-is-not-working-for-users-created-by-register-page-but-w
def add_hr_manager():
    # create HrManager
    hr_manager, is_hr_manager_created = User.objects.get_or_create(
        username='HrManager', email='HrManager@soton.ir')
    if is_hr_manager_created:
        HrManagerGroup = Group.objects.get(name='HrManagers')
        hr_manager.set_password("P@ss23??")
        hr_manager.groups.add(HrManagerGroup)
        hr_manager.save()
        HrManagerGroup.user_set.add(hr_manager)


def add_payroll_manager():
    # create PayrollManager
    payroll_manager, is_payroll_manager_created = User.objects.get_or_create(
        username='PayrollManager', email='PayrollManager@soton.ir')
    if is_payroll_manager_created:
        PayrollManagerGroup = Group.objects.get(name='PayrollManagers')
        payroll_manager.set_password("P@ss23??")
        payroll_manager.groups.add(PayrollManagerGroup)
        payroll_manager.save()
        PayrollManagerGroup.user_set.add(payroll_manager)
