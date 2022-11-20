from rest_framework.permissions import BasePermission, SAFE_METHODS
from softdesk_api.models import Contributor

class IsAuthorOrReadOnly(BasePermission):
    """
    Permission to only allow author to request PUT and DELETE method.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author_user_id == request.user

class IsContributor(BasePermission):
    """
    Permission to only allow contributors of a project to request SAFE METHODS (GET, OPTIONS and HEAD).
    """
    def has_object_permission(self, request, view, obj):
        contributor = Contributor.objects.get(user_id=request.user.user_id)
        return obj.project_id == contributor.project_id.project_id and request.method in SAFE_METHODS