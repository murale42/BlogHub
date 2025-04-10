from rest_framework import permissions

#Разрешает редактировать и удалять пост только автору.
class IsAuthorOrReadOnly(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True     
        # Разрешает изменение и удаление только автору поста
        return obj.author == request.user

class IsCommentAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user