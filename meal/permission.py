from rest_framework import permissions 


class UpdateOwnRating(permissions.BasePermission):

    def has_object_permission(self ,request ,view ,obj):
        
        print(f"the request is --{request}" ) 
        print(view)
        print(obj.user)
        print(request.user)
        if request.method in permissions.SAFE_METHODS:
            return True
        elif  obj.user == request.user:  
            return True 
        return False  

class Readalmost(permissions.BasePermission):

   def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False 

