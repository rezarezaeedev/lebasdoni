from rest_framework.permissions import BasePermission


class IsOwnerUserForCart(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class IsOwnerUserForCartItem(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.cart.user.id == request.user.id
