__author__ = 'dmorina'
from rest_framework import permissions

class IsProjectCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        for collaborator in obj.collaborators.all():
            if collaborator.profile.user==request.user:
                return True

        return False

class IsReviewerOrRaterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.worker.profile.user == request.user

     



