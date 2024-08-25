Permissions and Groups Setup

Custom Permissions
The following custom permissions have been added to the `book model`:
- `can_view`: Allows users to view instances of the model.
- `can_create`: Allows users to create new instances of the model.
- `can_edit`: Allows users to edit instances of the model.
- `can_delete`: Allows users to delete instances of the model.

User Groups
The following user groups have been configured:
- **Viewers**: Assigned the `can_view` permission.
- **Editors**: Assigned the `can_view`, `can_create`, and `can_edit` permissions.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

Enforcing Permissions in Views
Views have been modified to check for the required permissions using the `@permission_required` decorato