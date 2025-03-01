# Permissions and Groups Setup

## Overview
This Django application uses custom permissions and groups to manage access control.

## Custom Permissions
- `can_view`: Allows users to view books.
- `can_create`: Allows users to create new books.
- `can_edit`: Allows users to edit existing books.
- `can_delete`: Allows users to delete books.

## Groups
- **Editors**: Can create and edit books.
- **Viewers**: Can view books.
- **Admins**: Has all permissions.

## How to Assign Permissions
1. Go to the Django admin panel.
2. Navigate to **Auth** > **Groups**.
3. Create or modify groups and assign the appropriate permissions.

## Enforcing Permissions
Permissions are enforced in views using the `@permission_required` decorator. If a user does not have the required permission, they will be redirected or receive a 403 Forbidden error.