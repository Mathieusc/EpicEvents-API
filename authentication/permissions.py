from rest_framework.permissions import BasePermission, SAFE_METHODS

from events.models import Event


class ClientPermissions(BasePermission):
    message = "Access denied."

    def has_permission(self, request, view):
        if request.user.role == 2:
            return request.method in SAFE_METHODS
        return True

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `owner`.
        # return obj.owner == request.user

        event = Event.objects.filter(support_contact=request.user, client=obj)
        if request.user.role == 2:
            if event:
                return request.method in SAFE_METHODS
            return False

        elif request.user.role == 3:
            if obj.sales_contact.id == request.user.id:
                if request.method == "DELETE":
                    return False
                return True

        elif request.user.role == 1:
            return True


class ManagerAndSalesPermissions(BasePermission):
    message = "Access denied."

    def has_permission(self, request, view):
        user = request.user
        role = user.role

        if view.action in ["list", "retrieve"]:
            return True

        if view.action in ["create"]:
            if role == 3:
                return True

        if view.action in ["update"]:
            if role == 1 or role == 3:
                return True


class SupportPermissions(BasePermission):
    message = "Access denied"

    def has_permission(self, request, view):
        if request.user.role == 2:
            if view.action in ["list", "retrieve", "update"]:
                return True
