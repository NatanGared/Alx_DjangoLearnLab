# Blog Post Management

## Features
- **Create**: Authenticated users can create new blog posts.
- **Read**: All users can view the list of posts and individual post details.
- **Update**: Only authors can edit their posts.
- **Delete**: Only authors can delete their posts.

## URL Patterns
- `/posts/`: List all posts.
- `/posts/new/`: Create a new post.
- `/posts/<int:pk>/`: View details of a post.
- `/posts/<int:pk>/edit/`: Edit an existing post.
- `/posts/<int:pk>/delete/`: Delete a post.