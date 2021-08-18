from django.urls import path

from apps.finances.api.views import DriverDeptCreateView, DriversRepaymentCreateView, \
    DriversSalaryCreateView, CashRegisterCreateView, CashRegisterView, DriversSalaryView, \
    DriversRepaymentView, DriverDeptView, DriverDeptListView, DriversRepaymentListView, DriverSalaryListView, \
    FinanceListView, FinanceView, FinanceDriverDetailView

urlpatterns = [
    path('', FinanceView.as_view(), name='finances'),
    path('list/', FinanceListView.as_view(), name='finances_list'),
    path('driver/<int:id>/', FinanceDriverDetailView.as_view(), name='finances_driver_detail'),
    path('drivers-dept/create/', DriverDeptCreateView.as_view(), name='driver_dept_create'),
    path('drivers-dept/<int:id>/', DriverDeptView.as_view(), name='driver_dept_detail'),
    path('<int:id>/driver-depts/', DriverDeptListView.as_view(), name='driver_dept_list'),
    path('drivers-repayment/create/', DriversRepaymentCreateView.as_view(), name='driver_repayment_create'),
    path('drivers-repayment/<int:id>/', DriversRepaymentView.as_view(), name='driver_repayment_detail'),
    path('<int:id>/driver-repayments/', DriversRepaymentListView.as_view(), name='driver_repayment_list'),
    path('drivers-salary/create/', DriversSalaryCreateView.as_view(), name='driver_salary_create'),
    path('drivers-salary/<int:id>/', DriversSalaryView.as_view(), name='driver_salary_detail'),
    path('<int:id>/driver-salary/', DriverSalaryListView.as_view(), name='driver_salary_list'),
    path('cash-register/create/', CashRegisterCreateView.as_view(), name='driver_dept_create'),
    path('cash-register/<int:id>/', CashRegisterView.as_view(), name='driver_dept_detail'),
]
