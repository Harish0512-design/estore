from rest_framework import permissions


# creating a permission class for Buyer
class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user belongs to the 'Buyer' group
        return request.user.groups.filter(name='Buyer').exists()


# creating a permission class for Seller
class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for all users
        if request.method == 'GET':
            return True

        # Check if the user belongs to the 'Seller' group for POST, PUT, DELETE requests
        return request.user.groups.filter(name='Seller').exists()
