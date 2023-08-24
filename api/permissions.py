# from rest_framework.permissions import BasePermission

# from accounts.models import Account


# class IsAdmin(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return bool(
#             request.user and request.user.is_active and request.user.is_staff and request.user.role == Account.Role.ADMIN)


# class IsReceptionist(BasePermission):
#     def has_permission(self, request, view):
#         if not request.user.is_authenticated:
#             return False
#         return bool(
#             request.user and request.user.is_active and request.user.role == Account.Role.RECEPTIONIST or
#             request.user.role == Account.Role.ADMIN)
