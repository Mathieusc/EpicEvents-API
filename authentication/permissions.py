from lib2to3.pytree import Base
from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermissions(BasePermission):
    message = "Access denied."

    def has_permission(self, request, view):
        user = request.user
        role = user.role

        if request.method in ["GET"]:
            return True

        if request.method in ["POST"]:
            if role != 3:
                return False

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if role != 2:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.role != 2:
            return False

        if request.user.role == 2:
            if request.method in SAFE_METHODS:
                return True

        if request.method in ["PUT", "PATCH", "DELETE"]:
            if obj.support_contact.id == request.user.id:
                return True
            return False

        return False


class SalesPermissions(BasePermission):
    """
    Sales permissions
    A sales user can:
        - Add new clients
        - Add an event for a contract
        - Display and update only clients assigned to them
        - Display and update only the client's contract assigned to them
    """

    # def has_permission(self, request, view):
    #     print("mange")
    #     if request.user.role == 2:
    #         if request.method in ["POST"]:
    #             return False
    #         return True
    #     elif request.user.role == 3 or request.user.role == 1:
    #         if request.method in ["GET"]:
    #             return True

    #     return True

    # def has_object_permission(self, request, view, obj):
    #     if request.user.role != 3 or request.user.role != 1:
    #         return False
    #     print(obj)
    #     print(request.user.role)
    #     print(view.action)
    #     if obj.sales_contact.id == request.user.id:
    #         if request.method in ["GET", "PUT", "PATCH", "DELETE", "POST"]:
    #             return True
    #     return False

    def has_permission(self, request, view):
        user = request.user
        role = user.role
        print(view.action)
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action in ["create", "destroy"]:
            if not role == 3 or not role == 1:
                return False
            return True

        elif view.action in ["update"]:
            if role == 1 or role == 3:
                return True
            return False

    # def has_object_permission(self, request, view, obj):
    #     print(view.action)
    #     user = request.user
    #     role = user.role

    #     if obj.sales_contact.id == user.id or role == 1:
    #         return True
    #     return False


class SupportPermissions(BasePermission):
    """
    Support permissions
    A support user can:
        - Display and update events assigned to them
        - Display clients (for the client's events assigned to them)
    """

    # def has_object_permission(self, request, view, obj):
    #     if request.user.role != 2:
    #         return False

    #     if request.method in ["GET", "PUT", "PATCH"]:
    #         if obj.support_contact.id == request.user.id:
    #             return True
    #         return False

    #     return False

    def has_permission(self, request, view):
        user = request.user
        role = user.role

        if view.action in ["list", "retrieve", "update"]:
            return True

        elif view.action in ["create", "destroy"]:
            if not role == 3:
                return False
            return True


class ManagerPermissions(BasePermission):
    """
    Manager permissions:
    Only a manager can create accounts.
    """

    message = "Acces reserved for managers."

    def has_permission(self, request, view):

        user = request.user
        role = user.role

        if not role == 1:
            return False
        return True
