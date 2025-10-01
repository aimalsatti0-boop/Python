class LoginSystem:
    def __init__(self, username, password, max_attempts=3):
        self._username = username
        self._password = password
        self.max_attempts = max_attempts
        self.attempts = 0

    def login(self):
        print("\n--- LOGIN ---")
        while self.attempts < self.max_attempts:
            name = input("Enter Your Username: ")
            password = input("Enter Your Password: ")

            if name == self._username and password == self._password:
                print("\n✅ LOGIN SUCCESSFUL.")
                self.attempts = 0
                return True
            else:
                self.attempts += 1
                attempts_remaining = self.max_attempts - self.attempts
                if attempts_remaining > 0:
                    print(f"\n❌ INVALID Username and Password! Try Again. You have ({attempts_remaining}) attempts remaining.")
                else:
                    print("\n🔒 MAXIMUM ATTEMPTS EXCEEDED. ACCOUNT LOCKED.")
        return False

    def reset_password(self):
        """Allows the user to set a new password."""
        print("\n--- PASSWORD RESET ---")

        #if self.attempts >= self.max_attempts:
            #print("🛑 Cannot reset password. Account is currently locked due to too many failed login attempts.")
            # False

        new_password = input("Enter your new password: ")
        confirm_password = input("Confirm your new password: ")

        if len(new_password) < 8:
            print("Error: New password must be at least 8 characters long.")
            return False

        if new_password == confirm_password:
            self._password = new_password
            print("✅ Password has been reset successfully.")
            return True
        else:
            print("❌ Error: Passwords do not match.")
            return False


login_system = LoginSystem("Aimal", "12345678")

is_logged_in = login_system.login()

if not is_logged_in:
    login_system.reset_password()
