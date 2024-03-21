from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAdmin(permissions.BasePermission):

    """
    Custom permission to only allow creator of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
 
        return self.has_permission(request, view)


    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return request.user
        else:
            raise PermissionDenied
        
class IsUser(permissions.BasePermission):
    
    """
    Custom permission to only allow creator of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
 
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        if request.user.role == 'user':
            return request.user
        else:
            raise PermissionDenied
        
class IsDriver(permissions.BasePermission):
    
    """
    Custom permission to only allow creator of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
 
        return self.has_permission(request, view)

    def has_permission(self, request, view):
        if request.user.role == 'driver':
            return request.user
        else:
            raise PermissionDenied
        
        
    
        
