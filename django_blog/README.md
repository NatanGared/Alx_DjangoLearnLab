# Authentication System Documentation

## Features
- **User Registration**: Users can register by filling out a form with their username, email, and password.
- **User Login**: Registered users can log in using their credentials.
- **User Logout**: Users can log out to end their session.
- **Profile Management**: Users can view and edit their profile information, such as their email.

## How to Test
1. Navigate to `/register/` to create a new account.
2. Use `/login/` to log in with the newly created account.
3. Access `/profile/` to view and update the user's email.
4. Use `/logout/` to log out.

## Security Measures
- All forms use CSRF tokens.
- Passwords are securely hashed using Django's built-in methods.

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


# Comment System Documentation

## Overview
The comment system allows users to engage with blog posts by leaving comments. Authenticated users can create, edit, and delete their comments.

## Features
- **Post Comments**: Users can add comments to blog posts.
- **Edit Comments**: Users can edit their comments if they are the author.
- **Delete Comments**: Users can delete their comments if they are the author.
- **View Comments**: All users can see comments on blog posts.

## How to Use
1. Navigate to a blog post to view existing comments and add your own.
2. Click "Edit" next to your comment to modify it.
3. Click "Delete" to remove your comment.

## Permissions
- Only authenticated users can post comments.
- Only the author of a comment can edit or delete it.