from rest_framework.permissions import BasePermission


class IsSales(BasePermission):
    """
    Permission for sales users: role 3 in charge of a client/contract
    Role 1 are the managers, they can only get/update.
    """

    message = "Message d'erreur à faire"

    def has_permission(self, request, view):
        user = request.user
        role = user.role

        if view.action in ["list", "retrieve"]:
            return True
        elif view.action in ["create", "destroy"]:
            if not role == 3:
                return False
            return True

        elif view.action in ["update"]:
            if role == 1 or role == 3:
                return True
            return False
