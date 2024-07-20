class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"

class UserManagement:
    def __init__(self):
        self.users = []

    async def create_user(self, name: str, email: str, password: str) -> User:
        new_user = User(name, email, password)
        self.users.append(new_user)
        return new_user

    async def login_user(self, email: str, password: str) -> bool:
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False

    async def get_all_users(self) -> list:
        return self.users

    async def create_document(self):
        user = await self.create_user('nischal', 'nishal@node.js', 'admin')
        print('User created:', user)

# Example usage:
import asyncio

async def main():
    user_manager = UserManagement()
    await user_manager.create_document()
    users = await user_manager.get_all_users()
    print('All users:', users)
    is_logged_in = await user_manager.login_user('nishal@node.js', 'admin')
    print('Login successful:', is_logged_in)

asyncio.run(main())
